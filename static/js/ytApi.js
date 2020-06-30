var tag = document.createElement("script");

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player("player", {
    width: "1280",
    height: "720",
    videoId: "lTRiuFIWV54",
    playerVars: {
      controls: 0,
      modestbranding: 1,
      ivloadpolicy: 3,
      rel: 0,
    },
    events: {
      onReady: onPlayerReady,
    },
  });
}
var done = false;

function onPlayerReady(event) {
  event.target.playVideo();
}

//SOCKET
const socket = io();

$("#send").on("click", function () {
  socket.send($("#myMessage").val());
  $("#myMessage").val(" ");
});

socket.on("message", function (msg) {
  player.loadVideoById(msg, 0, "large");

  $("#messages").append("<li>" + msg + "</li>");
});
