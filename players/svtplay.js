boxee.enableLog(true);
boxee.setDefaultCrop(0,0,0,26);

// var seekbar = {
//   start: {
//     x: 70,
//     y: 373
//   },
//   end: {
//     x: 440,
//     y: 373
//   },
//   pixels: ['467f2d', '3d7927', '437027', '3b7c27', '3d7f29', '3b7c27', '367522', '326e1c', '4a8331'],
//   getPosition: function(widget) {
//     var xLength = seekbar.end.x - seekbar.start.x,
//         yLength = seekbar.end.y - seekbar.start.y,
//         sLength = xLength >= yLength ? xLength : yLength,
//         steps   = seekbar.pixels.length,
//         xInc    = xLength / steps,
//         yInc    = yLength / steps,
//         x,
//         y;
// 
//     for (var i = 0; i <= sLength; i++) {
//       for (var p in seekbar.pixels) {
//         x = seekbar.start.x + Math.round((i + p) * xInc);
//         y = seekbar.start.y + Math.round((i + p) * yInc);
// boxee.log(x + ' ' +y + ' ' + p);
//         var color     = widget.getPixelData(x, y);
//         var decColor  = (color.b + 256 * color.g + 65536 * color.r);
//         var seekColor = seekbar.pixels[p];
//         
//         if (decColor == parseInt(seekColor, 16)) {  
//           boxee.log('Found match ' + seekColor + ' at ' + x + ' ' + y);
//         } else {
//           break;
//         }
//       }
//     }
//   }
// }


if(boxee.getVersion() > 3.0)
{
  boxee.setCanPause(true);
  boxee.setCanSkip(false);
  boxee.setCanSetVolume(false);
}

boxee.onPause = function() {
	boxee.getActiveWidget().click(16,375);
}
boxee.onPlay = function() {
	boxee.getActiveWidget().click(16,375);
}
boxee.onSkip = function() {
}