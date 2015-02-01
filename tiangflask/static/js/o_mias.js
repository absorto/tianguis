////////////////////////////////////////////
// grid con mis ofertas
////////////////////////////////////////////
// var o_mias = {
//   name: 'o_mias',
//   url: '/ofertas/mias',

//   show: {
//     toolbar : true,
//     toolbarDelete: true,
//     toolbarSave: false,
//     toolbarEdit: true
//   },

//   toolbar: {
//     items: [
//       { id: 'add', type: 'button', caption: 'Nueva oferta', icon: 'w2ui-icon-plus' },
//       { type: 'break',  id: 'break0' },
//       { id: 'save', type: 'button', caption: 'Guardar', icon: 'w2ui-icon-check' }
//     ],
//     onClick: function (event) {
//       if (event.target == 'add') {
//         console.log('dafuq');
//         var newid = w2ui.o_mias.records.length + 1;
//         w2ui.o_mias.add({ recid: newid });
//         w2ui.o_mias.select( newid );
//       }
//       if (event.target == 'save') {
//         //console.log(w2ui.o_mias.records);
//         w2ui.o_mias.mergeChanges();                     
//         $.ajax({
//           type: "POST",
//           url: "/ofertas/save",
//           data: JSON.stringify( w2ui.o_mias.records ),
//           contentType: "application/json; charset=utf-8",
//           dataType: "json",
//           error: function(errMsg) {
//             console.log(errMsg);
//             w2ui.o_mias.error("AJAX error" + errMsg.responseText);
//           }
//         });
//       }
//     }  
//   }, // toolbar

//   columns: [
//     { field: 'titulo', caption: 'Título', size: '180px', editable: { type: 'text' } },
//     { field: 'desc', caption: 'Descripción', size: '180px', editable: { type: 'text' } },
//     { field: 'vigencia', caption: 'Vigencia', size: '120px', sortable: true, editable: { type: 'date' }},
//     { field: 'publicado', caption: 'Publicado', size: '100px', sortable: true, resizable: true, editable: { type: 'checkbox' } 
//     }
//   ],

//   searches: [
//     { type: 'date', field: 'vigencia', caption: 'Vigencia' }
//   ],

//   // abre lista de items
//   onEdit: function(event) {
//     $().w2grid(o_itemgrid(event.recid));
//     openOfertaItemPopup(event.recid);
//   }
          
// }; // o_mias
