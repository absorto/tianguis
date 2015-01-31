




var o_inbox = { 
  name: 'o_inbox',
  show: {
    toolbar : true
  },
  searches: [
    { type: 'date', field: 'vigencia', caption: 'Vigencia' }
  ],
  url: '/ofertas/inbox',
  columns: [
    { field: 'usuario', caption: 'Usuario', size: '180px' },
    { field: 'titulo', caption: 'Título', size: '180px' },
    { field: 'desc', caption: 'Descripción', size: '180px' },
    { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true },
    { field: 'lugar', caption: 'Lugar', size: '180px'}
  ],

  onClick: function (event) {
    $().w2grid(p_itemgrid(event.recid));
    openPedidoItemPopup(event.recid);
  },
        
  records: [
    { recid: 1, usuario: "la granja", titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012', lugar: 'mercado100' },
    { recid: 2, usuario: "la nicolasa", titulo: 'A domicilio', desc: 'fruta y verdura otoñal', email: 'jdoe@gmail.com', vigencia: '4/3/2012', lugar: 'indefinido' }
  ]
};
