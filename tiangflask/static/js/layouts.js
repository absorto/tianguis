////////////////
// top layout //
////////////////

var pstyle = 'background-color: #F5F6F7; border: 1px solid #dfdfdf; padding: 5px;';

var base_layout = {
  name: 'base_layout',
  padding: 0,
  panels: [
    { type: 'top',  size: 50, resizable: true, style: pstyle, content: 'top' },
    { type: 'left', size: 200, resizable: true, style: pstyle, content: 'left' },
    { type: 'main', style: pstyle, content: 'main' },
    { type: 'preview', size: '50%', resizable: true, style: pstyle, content: "<div id='editor'> <textarea></textarea> </div>" },
  ]
};


var ad_layout = {
  name: 'ad_layout',
  padding: 0,
  panels: [
    { type: 'top', size: '20%', resizable: true, style: pstyle, content: "formulario" },
    { type: 'main', size: '20%', resizable: true, style: pstyle, content: "<div id='editor'> <textarea></textarea> </div>" },
    { type: 'preview', size: '60%', resizable: true, style: pstyle, content: '' },
  ]
};
