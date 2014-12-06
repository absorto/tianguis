w2utils.locale('bower_components/w2ui/locale/es-mx.json');

// widget configuration
var config = {
    layout: {
        name: 'layout',
        padding: 0,
        panels: [
            { type: 'left', size: 200, resizable: true, minSize: 120 },
            { type: 'main', minSize: 550, overflow: 'hidden' }
        ]
    },
    sidebar: {
        name: 'sidebar',
        nodes: [ 
            { id: 'general', text: 'Yo', group: true, expanded: true, nodes: [
                { id: 'grid1', text: 'Ofertas', img: 'icon-page', selected: true },
                { id: 'grid2', text: 'Pedidos', img: 'icon-page' },
            ]}
        ],
        onClick: function (event) {
            switch (event.target) {
                case 'grid1':
                    w2ui.layout.content('main', w2ui.grid1);
                    break;
                case 'grid2':
                    w2ui.layout.content('main', w2ui.grid2);
                    break;
            }
        }
    },
    grid1: { 
        name: 'grid1',
        show: {
            header  : true,
            toolbar : true,
            toolbarDelete: true,
            toolbarSave: true,
            toolbarEdit: true
        },
        toolbar: {
            items: [
                { id: 'add', type: 'button', caption: 'Nueva oferta', icon: 'w2ui-icon-plus' }
            ],
            onClick: function (event) {
                if (event.target == 'add') {
                    w2ui.grid1.add({ recid: w2ui.grid1.records.length + 1 });
                }
            }
        },
        columns: [
            { field: 'titulo', caption: 'Título', size: '180px', editable: { type: 'text' } },
            { field: 'desc', caption: 'Descripción', size: '180px', editable: { type: 'text' } },
            { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true, editable: { type: 'date' },   },
            { field: 'publicado', caption: 'Publicado', size: '100px', sortable: true, resizable: true, 
                editable: { type: 'checkbox' } 
            },
        ],
        records: [
            { recid: 1, titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
            { recid: 2, titulo: 'A domicilio', desc: 'fruta y verdura otoñal', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
        ],
        searches: [
            { type: 'date', field: 'vigencia', caption: 'Vigencia' }
        ],
        onEdit: function() {openPopup()},
    },
    grid2: { 
        name: 'grid2',
                show: {
            header  : true,
            toolbar : true,
        },
        toolbar: {
            items: [
                { id: 'add', type: 'button', caption: 'Nueva oferta', icon: 'w2ui-icon-plus' }
            ],
            onClick: function (event) {
                if (event.target == 'add') {
                    w2ui.grid1.add({ recid: w2ui.grid1.records.length + 1 });
                }
            }
        },
        columns: [
            { field: 'titulo', caption: 'Título', size: '180px', editable: { type: 'text' } },
            { field: 'desc', caption: 'Descripción', size: '180px', editable: { type: 'text' } },
            { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true, editable: { type: 'date' },   },
            { field: 'publicado', caption: 'Publicado', size: '100px', sortable: true, resizable: true, 
                editable: { type: 'checkbox' } 
            },
        ],
        records: [
            { recid: 1, titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
            { recid: 2, titulo: 'A domicilio', desc: 'fruta y verdura otoñal', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
        ],
        searches: [
            { type: 'date', field: 'vigencia', caption: 'Vigencia' }
        ]

    }
}

$(function () {
    // initialization
    $('#main').w2layout(config.layout);
    w2ui.layout.content('left', $().w2sidebar(config.sidebar));
    w2ui.layout.content('main', $().w2grid(config.grid1));
    // in memory initialization
    $().w2grid(config.grid2);
});



function openPopup() {
    w2popup.open({
        title   : 'Popup',
        width   : 900,
        height  : 600,
        showMax : true,
        body    : '<div id="popped" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
        onOpen  : function (event) {
            event.onComplete = function () {
                $('#w2ui-popup #popped').w2render('poplayout');
//                w2ui.layout.content('left', w2ui.grid);
//                w2ui.layout.content('main', w2ui.form);
            };
        },
        onToggle: function (event) { 
            event.onComplete = function () {
                w2ui.layout.resize();
            }
        }
    });
}
