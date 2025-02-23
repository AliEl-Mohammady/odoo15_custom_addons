odoo.define('pos_add_button.PaymentScreen', function(require) {
    "use strict";
//Extend component and add functionalite to it

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');


    const PosSAPaymentScreenAddButton = PaymentScreen => class extends PaymentScreen {
        showPopup() {
            Gui.showPopup('ErrorPopup', {
                title: this.env._t('Popup to test this Button'),
                body: this.env._t('Component is working well'),
            });
        }
    };

    Registries.Component.extend(PaymentScreen, PosSAPaymentScreenAddButton);

    return PosSAPaymentScreenAddButton;
})