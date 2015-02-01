////////////////
// top layout //
////////////////

var pstyle = 'background-color: #F5F6F7; border: 1px solid #dfdfdf; padding: 5px;';

var layout = { name: 'layout',
               padding: 0,
               panels: [
            { type: 'top',  size: 50, resizable: true, style: pstyle, content: 'top' },
            { type: 'left', size: 200, resizable: true, style: pstyle, content: 'left' },
            { type: 'main', style: pstyle, content: 'main' },
            { type: 'preview', size: '50%', resizable: true, style: pstyle, content: "<div id='editor'> <textarea></textarea> </div>" },
//            { type: 'right', size: 200, resizable: true, style: pstyle, content: 'right' },
//            { type: 'bottom', size: 50, resizable: true, style: pstyle, content: 'bottom' }
                 
                 // { type: 'left', size: 200, resizable: true, minSize: 120 },
                 // { type: 'left', size: 200, resizable: true, minSize: 120 },
                 // { type: 'main', minSize: 550, overflow: 'hidden' },
                 // { type: 'preview', minSize: 550, overflow: 'hidden' }
               ]
             };

