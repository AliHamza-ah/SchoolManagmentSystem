from django.forms.widgets import Input
try:
    from mptt.models import MPTTModel
except ImportError:
    class MPTTModel(object):
        pass


class SimpleChoices(object):

    def __init__(self, *cascadings, empty1="-"*10, empty2="-"*10):
        self.cascadings = cascadings
        self.empty1 = empty1
        self.empty2 = empty2

    def get_selected_item_path(self, value):
        for cascading in self.cascadings:
            for item in cascading[1]:
                if value == item[0]:
                    return [cascading[0], item[0]]
        return None

    def __call__(self, value):
        selectors = []
        selected_item_path = self.get_selected_item_path(value)
        root = {
            "path": [],
            "empty": self.empty1,
            "options": [],
            "hidden": False,
        }
        selectors.append(root)
        for cascading in self.cascadings:
            root["options"].append({
                "title": cascading[0],
                "value": cascading[0],
                "selected": selected_item_path and cascading[0] == selected_item_path[0],
            })
            selector2 = {
                "path": [cascading[0]],
                "empty": self.empty2,
                "options": [],
                "hidden": not (selected_item_path and cascading[0] == selected_item_path[0]),
            }
            for item in cascading[1]:
                selector2["options"].append({
                    "title": item[1],
                    "value": item[0],
                    "selected": selected_item_path and item[0] == selected_item_path[1],
                })
            selectors.append(selector2)
        return selectors

SimpleChoices2 = SimpleChoices

class _Object(object):
    pass

class CascadingModelchoices(object):
    def __init__(self, *cascadings):
        self.cascadings = cascadings

    def get_title(self, item, cascading):
        if "str" in cascading:
            value = getattr(item,cascading["str"])
            if callable(value):
                return value()
            else:
                return value
        else:
            return str(item)

    def get_empty(self, cascading):
        if "empty" in cascading:
            return cascading["empty"]
        else:
            return "----- {0} -----".format(cascading["model"]._meta.verbose_name)

    def get_selected_item_path(self, item):
        if isinstance(item, _Object):
            return []
        else:
            selected_item_path = []
            for cascading in reversed(self.cascadings):
                selected_item_path.append(item.pk)
                if not "fk_name" in cascading:
                    break
                item = getattr(item, cascading["fk_name"])
            selected_item_path.reverse()
            return selected_item_path

    def get_selected_item(self, value):
        if value:
            # if selected, found the selected item
            selected_item = self.cascadings[-1]["model"].objects.get(pk=int(value))
        else:
            # if no selected, create an empty selected item
            selected_item = _Object()
            item = selected_item
            for cascading in reversed(self.cascadings):
                setattr(item, "pk", None)
                if not "fk_name" in cascading:
                    break
                setattr(item, cascading["fk_name"], _Object())
                item = getattr(item, cascading["fk_name"])
        return selected_item

    def get_related_names(self):
        # get related_names to do queryset.prefetch_related, so that only query database one time.
        prefix = ""
        related_names = []
        for cascading in self.cascadings[:-1]:
            related_name = prefix + cascading["related_name"]
            related_names.append(related_name)
            prefix = related_name + "__"
        return related_names

    def get_root_queryset(self, related_names=None):
        related_names = related_names
        if related_names:
            root_queryset = self.cascadings[0]["model"].objects.prefetch_related(*related_names).all()
        else:
            root_queryset = self.cascadings[0]["model"].objects.all()
        return root_queryset

    def walk(self, root_item, queryset, index, choices, path, selected_item_path):
        cascading = self.cascadings[index]
        root = {
            "path": [] + path,
            "empty": self.get_empty(cascading),
            "options": [],
            "hidden": not (index == 0 or (root_item and selected_item_path and root_item.pk == selected_item_path[index - 1])),
        }
        choices.append(root)
        for item in queryset:
            root["options"].append({
                "title": self.get_title(item, cascading),
                "value": item.pk,
                "selected": selected_item_path and item.pk == selected_item_path[index],
            })
        if index <= len(self.cascadings) - 1:
            for item in queryset:
                if "related_name" in cascading:
                    if isinstance(item, MPTTModel):
                        item_tree = item.get_descendants(include_self=True).all()
                        next_cascading = self.cascadings[index + 1]
                        next_queryset = next_cascading["model"].objects.filter(**{next_cascading["fk_name"]+"__in": item_tree}).all()
                    else:
                        next_queryset = getattr(item, cascading["related_name"]).all()
                    self.walk(item, next_queryset, index+1, choices, [] + path + [item.pk], selected_item_path)

    def __call__(self, value):
        selected_item = self.get_selected_item(value)
        selected_item_path = self.get_selected_item_path(selected_item)
        related_names = self.get_related_names()
        # do walk
        choices = []
        root_path = []
        root_queryset = self.get_root_queryset(related_names)
        self.walk(None, root_queryset, 0, choices, root_path, selected_item_path)
        # return the result
        return choices

class DjangoCascadingDropdownWidget(Input):
    template_name = "django-cascading-dropdown-widget/django-cascading-dropdown-widget.html"
    input_type = "text"

    class Media:
        css = {
            "all": [
                "django-cascading-dropdown-widget/css/django-cascading-dropdown-widget.css",
            ]
        }
        js = [
            "admin/js/vendor/jquery/jquery.js",
            "django-cascading-dropdown-widget/js/django-cascading-dropdown-widget.js",
            "admin/js/jquery.init.js",
        ]

    def __init__(self, attrs=None, choices=None):
        """choices must be a callable object or function.
        """
        attrs = attrs or {}
        attrs["hidden"] = "hidden"
        attrs["class"] = attrs.get("class", "") + " django-cascading-dropdown-widget-hidden-input"
        super().__init__(attrs)
        self.django_cascading_dropdown_widget_choices = choices

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context.update({
            "choices": self.get_choices(value),
        })
        return context

    def get_choices(self, value):
        return self.django_cascading_dropdown_widget_choices(value)
