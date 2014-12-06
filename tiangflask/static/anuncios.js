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
            { id: 'general', text: 'General', group: true, expanded: true, nodes: [
                { id: 'grid1', text: 'Grid 1', img: 'icon-page', selected: true },
                { id: 'grid2', text: 'Grid 2', img: 'icon-page' },
                { id: 'html', text: 'Some HTML', img: 'icon-page' }
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
                case 'html':
                    w2ui.layout.content('main', '<div style="padding: 10px">Some HTML</div>');
                    $(w2ui.layout.el('main'))
                        .removeClass('w2ui-grid')
                        .css({ 
                            'border-left': '1px solid silver'
                        });
                    break;
            }
        }
    },
    grid1: { 
        name: 'grid1',
        show: {
            header  : true,
            toolbar : true,
            footer  : true,
        },
        toolbar: {
            items: [
                { id: 'add', type: 'button', caption: 'Add Record', icon: 'w2ui-icon-plus' }
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
            { field: 'publicado', caption: 'Publicado', size: '60px', sortable: true, resizable: true, 
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
        
    },
    grid2: { 
        name: 'grid2',
        columns: [
            { field: 'state', caption: 'State', size: '80px' },
            { field: 'title', caption: 'Title', size: '100%' },
            { field: 'priority', caption: 'Priority', size: '80px', attr: 'align="center"' }
        ],
        records: [
            { recid: 1, state: 'Open', title: 'Short title for the record', priority: 2 },
            { recid: 2, state: 'Open', title: 'Short title for the record', priority: 3 },
            { recid: 3, state: 'Closed', title: 'Short title for the record', priority: 1 },
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
