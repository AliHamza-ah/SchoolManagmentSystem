(function($){
    $(document).on("change", ".django-cascading-dropdown-widget-select", function(){
        var ignore_first_change_event = $(this).attr("ignore-first-change-event");
        if(ignore_first_change_event == "true"){
            $(this).removeAttr("ignore-first-change-event");
        }else{
            var value = $(this).val();
            var name = $(this).attr("data-name");
            var show_name = name + "-" + value;
            var input = $(this).prevAll(".django-cascading-dropdown-widget-hidden-input");
            $(this).nextAll().val("").hide();
            var next_select = $(this).nextAll(".django-cascading-dropdown-widget-select[data-name=" + show_name + "]");
            if(next_select.length > 0){
                next_select.show();
                input.val("").change();
            }else{
                input.val(value).change();
            }
        }
    });
})(jQuery);
