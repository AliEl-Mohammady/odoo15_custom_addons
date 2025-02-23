odoo.define('pos_add_button.ProductTestButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    const { Gui } = require('point_of_sale.Gui');

    class ProductTestButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }

        onClick() {
            console.log(this.env.pos.get_cashier())
            console.log(this.env.pos.get_cashier().user_id)
            Gui.showPopup('ErrorPopup', {
                title: this.env._t('Popup to Call So Button'),
                body: this.env.pos.get_cashier().name,
            });
        }
    }


    ProductTestButton.template = 'ProductTestButton';

    ProductScreen.addControlButton({
        component: ProductTestButton,
        condition: () => true,
        position: ['before', 'SetFiscalPositionButton'],
    });


    Registries.Component.add(ProductTestButton);

    return ProductTestButton;
});
