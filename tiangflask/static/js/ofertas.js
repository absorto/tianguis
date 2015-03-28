
function o_edit_top_form(record) {
  return { 
    name  : 'o_edit_top_form',
    recid : record.recid,
    //  url   : 'server/post',
    fields: [ 
      { field: 'asunto', type: 'text', required: true },
// TODO: get these from server      
      { field: 'destinatarios', type: 'enum', required: true, 
        options: { items: ['Adams, John', 'Johnson, Peter', 'Lewis, Frank', 'Cruz, Steve', 'Donnun, Nick'] }},

// TODO: get these from server
      { field: 'listas', type: 'enum',  
        options: { items: ['todos', 'la roma', 'sur', 'veganos', 'tianguis el 100'],
                   openOnFocus: true, }},
      { field: 'vigencia', type: 'date',
        options: { format: 'm/d/yyyy' }},

      { field: 'publicada', type: 'checkbox', required: false },
      
      // TODO: use tinymce on textarea
      { field: 'cartel', type: 'textarea'}
    ],
  }
}



var o_edit_itemgrid = {
  name  : 'o_edit_itemgrid',
  header: 'items en venta',
  show  : {
    header       : true,
    toolbar      : true,
    toolbarDelete: true,
    toolbarSave  : false
  },
  toolbar: {
    items: [
      { id: 'add', type: 'button', caption: 'Otro item', icon: 'w2ui-icon-plus' }
    ],
    onClick: function (event) {
      if (event.target == 'add') {
        w2ui.o_edit_itemgrid.add({ recid: w2ui.o_edit_itemgrid.records.length + 1 });
      }
    }
  },
  columns: [                
    { field: 'text', caption: 'nombre', size: '120px', sortable: true, resizable: true, 
      editable: { type: 'text' }
    },
    { field: 'desc', caption: 'descripción', size: '50%', sortable: true, resizable: true, 
      editable: { type: 'text' }
    },
    { field: 'presentacion', caption: 'presentación', size: '100px', sortable: true, resizable: true, 
      editable: { type: 'combo', items: unidades, openOnFocus: true } 
    },
    { field: 'precio', caption: 'precio', size: '80px', sortable: true, resizable: true, render: 'money',
      editable: { type: 'money' }
    },
  ],
}








var o_edit_bottom_toolbar = {
  name: 'savebar',
  items: [
    { id: 'spcer', type: 'spacer' },
    { id: 'save', type: 'button', caption: 'guardar y cerrar', img: 'icon-page'}
  ],
  onClick: function (event) {
    if (event.target == 'save') {
      errors = w2ui.o_edit_top_form.validate( showErrors=true );
      if (errors.length == 0) {
        $.ajax({
          type: "POST",
          url: "/ofertas/save",
          data: JSON.stringify( {
            'recid'   : w2ui.o_edit_top_form.recid,
            'top_form': w2ui.o_edit_top_form.record,
            'itemgrid': w2ui.o_edit_itemgrid.records} ),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          error: function(errMsg) {
            console.log(errMsg);
            w2ui.o_mias.error("AJAX error" + errMsg.responseText);
          },
          success: function() {
            w2popup.close();
          }
        });
      }
    }
  }
}





function asunto(recid) {
  if (recid=="nueva") {
    return 'crear oferta nueva';
  } else {
    return 'editar oferta ' + recid;
  }
}


function o_edit_popup(record) {
  w2popup.open({
    title   : asunto(record.recid),
    width   : 900,
    height  : 600,
    showMax : true,
    body    : '<div id="poplayout" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
    onOpen  : function (event) {
      event.onComplete = function () {
        $('#w2ui-popup #poplayout').w2layout(ad_layout);
        w2ui.ad_layout.content('top', "<div id='o_edit_top_form'></div>");
        $('#o_edit_top_form').w2form(o_edit_top_form(record));
        w2ui.o_edit_top_form.record = record;
        w2ui.ad_layout.content('main', $().w2grid(o_edit_itemgrid));
        w2ui.o_edit_itemgrid.add(record.items);
        w2ui.ad_layout.content('bottom', $().w2toolbar( o_edit_bottom_toolbar ));
        this.max();
        w2ui.ad_layout.resize();
      }
    },
    onToggle: function (event) { 
      event.onComplete = function () {
        w2ui.ad_layout.resize();
      }
    },
    onClose: function(event) {
      w2ui.o_edit_top_form.destroy();
      w2ui.o_edit_itemgrid.destroy();
      w2ui.savebar.destroy();
      w2ui.ad_layout.destroy();
      w2ui.o_mias.reload();      
    }
  });
}






