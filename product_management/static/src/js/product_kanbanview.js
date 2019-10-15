odoo.define('product_management.product_kanbanview', function (require) {
"use strict";

    var ProductKanbanController = require('product_management.product_kanbancontroller');
    var ProductKanbanModel = require('product_management.product_kanbanmodel');
    var ProductKanbanRenderer = require('product_management.product_kanbanrender');
    var config = require('web.config');
    var core = require('web.core');
    var KanbanView = require('web.KanbanView');
    var view_registry = require('web.view_registry');

    var _lt = core._lt;

    var ProductKanbanView = KanbanView.extend({
        config: _.extend({}, KanbanView.prototype.config, {
            Controller: ProductKanbanController,
            Model: ProductKanbanModel,
            Renderer: ProductKanbanRenderer,
        }),
        display_name: _lt('Product Management'),
        groupable: false,
    });

    view_registry.add('product_kanban', ProductKanbanView);

    return ProductKanbanView;

});