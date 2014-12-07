w2utils.locale('bower_components/w2ui/locale/es-mx.json');
// # /ofertas/mias
// # /overtas/inbox
// # /ofertas/mercado


// # /pedidos/mios
// # /pedidos/inbox
// # /pedidos/mercado

// widget configuration
var unidades = ['kg', 'bolsa', 'ramo', 'litro', 'domo', 'manojo', 'pieza'];

var config = {

    ////////////////////
    // layout general //
    ////////////////////
    layout: {
        name: 'layout',
        padding: 0,
        panels: [
            { type: 'left', size: 200, resizable: true, minSize: 120 },
            { type: 'main', minSize: 550, overflow: 'hidden' }
        ]
    },

    /////////////
    // sidebar, va en left //
    /////////////
    sidebar: {
        name: 'sidebar',
        nodes: [ 
            { id: 'ofertas', text: 'Ofertas', group: true, expanded: true, nodes: [
                { id: 'o_mias', text: 'Mías', img: 'icon-home', selected: true },
                { id: 'o_inbox', text: 'Inbox', img: 'icon-folder' },
                { id: 'o_mercado', text: 'En el mercado', img: 'icon-page' },
            ]},
            { id: 'pedidos', text: 'Pedidos', group: true, expanded: true, nodes: [
                { id: 'p_mias', text: 'Mis pedidos', img: 'fa-home' },
                { id: 'p_inbox', text: 'Inbox', img: 'icon-folder' },
                { id: 'p_mercado', text: 'En el mercado', img: 'icon-page' },
            ]}

        ],
        onClick: function (event) {
            switch (event.target) {
                case 'o_mias':
                    w2ui.layout.content('main', w2ui.grid1);
                    break;
            case 'o_inbox':
                    $().w2grid(config.grid2);
                    w2ui.layout.content('main', w2ui.grid2);
                    break;
            }
        }
    },


    /////////////
    // ofertas //
    /////////////
    grid1: { 
        name: 'grid1',
        show: {
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
        // sustituir por llamada al api
        records: [
            { recid: 1, titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
            { recid: 2, titulo: 'A domicilio', desc: 'fruta y verdura otoñal', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
        ],
        searches: [
            { type: 'date', field: 'vigencia', caption: 'Vigencia' }
        ],
        // falta onSave
        onEdit: function() {
            $().w2grid(itemgrid);
            openPopup();
        },
    
    },

    /////////////
    // pedidos //
    /////////////
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




var itemgrid = { 
    name: 'itemgrid', 
    show: {
        toolbar: true,
        toolbarDelete: true,
        toolbarSave: true,
    },
    toolbar: {
        items: [
            { id: 'add', type: 'button', caption: 'Otro item', icon: 'w2ui-icon-plus' }
        ],
        onClick: function (event) {
            if (event.target == 'add') {
                w2ui.grid1.add({ recid: w2ui.itemgrid.records.length + 1 });
            }
        }
    },

    columns: [                
        { field: 'text', caption: 'nombre', size: '120px', sortable: true, resizable: true, 
          editable: { type: 'text' }
        },
        { field: 'desc', caption: 'descripci&oacute;n', size: '120px', sortable: true, resizable: true, 
          editable: { type: 'text' }
        },
        { field: 'unidad', caption: 'unidad', size: '50%', sortable: true, resizable: true, 
                editable: { type: 'combo', items: unidades, showAll: true } 
        },
        { field: 'precio', caption: 'precio', size: '80px', sortable: true, resizable: true, render: 'money',
          editable: { type: 'money' }
        },
    ],
    toolbar: {
        items: [
            { id: 'add', type: 'button', caption: 'Nueva oferta', icon: 'w2ui-icon-plus' }
        ],
        onClick: function (event) {
            if (event.target == 'add') {
                w2ui.itemgrid.add({ recid: w2ui.itemgrid.records.length + 1 });
            }
        }
    },
    records: [
    ]
}



function openPopup() {
    w2popup.open({
        title   : 'Items en la oferta',
        width   : 600,
        height  : 600,
        body    : '<div id="poplayout" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
        onOpen  : function (event) {
            event.onComplete = function () {
                $('#w2ui-popup #poplayout').w2render('itemgrid');
            };
        },
        onToggle: function (event) { 
            event.onComplete = function () {
                w2ui.layout.resize();
            }
        }
    });
}



$(function () {
    // initialization
    $('#main').w2layout(config.layout);
    w2ui.layout.content('left', $().w2sidebar(config.sidebar));
    w2ui.layout.content('main', $().w2grid(config.grid1));
});
