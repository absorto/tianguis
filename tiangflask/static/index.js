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
                    w2ui.layout.content('main', w2ui.o_mias);
                    break;
            case 'o_inbox':
                    $().w2grid(config.o_inbox);
                    w2ui.layout.content('main', w2ui.o_inbox);
                break;
            case 'o_mercado':
                    w2ui.layout.content('main', "la patita se ha enojado ya sabes por qué");
                    break;

            }
        }
    },


    /////////////
    // ofertas //
    /////////////
    o_mias: { 
        name: 'o_mias',
        url: '/ofertas/mias',
//        method: 'GET', 
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
                    w2ui.o_mias.add({ recid: w2ui.o_mias.records.length + 1 });
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

        searches: [
            { type: 'date', field: 'vigencia', caption: 'Vigencia' }
        ],
        // falta onSave

        // abre lista de items
        onEdit: function(event) {
            $().w2grid(o_itemgrid(event.recid));
            openOfertaItemPopup(event.recid);
        },
    
    },

    /////////////
    // inbox //
    /////////////
    o_inbox: { 
        name: 'o_inbox',
                show: {
                    toolbar : true,
                },
        searches: [
            { type: 'date', field: 'vigencia', caption: 'Vigencia' }
        ],

        columns: [
            { field: 'usuario', caption: 'Usuario', size: '180px' },
            { field: 'titulo', caption: 'Título', size: '180px' },
            { field: 'desc', caption: 'Descripción', size: '180px' },
            { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true },
        ],

        onClick: function (event) {
            $().w2grid(p_itemgrid(event.recid));
            openPedidoItemPopup(event.recid);
        },
        
        records: [
            { recid: 1, usuario: "la granja", titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
            { recid: 2, usuario: "la nicolasa", titulo: 'A domicilio', desc: 'fruta y verdura otoñal', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
        ],

        
    }
}




function o_itemgrid(recid) {
    return { 
        name: 'o_itemgrid', 
        show: {
            toolbar: true,
            toolbarDelete: true,
            toolbarSave: true,
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



function p_itemgrid(recid) {
    return { 
        name: 'p_itemgrid', 
        show: {
            toolbar: true,
            toolbarDelete: true,
            toolbarSave: true,
        },
//        url: '/'+recid,

        columns: [                
            { field: 'nombre', caption: 'nombre', size: '120px', sortable: true, resizable: true, },
            { field: 'desc', caption: 'descripción', size: '50%', sortable: true, resizable: true, },
            { field: 'presentacion', caption: 'presentación', size: '100px', sortable: true, resizable: true, },
            { field: 'precio', caption: 'precio', size: '80px', resizable: true, render: 'money' },
            { field: 'cantidad', caption: 'cantidad', size: '80px', resizable: true, render: 'float:3',
              editable: { type: 'float' } },
        ],
        records: [
            { recid: 1, nombre: "jitomate", desc: 'hidroponico', presentacion: 'kg', cantidad: 2.2 },
        ]
    }
}




function openOfertaItemPopup(recid) {
    w2popup.open({
        title   : 'items en la oferta '+recid,
        width   : 600,
        height  : 600,
        body    : '<div id="poplayout" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
        onOpen  : function (event) {
            event.onComplete = function () {
                $('#w2ui-popup #poplayout').w2render('o_itemgrid');
            };
        },
        onToggle: function (event) { 
            event.onComplete = function () {
                w2ui.layout.resize();
            }
        }
    });
}


function openPedidoItemPopup(recid) {
    w2popup.open({
        title   : 'ordena contra '+recid,
        width   : 600,
        height  : 600,
        body    : '<div id="poplayout" style="position: absolute; left: 5px; top: 5px; right: 5px; bottom: 5px;"></div>',
        onOpen  : function (event) {
            event.onComplete = function () {
                $('#w2ui-popup #poplayout').w2render('p_itemgrid');
            };
        },
        onToggle: function (event) { 
            event.onComplete = function () {
                w2ui.layout.resize();
            }
        }
    });
}






// initialization
$(function () {
    $('#main').w2layout(config.layout);
    w2ui.layout.content('left', $().w2sidebar(config.sidebar));
    w2ui.layout.content('main', $().w2grid(config.o_mias));
    w2ui.o_mias.autoLoad = false;
    w2ui.o_mias.skip(0);
});
