w2utils.locale('bower_components/w2ui/locale/es-mx.json');
// # /ofertas/mias
// # /overtas/inbox
// # /ofertas/mercado


// # /pedidos/mios
// # /pedidos/inbox
// # /pedidos/mercado


var unidades = ['kg', 'bolsa', 'ramo', 'litro', 'domo', 'manojo', 'pieza'];




function p_itemgrid(recid) {
    return { 
        name: 'p_itemgrid', 
        show: {
            toolbar: true,
            toolbarDelete: true,
            toolbarSave: true
        },
//        url: '/'+recid,

        columns: [                
            { field: 'nombre', caption: 'nombre', size: '120px', sortable: true, resizable: true },
            { field: 'desc', caption: 'descripción', size: '50%', sortable: true, resizable: true },
            { field: 'presentacion', caption: 'presentación', size: '100px', sortable: true, resizable: true },
            { field: 'precio', caption: 'precio', size: '80px', resizable: true, render: 'money' },
            { field: 'cantidad', caption: 'cantidad', size: '80px', resizable: true, render: 'float:3',
              editable: { type: 'float' } }
        ],
        records: [
            { recid: 1, nombre: "jitomate", desc: 'hidroponico', presentacion: 'kg', cantidad: 2.2 }
        ]
    }
}











// initialization
$(function () {
    $('#main').w2layout(layout);
    w2ui.layout.content('left', $().w2sidebar(sidebar));
    w2ui.layout.content('main', $().w2grid(o_mias));
    w2ui.o_mias.autoLoad = false;
    w2ui.o_mias.skip(0);
});


