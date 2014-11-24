w2utils.locale('bower_components/w2ui/locale/es-mx.json');


$(function () {
    $('#form').w2form({ 
        name   : 'anuncioForm',
        header : 'Crear Anuncio',
        url    : 'http://127.0.0.1:5000/crear',
        fields : [
            { field: 'autor', type: 'text', required: true, html: 
                { caption: 'Autor', attr: 'style="width: 300px"' } },
            { field: 'titulo',  type: 'text', required: true, html: 
                { caption: 'Titulo', attr: 'style="width: 300px"' } },
            { field: 'descripcion',   type: 'textarea', html: 
                { caption: 'Descripcion', attr: 'style="width: 300px; height: 90px"' } },
            { field: 'fecha_expira',  type: 'date'}
                
        ],
        actions: {
            'Guardar y Continuar': function (event) {
                console.log('guardar', event);
                this.save();
            },
            'Limpiar': function (event) {
                console.log('limpiar', event);
                this.clear();
            },
        }
    });
});
