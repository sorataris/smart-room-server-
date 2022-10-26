// variables
let userName = null;
let state = 'SUCCESS';

// functions
function Message(arg) {
    this.text = arg.text;
    this.message_side = arg.message_side;

    this.draw = function (_this) {
        return function () {
            let $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(_this.message_side).find('.text').html(_this.text);
            $('.messages').append($message);

            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
    }(this);
    return this;
}

function getMessageText() {
    let $message_input;
    $message_input = $('.message_input');
    return $message_input.val();
}

function sendMessage(text, message_side) {
    let $messages, message;
    $('.message_input').val('');
    $messages = $('.messages');
    message = new Message({
        text: text,
        message_side: message_side
    });
    message.draw();
    $messages.animate({scrollTop: $messages.prop('scrollHeight')}, 300);
}

function greet() {
    setTimeout(function () {
        return sendMessage("스마트 홈에 오신걸 환영합니다.", 'left');
    }, 1000);

    setTimeout(function () {
        return sendMessage("사용할 닉네임을 알려주세요.", 'left');
    }, 2000);
}

function onClickAsEnter(e) {
    if (e.keyCode === 13) {
        onSendButtonClicked()
    }
}

function setUserName(username) {

    if (username != null && username.replace(" ", "" !== "")) {
        setTimeout(function () {
            return sendMessage("반갑습니다." + username + "님. 닉네임이 설정되었습니다.", 'left');
        }, 1000);
        setTimeout(function () {
            return sendMessage("저는 편리한 생활을 도와드리는 파트너 스마트 윈도우입니다!", 'left');
        }, 2000);
        setTimeout(function () {
            return sendMessage("저는 날씨정보나 IoT홈 서비스가 필요하실땐 저를 불러주세요!", 'left');
        }, 3000);

        return username;

    } else {
        setTimeout(function () {
            return sendMessage("올바른 닉네임을 이용해주세요.", 'left');
        }, 1000);

        return null;
    }
}

function requestChat(messageText, url_pattern) {
    $.ajax({
        url: "http://127.0.0.1:8080/" + url_pattern + '/' + userName + '/' + messageText,
        type: "GET",
        dataType: "json",
        success: function (data) {
            state = data['state'];

            if (state === 'SUCCESS') {
                return sendMessage(data['answer'], 'left');
            } else if (state === 'REQUIRE_LOCATION') {
                return sendMessage('어느 지역을 알려드릴까요?', 'left');
            }
             else if (state === 'REQUIRE_DO') {
                return sendMessage('어떻게 해드릴까요?', 'left');
            }
            else {
                return sendMessage('죄송합니다. 무슨말인지 잘 모르겠어요.', 'left');
            }
        },

        error: function (request, status, error) {
            console.log(error);

            return sendMessage('죄송합니다. 서버 연결에 실패했습니다.', 'left');
        }
    });
}

function onSendButtonClicked() {
    let messageText = getMessageText();
    sendMessage(messageText, 'right');

    if (userName == null) {
        userName = setUserName(messageText);

    } else {
        if (messageText.includes('안녕')) {
            setTimeout(function () {
                return sendMessage("안녕하세요. 저는 스마트 윈도우 입니다.", 'left');
            }, 1000);
        } else if (messageText.includes('고마워')) {
            setTimeout(function () {
                return sendMessage("천만에요. 더 물어보실 건 없나요?", 'left');
            }, 1000);
        } else if (messageText.includes('없어')) {
            setTimeout(function () {
                return sendMessage("그렇군요. 알겠습니다!", 'left');
            }, 1000);


        } else if (state.includes('REQUIRE')) {
            return requestChat(messageText, 'fill_slot');
        } else {
            return requestChat(messageText, 'request_chat');
        }
    }
}