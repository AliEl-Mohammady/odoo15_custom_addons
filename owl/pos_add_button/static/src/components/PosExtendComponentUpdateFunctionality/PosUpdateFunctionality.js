odoo.define('pos_add_button.ExtendDiscountButton', function(require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const DiscountButton=require('pos_discount.DiscountButton');

    ProductScreen.addControlButton({
        component: DiscountButton,
        condition: function() {
            let has_discount_access=true
            console.log(">>>>>>>>>>>>>>>>>>>>>>>>>",this.env.pos.get_cashier().user_id[0])
            if (this.env.pos.get_cashier().user_id[0] != 2){
                has_discount_access=false
            }
            return this.env.pos.config.module_pos_discount && this.env.pos.config.discount_product_id && has_discount_access;
        },
        position : ['replace','DiscountButton']
    });

});
