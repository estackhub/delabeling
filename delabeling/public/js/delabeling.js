$(window).on('load', function() {
    frappe.after_ajax(function () {
        if (frappe.boot.delabeling_setting.show_help_menu) {
            
            $('.dropdown-help').attr('style', 'display: block !important');
        }
        if (frappe.boot.delabeling_setting.logo_width) {
            $('.app-logo').css('width',frappe.boot.delabeling_setting.logo_width+'px');
        }
        if (frappe.boot.delabeling_setting.logo_height) {
            $('.app-logo').css('height',frappe.boot.delabeling_setting.logo_height+'px');
        }
        if (frappe.boot.delabeling_setting.navbar_background_color) {
            $('.navbar').css('background-color',frappe.boot.delabeling_setting.navbar_background_color)
        }
        if (frappe.boot.delabeling_setting.custom_navbar_title_style && frappe.boot.delabeling_setting.custom_navbar_title) {
            $(`<span style=${frappe.boot.delabeling_setting.custom_navbar_title_style.replace('\n','')} class="hidden-xs hidden-sm">${frappe.boot.delabeling_setting.custom_navbar_title}</span>`).insertAfter("#navbar-breadcrumbs")
        }
    })
})
