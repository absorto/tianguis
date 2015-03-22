////////////////////////////////////////////
// grid con mis ofertas
////////////////////////////////////////////
var o_mias = {
  name: 'o_mias',
  url: '/ofertas/mias',
  show: {
    toolbar : true,
    toolbarDelete: true,
    toolbarSave: false,
    toolbarEdit: true
  },

  toolbar: {
    items: [
      { id: 'add', type: 'button', caption: 'Nueva oferta', icon: 'w2ui-icon-plus' },
      { type: 'break',  id: 'break0' },
    ],
    onClick: function (event) {
      if (event.target == 'add') {
        o_edit_popup("nueva");
      }
    }
  },
  
  columns: [
    { field: 'asunto', caption: 'Asunto', size: '180px', },
    { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true, },
    { field: 'publicada', caption: 'Publicada', size: '120px', sortable: true, },
//    { field: 'destinatarios', caption: 'Destinatarios', size: '180px', },
    // TODO: un campo que de algun resumen de la oferta, quiza:
    // cuantos productos, cuanto lleva vendido, etc.
  ],

  searches: [
    { type: 'date', field: 'vigencia', caption: 'Vigencia' }
  ],

//   // abre lista de items
  onEdit: function(event) {
    $.get('/ofertas/'+ event.recid,
          function(record) {
            o_edit_popup(record);
          } )
  } 

}
