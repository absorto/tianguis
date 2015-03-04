/////////////////////////////////
// menu general a la izquierda //
/////////////////////////////////
var sidebar = { name: 'sidebar',
                nodes: [ 
                  { id: 'ofertas', text: 'Ofertas', group: true, expanded: true, nodes: [
                    { id: 'o_mias', text: 'Mías', img: ' w2ui-icon-columns', selected: true },
                    { id: 'o_inbox', text: 'Inbox', img: 'icon-folder' },
                    { id: 'o_mercado', text: 'En el mercado', img: 'icon-page' }
                  ]},
                  { id: 'pedidos', text: 'Pedidos', group: true, expanded: true, nodes: [
                    { id: 'p_mias', text: 'Mis pedidos', img: 'w2ui-icon-columns' },
                    { id: 'p_inbox', text: 'Inbox', img: 'icon-folder' },
                    { id: 'p_mercado', text: 'En el mercado', img: 'icon-page' }
                  ]}

                ],
                onClick: function (event) {
                  switch (event.target) {
                  case 'o_mias':
                    w2ui.layout.content('main', $().w2grid(o_mias));
                    w2ui.layout.content('preview', 'preview oferta');
                    break;
                  case 'o_inbox':
                    $().w2grid(o_inbox);
                    w2ui.layout.content('main', 'w2ui.o_inbox');
                    break;
                  case 'o_mercado':
                    //w2ui.layout.content('main', "la patita se ha enojado ya sabes por qué");
                    $().w2grid(config.o_inbox);
                    w2ui.layout.content('main', 'w2ui.o_inbox');
                    break;
                    
                  case 'p_mias':
                    w2ui.layout.content('main', 'w2ui.grid1');
                    break;
                  case 'p_inbox':
                    $().w2grid(config.o_inbox);
                    w2ui.layout.content('main', 'w2ui.o_inbox');
                    break;
                  case 'p_mercado':
                    //w2ui.layout.content('main', "la patita se ha enojado ya sabes por qué");
                    $().w2grid(config.o_inbox);
                    w2ui.layout.content('main', 'w2ui.o_inbox');
                  }
                }
              };
