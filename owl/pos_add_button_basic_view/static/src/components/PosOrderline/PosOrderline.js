odoo.define('pos_add_button_basic_view.InheritOrderLine', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');

    class InheritOrderLine extends PosComponent {
        onClick() {
            const barcode = this.props?.line?.product?.barcode || 'N/A';
            Gui.showPopup('ErrorPopup', {
                title: this.env._t('Product Barcode'),
                body: this.env._t(barcode),
            });
        }
    }

    InheritOrderLine.template = 'InheritOrderLine';

    Registries.Component.add(InheritOrderLine);

    return InheritOrderLine;
});
