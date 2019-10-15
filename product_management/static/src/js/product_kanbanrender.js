odoo.define('product_management.product_kanbanrender', function (require) {
"use strict";

    var ProductKanbanRecord = require('product_management.product_kanbanrecord');
    var KanbanRenderer = require('web.KanbanRenderer');

    var ProductKanbanRenderer = KanbanRenderer.extend({
        config: _.extend({}, KanbanRenderer.prototype.config, {
            KanbanRecord: ProductKanbanRecord,
        }),
        updateSelection: function (selectedRecords) {
            // To keep selected products when switching between pages and filters
            _.each(this.widgets, function (widget) {
                var selected = _.contains(selectedRecords, widget.id);
                widget._updateRecordView(selected);
            });
        },
    });

    return ProductKanbanRenderer;

});
