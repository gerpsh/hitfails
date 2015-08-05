function readURL(input, num) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#picture-' + num + '-preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_picture1").change(function(){
    readURL(this, '1');
});

$("#id_picture2").change(function(){
    readURL(this, '2');
});

$("#id_picture3").change(function(){
    readURL(this, '3');
});