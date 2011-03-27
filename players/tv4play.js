// boxee.enableLog(true);
// 
// boxee.setCanPause(true);
// 
// boxee.onPause = function() {
//   browser.execute("playVideo();");
// }
// boxee.onPlay = function() {
//   browser.execute("pauseVideo();");
// }
// 
// function initPlayer() {
//   boxee.log('trying');
//   var widget  = boxee.getActiveWidget();
//   
//   if (widget) {
//     var color = widget.getPixelData(315, 180);
//     if (color.r == 255 && color.g == 255 && color.b == 255) {
//       boxee.log('GO!');
//       widget.click(315,180);
//       return true;
//     }
//   }
//   
//   boxee.log('timeout');
//   setTimeout(initPlayer, 1000);
// }
// 
// boxee.onDocumentLoaded = initPlayer;