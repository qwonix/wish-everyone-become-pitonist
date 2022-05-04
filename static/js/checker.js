toastr.options = {
    positionClass: "toast-top-center toast-top-full-width",
    preventDuplicates: true
};

$('#exampleInputNickname1').bind('input propertychange', function () {
    $('#labelExampleInputNickname1').text('Никнейм (' + this.value.length + ' символов)')
});

$('#exampleInputTitle1').bind('input propertychange', function () {
    $('#labelExampleInputTitle1').text('Заголовок (' + this.value.length + ' символов)')
});

$('#exampleTextarea').bind('input propertychange', function () {
    $('#labelExampleTextarea').text('Ваш текст (' + this.value.length + ' символов)')
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
