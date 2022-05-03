toastr.options = {
    positionClass: "toast-top-center toast-top-full-width",
    preventDuplicates: true
};

function validate_all() {
    let email = $("#exampleInputEmail1").val();
    let nickname = $("#exampleInputNickname1").val();
    let title = $("#exampleInputTitle1").val();
    let description = $("#exampleTextarea").val();

    let arr = {'email': email, 'nickname': nickname, 'title': title, 'description': description}

    let request = new XMLHttpRequest();
    request.open("GET", "check_noveltie/data=" + encodeURI(JSON.stringify(arr)), false);
    request.send();

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
