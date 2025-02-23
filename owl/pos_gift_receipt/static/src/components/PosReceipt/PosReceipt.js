odoo.define('pos_pass_discount.PosReceipt', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class PosReceipt extends PosComponent {
        constructor() {
            super(...arguments);
        }

        mounted(){
            console.log("Hello from inside Extended Component")
        }

        set_default(){
            alert("Set Default")
        }
        set_A4(){
            alert("Set A4")
        }

    }


    PosReceipt.template = 'PosReceipt';
    Registries.Component.add(PosReceipt);

    return PosReceipt;
});
