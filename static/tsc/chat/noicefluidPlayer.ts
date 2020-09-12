"use strict";
// #region YT player

// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var YT: any

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '360',
        width: '640',
        videoId: 'M7lc1UVf-VE',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        },
        playerVars: { 'controls': 0, 'cc_load_policy': 0, 'color': 'white', 'disablekb': 1, 'fs': 1, 'iv_load_policy': 3, 'modestbranding': 1, 'rel': 0, 'showinfo': 0, 'autoplay': 0 },
    });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {

    // event.target.playVideo();
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
        setTimeout(stopVideo, 6000);
        done = true;
    }
}

function stopVideo() {
    player.stopVideo();
}

//#endregion


//#region WebSocket
var wss_protocol = window.location.protocol == 'https:' ? 'wss://' : 'ws://';
var chatSocket = new WebSocket(wss_protocol + window.location.host + '/ws/chat/');
// TODO obtain the history
chatSocket.onopen = function (e) {
    document.querySelector('#chat-log').value +=
        "Socket Connection Succesfully!\nWelcome to the noicefluid chat.\nHere you can chat in realtime with all others.\n";
};
chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    console.log(data);
    var message = data['message'];
    if (data['id'] == "msg") {
        document.querySelector('#chat-log').value += message + '\n';
    }
    else {
        alert(message);
        //             var counter = 0;
        //             data.items.forEach(item => {
        //                 counter += 1;
        //                 var video = <HTMLInputElement>(document.createElement('Input'));
        //                 video.classList.add("thumbnails", `video${(counter % 2) + 1}`);
        //                 video.src = item.snippet.thumbnails.high.url;
        //                 video.id = item.id.videoId;
        //                 video.type = "image";
        //                 video.onclick = function () { $(this).attr('class') };
        //                 $("#videos").append(video)
    }
};
chatSocket.onclose = function (e) {
    document.querySelector('#chat-log').value +=
        'Socket closed, please reload the page.\n';
};

//#endregion
//#region send buttons
document.querySelector('#chat-message-submit').onclick = function (e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        type: 'chat_message',
        content: message,
        author: 'fixedUser'
    }));
    messageInputDom.value = '';
};
document.querySelector('#chat-message-search').onclick = function (e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        type: 'command_message',
        content: message,
        author: 'fixedUser',
        task: 'queryvideo'
    }));
    messageInputDom.value = '';
};
//#endregion

//# sourceMappingURL=noicefluidPlayer.js.map