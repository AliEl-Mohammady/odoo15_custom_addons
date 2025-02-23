odoo.define('pos_add_button.TicketButtonAli', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');

    class PosAddButton extends PosComponent {
        onClick() {
            Gui.showPopup('ErrorPopup', {
                title: this.env._t('Popup to test this Button'),
                body: this.env._t('Component is working well'),
            });
        }
    }
    PosAddButton.template = 'PosAddButton';

    Registries.Component.add(PosAddButton);

    return PosAddButton;
});
