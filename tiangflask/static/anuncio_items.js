$(function () {
    $('#grid').w2grid({ 
        name: 'grid', 
        show: { 
            toolbar: true,
//            footer: true,
//            toolbarSave: true
        },
        columns: [                
            { field: 'text', caption: 'nombre', size: '120px', sortable: true, resizable: true, 
                editable: { type: 'text' }
            },
            { field: 'desc', caption: 'descripci&oacute;n', size: '120px', sortable: true, resizable: true, 
                editable: { type: 'text' }
            },
            { field: 'unidad', caption: 'unidad', size: '120px', sortable: true, resizable: true, 
                editable: { type: 'text' }
            },
            { field: 'precio', caption: 'precio', size: '80px', sortable: true, resizable: true, render: 'money',
                editable: { type: 'money' }
            },

        ],
        toolbar: {
            items: [
                { id: 'add', type: 'button', caption: 'Agregar item', icon: 'w2ui-icon-plus' }
            ],
            onClick: function (event) {
                if (event.target == 'add') {
                    w2ui.grid.add({ recid: w2ui.grid.records.length + 1 });
                }
            }
        },
        records: [
        ]
    });    
});

function showChanged() {
    console.log(w2ui['grid'].getChanges()); 
    w2alert('Changed records are displayed in the console');
}
