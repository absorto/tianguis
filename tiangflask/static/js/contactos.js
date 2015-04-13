contactos_grid = { 
        name: 'contactos_grid', 
        show: { 
            toolbar: true,
            footer: true,
            toolbarSave: true
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
                { id: 'add', type: 'button', caption: 'Add Record', icon: 'w2ui-icon-plus' }
            ],
          
            onClick: function (event) {
                if (event.target == 'add') {
                    w2ui.contactos_grid.add({ recid: w2ui.contactos_grid.records.length + 1 });
                }
            }
        }
};


