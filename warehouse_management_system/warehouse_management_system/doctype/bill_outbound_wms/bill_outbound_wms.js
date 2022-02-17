// Copyright (c) 2022, Afrikedge and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bill Outbound WMS', {
	refresh: function(frm) {
    frm.add_custom_button('Update Balance', () => {
      frappe.new_doc('Bill Outbound WMS', {
        bill_outbound_wms:frm.doc.name
      })
    })
	}
});
