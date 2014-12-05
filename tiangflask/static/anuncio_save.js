w2utils.locale('bower_components/w2ui/locale/es-mx.json');

$(function () {
    $('#myForm').w2form({ 
        name   : 'myForm',
        url: 'http://localhost:5000/anuncio_save',
        header: "Crear anuncio",
        fields : [
            { name: 'autor', type: 'text', required: true, html:
              { caption: 'Autor', attr: 'style="width: 300px"' } },
            { name: 'titulo',  type: 'text', required: true, html: 
              { caption: 'Titulo', attr: 'style="width: 300px"' } },
            { name: 'descripcion',   type: 'textarea', html: 
              { caption: 'Descripción', attr: 'style="width: 300px; height: 90px"' } },
            { name: 'fecha_expira',  type: 'date'}
            
        ],
        actions: {
            reset: function () {
                this.clear();
            },
            "save": function (event) {
                this.save();
            }
        },
        onSave: function() {
            window.location = "/anuncios/";
        }
    });
});
