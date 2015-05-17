contactos_grid = {
  url: '/contactos',
  name: 'contactos_grid', 
  show: { 
    toolbar: true,
    footer: true,
    toolbarSave: false,
    toolbarDelete: true          
  },
  columns: [                
    { field: 'nombre', caption: 'Nombre', size: '30%', sortable: true, resizable: true, 
      editable: { type: 'text' }
    },
    { field: 'email', caption: 'Correo', size: '30%', sortable: true, resizable: true,
      editable: { type: 'email' }
    },
    { field: 'phone', caption: 'Teléfono', size: '20%', sortable: false, resizable: true,
      editable: { type: 'text' }
    },
    { field: 'etc', caption: '&c', size: '20%', sortable: false, resizable: true,
      editable: { type: 'text' }
    }
  ],
  toolbar: {
    items: [
      { id: 'add', type: 'button', caption: 'Agregar contacto', icon: 'w2ui-icon-plus' },
      { id: 'save', type: 'button', caption: 'guardar', img: 'icon-page'}
    ],
          
    onClick: function (event) {
      if (event.target == 'add') {
        w2ui.contactos_grid.add({ recid: 'nueva' + (w2ui.contactos_grid.records.length + 1) });
      }
      if (event.target == 'save') {
        $.ajax({
          type: "POST",
          url: "/contactos/save",
          data: JSON.stringify( {
            'itemgrid': w2ui.contactos_grid.records} ),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          error: function(errMsg) {
            console.log(errMsg);
            w2ui.o_mias.error("AJAX error" + errMsg.responseText);
          },
          success: function() {
            w2popup.close();
          }})}}      
  }
};


