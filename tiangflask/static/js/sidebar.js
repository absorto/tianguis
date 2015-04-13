/////////////////////////////////
// menu general a la izquierda //
/////////////////////////////////
var sidebar = { name: 'sidebar',
                nodes: [ 
                  { id: 'ofertas', text: 'Ofertas', group: true, expanded: true,
                    nodes: [
                      { id: 'o_mias', text: 'Mías', img: ' w2ui-icon-columns', selected: true },
                      { id: 'o_inbox', text: 'Inbox', img: 'icon-folder' },
                      { id: 'o_mercado', text: 'En el mercado', img: 'icon-page' }
                    ]},
                  { id: 'pedidos', text: 'Pedidos', group: true, expanded: true,
                    nodes: [
                      { id: 'p_mias', text: 'Mis pedidos', img: 'w2ui-icon-columns' },
                      { id: 'p_inbox', text: 'Inbox', img: 'icon-folder' },
                      { id: 'p_mercado', text: 'En el mercado', img: 'icon-page' }
                    ]
                  },
                  { id: 'contactos_sidebar', text: 'Contactos', group: true, expanded: true,
                    nodes: [
                      { id: 'contactos_grid', text: 'Contactos', img: 'w2ui-icon-columns' },
                      { id: 'listas', text: 'Listas', img: 'icon-folder' },
                    ]
                  },
                  

                ],
                onClick: function (event) {
                  switch (event.target) {
                  case 'o_mias':
                    if (!('o_mias' in w2ui)) {
                      w2ui['base_layout'].content('main', $().w2grid(o_mias));
                      w2ui.base_layout.content('preview', 'preview oferta');
                    } else {
                      w2ui['base_layout'].content('main', w2ui['o_mias']);
                      w2ui.base_layout.content('preview', 'preview oferta');
                    }
                    break;
                  case 'o_inbox':
                    break;
                  case 'o_mercado':
                    break;
                    
                  case 'p_mias':
                    break;
                  case 'p_inbox':
                    break;
                  case 'p_mercado':
                    break;

                  // contactos
                  case 'contactos_grid':
                    if (!('contactos_grid' in w2ui)) {
                      w2ui['base_layout'].content('main', $().w2grid(contactos_grid));
                    } else {
                      w2ui['base_layout'].content('main', w2ui['contactos_grid']);
                    }
                    break;
                    
                  }
                  
                }
              };
