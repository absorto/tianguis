function        asunto(recid) {
  if (recid=="nueva") {
    return 'crear oferta nueva';
  } else {
    return 'editar oferta ' + recid;
  }
}

function o_edit_popup(recid) {
  w2popup.open({
    title   : asunto(recid),
    width   : 900,
    height  : 600,
    body    : '<div id="poplayout" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
    onOpen  : function (event) {
      event.onComplete = function () {
        $('#w2ui-popup #poplayout').w2layout(ad_layout);
        w2ui.ad_layout.content('top', "formulario"); 
        w2ui.ad_layout.content('main', "<div id='editor'> <textarea></textarea> </div>");
        w2ui.ad_layout.content('preview', $().w2grid(o_itemgrid(recid)));
      };
    },
    onToggle: function (event) { 
      event.onComplete = function () {
        w2ui.layout.resize();
      }
    },
    onClose: function(event) {
      w2ui.o_itemgrid.destroy();
      w2ui.ad_layout.destroy();
    }
      
  });
}





function o_itemgrid(recid) {
    return { 
        name: 'o_itemgrid', 
        show: {
            toolbar: true,
            toolbarDelete: true,
            toolbarSave: true
        },
//        url: '/'+recid,

        toolbar: {
            items: [
                { id: 'add', type: 'button', caption: 'Otro item', icon: 'w2ui-icon-plus' }
            ],
            onClick: function (event) {
                if (event.target == 'add') {
                    w2ui.o_itemgrid.add({ recid: w2ui.o_itemgrid.records.length + 1 });
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
        records: [
        ]
    }
}

