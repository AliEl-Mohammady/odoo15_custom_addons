odoo.define('pos_add_button_basic_view.InheritChrome', function(require) {
    'use strict';


    const { useListener } = require('web.custom_hooks');
    const models = require('point_of_sale.models');
    const Chrome = require('point_of_sale.Chrome');
    const Registries = require('point_of_sale.Registries');


    const AddButtonChrome = (Chrome) =>
        class extends Chrome {
            reloadPage() {
            console.log('Reload Page button clicked');
            location.reload(); // Reload the page
            }
        };

    Registries.Component.extend(Chrome, AddButtonChrome);

    return AddButtonChrome;
});
