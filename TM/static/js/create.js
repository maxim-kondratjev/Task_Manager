var update_button = document.getElementById("add");
var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var form_create = document.getElementById("form_create");

btn.onclick = function(e) {
    modal.style.display = "block";
};

span.onclick = function() {
    modal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};


update_button.onclick = function (e) {
    e.preventDefault();

    const formData = new FormData(form_create);


    $.ajax({
        type: 'POST',
        url: '/fast_task_creation/',
        data: formData,
        processData: false,
        contentType: false,

        success: (result) => {
          modal.style.display = "none";
          $("#tasks").append(result);
        },

        error: (result) => {
          alert('Ошибка')
        }
    });
};