toastr.options = {
    positionClass: "toast-top-center toast-top-full-width",
    preventDuplicates: true
};

function count_of_vals(number, format) {
    return number + ' ' + format[(number % 100 > 4 && number % 100 < 20) ? 2 : [2, 0, 1, 1, 1, 2][Math.min(number % 10, 5)]];
}

$('#exampleInputNickname1').bind('input propertychange', function () {
    $('#labelExampleInputNickname1').text('Никнейм (' + count_of_vals(this.value.length, ['символ', 'символа', 'символов']) + ')')
});

$('#exampleInputTitle1').bind('input propertychange', function () {
    $('#labelExampleInputTitle1').text('Заголовок (' + count_of_vals(this.value.length, ['символ', 'символа', 'символов']) + ')')
});

$('#exampleTextarea').bind('input propertychange', function () {
    $('#labelExampleTextarea').text('Ваш текст (' + count_of_vals(this.value.length, ['символ', 'символа', 'символов']) + ')')
});

function validate_all() {
    let email = $("#exampleInputEmail1").val();
    let nickname = $("#exampleInputNickname1").val();
    let title = $("#exampleInputTitle1").val();
    let description = $("#exampleTextarea").val();

    let arr = {'email': email, 'nickname': nickname, 'title': title, 'description': description}

    let request = new XMLHttpRequest();
    request.open("POST", "check_noveltie", false);
    request.send(JSON.stringify(arr));

    if (request.status === 200) {
        let data = JSON.parse(request.responseText);
        console.log(data);
        if ('status' in data && data.status === 'ok') {
            return true;
        } else if ('error' in data) {
            toastr.warning(data.error);
        }
    }

    return false;
}
