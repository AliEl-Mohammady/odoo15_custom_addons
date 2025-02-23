odoo.define('owl_list_view_add_buttons.ListViewAddButtons', function (require) {
"use strict";

    const session = require('web.session');
    const ListController = require('web.ListController');


    ListController.include({
        events: _.extend({}, ListController.prototype.events, {
        'click .o_list_button_custom': '_callPythonFunction',
        }),

        _callPythonFunction() {
            return this._rpc({
                model: 'pos.order',
                method: 'get_alert_call_js',
                args: [[]],
            }).then((result) => window.alert(result))
        },
    })
});