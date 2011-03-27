boxee.enableLog(true);

boxee.setCanPause(true);
boxee.setCanSkip(true);
boxee.setCanSetVolume(false);

boxee.notifyPlaybackPaused();

boxee.onPause = function() {
  browser.execute("window.player.pause();");
}
boxee.onPlay = function() {
  browser.execute("window.player.play();");
}
boxee.onSkip = function() {
  var currentPosition = parseFloat(browser.execute("window.player.getVideoPosition()"));
  browser.execute("window.player.seek(" + (currentPosition + 10) + ")")
  boxee.notifyCurrentTime(parseFloat(browser.execute("window.player.getVideoPosition()")));
}
boxee.onBack = function() {
  var currentPosition = parseFloat(browser.execute("window.player.getVideoPosition()"));
  browser.execute("window.player.seek(" + (currentPosition - 10) + ")")
  boxee.notifyCurrentTime(parseFloat(browser.execute("window.player.getVideoPosition()")));
}
boxee.onBigSkip = function() {
  var currentPosition = parseFloat(browser.execute("window.player.getVideoPosition()"));
  browser.execute("window.player.seek(" + (currentPosition + 30) + ")")
  boxee.notifyCurrentTime(parseFloat(browser.execute("window.player.getVideoPosition()")));
}
boxee.onBigBack = function() {
  var currentPosition = parseFloat(browser.execute("window.player.getVideoPosition()"));
  browser.execute("window.player.seek(" + (currentPosition - 30) + ")")
  boxee.notifyCurrentTime(parseFloat(browser.execute("window.player.getVideoPosition()")));
}
boxee.onDocumentLoaded = function() {
  initPlayer();
}

function initPlayer() {
  boxee.log('trying');
  var playerId    = browser.execute("document.getElementsByClassName('BrightcoveExperience')[0].id"),
      experience  = browser.execute("brightcove.getExperience('" + playerId + "').callback");

  if (experience) {
    boxee.log('GO!');
    browser.execute("window.player = brightcove.getExperience('" + playerId + "').getModule(APIModules.VIDEO_PLAYER);");
    browser.execute("window.player.play();");
    var duration = parseFloat(browser.execute("window.player.getVideoDuration();"));
    
    if (duration) {
      browser.execute("window.player.removeUserMessage();");
      browser.execute("window.player.play();");
      boxee.setDuration(duration);
      boxee.notifyPlaybackResumed();
      return true;
    }
  }
  
  boxee.log('timeout');
  setTimeout(initPlayer, 1000);
}