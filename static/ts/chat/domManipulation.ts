// Note The not null assertion operator, will not perform any runtime checks, 
// it just tells the compiler you have special information and you know DOM
// will not be null at runtime.

var wss_protocol = window.location.protocol == 'https:' ? 'wss://' : 'ws://';
const chatSocket = new WebSocket(
    wss_protocol + window.location.host + '/ws/chat/'
);

// TODO obtain the history
chatSocket.onopen = function (e) {
    document.querySelector<HTMLInputElement>('#chat-log')!.value +=
        "Welcome to the noicefluid chat.\nHere you can chat in realtime with all others.\n";
};

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var message = data['message'];
    document.querySelector<HTMLInputElement>('#chat-log')!.value +=
        data.message + '\n';
};

chatSocket.onclose = function (e) {
    document.querySelector<HTMLInputElement>('#chat-log')!.value +=
        'Socket closed unexpectedly, please reload the page.\n';
};



document.querySelector<HTMLInputElement>('#chat-message-input')!.focus();
document.querySelector<HTMLInputElement>('#chat-message-input')!.onkeyup = function (e) {
    if (e.keyCode === 13) { // enter, return
        document.querySelector<HTMLInputElement>('#chat-message-submit')!.click();
    }
};

// SEND
document.querySelector<HTMLInputElement>('#chat-message-submit')!.onclick = function (e) {
    const messageInputDom = document.querySelector<HTMLInputElement>('#chat-message-input')!;
    const message = messageInputDom.value;

    document.querySelector<HTMLInputElement>('#chat-log')!.value +=
        message + '\n';

    messageInputDom.value = '';
};






// SEARCH
document.querySelector<HTMLInputElement>('#chat-message-search')!.onclick = function (e) {
    const messageInputDom = document.querySelector<HTMLInputElement>('#chat-message-input')!;
    const message = messageInputDom.value;

    chatSocket.send(
        JSON.stringify({
            message: message,
        })
    );

    messageInputDom.value = '';
};