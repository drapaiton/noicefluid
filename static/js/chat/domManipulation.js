"use strict";
// Note The not null assertion operator, will not perform any runtime checks, 
// it just tells the compiler you have special information and you know DOM
// will not be null at runtime.
var wss_protocol = window.location.protocol == 'https:' ? 'wss://' : 'ws://';
var chatSocket = new WebSocket(wss_protocol + window.location.host + '/ws/chat/');
// TODO obtain the history
// ChatSocket behaviour
chatSocket.onopen = function (e) {
    document.querySelector('#chat-log').value +=
        "Welcome to the noicefluid chat.\nHere you can chat in realtime with all others.\n";
};
// Append messages
chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    document.querySelector('#chat-log').value +=
        data.message + '\n';
};
// onclose
chatSocket.onclose = function (e) {
    document.querySelector('#chat-log').value +=
        'Socket closed unexpectedly, please reload the page.\n';
};
// Submit Button (enter key)
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {
        // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};
// Submit Button
document.querySelector('#chat-message-submit').onclick = function (e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        message: message,
    }));
    messageInputDom.value = '';
};
