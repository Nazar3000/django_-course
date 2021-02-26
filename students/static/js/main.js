function initJournal(){
    var indicator = $('#ajax-progress-indicator');
    var danger = $('#alert-danger');

    $('.day-box input[type="checkbox"]').click(function(event){
        var box = $(this), progress = $(".progress");
        $.ajax(box.data('url'),{
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]'
                ).val()
            },
            'beforeSend': function (xhr, settings){
              indicator.show();
              danger.hide();
              $(progress).show();

            },

            'error': function (xhr, status, error){
                // alert(error);
                indicator.hide();
                // .attr(danger, error)
                danger.show().append(error);
            },
            'success': function(data, status, xhr){
                indicator.hide();
                danger.hide();
            }
        });
    });
}



function initGroupSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#group-selector select').change(function(event){
        // get value of currently selected group option
        var group = $(this).val();

        if (group){
            // set cookie with expiration date 1 year sibce now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
        }
        else {
            // otherwies we delete the cookie
            $.removeCookie('current_group', {'path': '/'});
        }
        // and reload a page
        location.reload(true);
        return true;
    });
}


function initDateFilds(){
    $('#datetimepicker2').datetimepicker({
        'format': 'YYYY-MM-DD',
        'locale': 'ru',

    }).on('dp.hide', function (event){
        $(this).blur();
    });
}

// students edit form step1
// function initAddStudentPage() {
//     $('a.student-edit-form-link').click(function(event){
//         var modal = $('#myModal');
//         modal.modal('show');
//         return false;
//     });
// }


function initEditStudentPage() {
    $('a.student-edit-form-link').click(function(event){
        var link = $(this), progress = $(".progress");
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'beforeSend': function () {
                $(progress).show();
            },

            'success': function(data, status, xhr){

                // check if we got successfull response from the server
                if(status !='success'){
                    alert('Ошибка на сервере. Попробуйте позже.');
                    return false;
                }
            // update modal window with arrived content from the server
                var modal = $('#myModal'),
                    html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // Вытаскивам ID студента
                student_id = form.find('.stud_id').attr('id');


                // init our edit form
                initEditStudentForm(form, modal);
                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true});
            },
            'error': function (){
                alert('Ошибка на сервере. Попробуйте позже');
                return false;
            }

        });
        return false;
    });
}


function initEditStudentForm(form, modal) {
    var butons = modal.find(".form-actions"),
        progress = $(".progress");
    // attach datepicker
    initDateFilds();

    // close modal window on Cacncel button click
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });

    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function (){
            alert('Ошибка на сервере. Попробуйте позже.');
            return false;
        },

        // progres indicator for ajax show

        'beforeSend': function (data, status, xhr){



            modal.find('.form-actions').append(progress);

            $(progress).show();
            // modal.find('input').prop('disabled', true);
            // $("input").prop('disabled', true);

        },

        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');


            // copy alert to modal window
            modal.find('.modal-body').html(html.find('.alert'));
            newform.find('.form-actions').append(progress);
            $(progress).show();
            // $("input").prop('disabled', true);


            // copy form to modal if we foud it in server response
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);

                // initialize form fields and buttons
                initEditStudentForm(newform, modal);

            } else {
                // if no form, it means success and we need to reload page
                // to get updated students list;
                // reload after 2 seconds, so that user can read
                // success message

                // Пытаемся вытащить студента по ид
                $.ajax({
                    'url': "http://127.0.0.1:8000/",
                    'async': true,
                    'dataType': 'html',
                    'type': 'get',
                    // 'data': {"student.id": student_id},
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]'
                    ).val(),
                    'success': function (data, status, xhr) {
                        // var cur_list = $('#content-column'), new_html = $(data),
                        //     new_list=new_html.find('#content-column');
                        // cur_list.find(`.stud_id[id=${student_id}]`).html(new_list.find(`.stud_id[id=${student_id}] td`));

                        // alert(stud_selector);
                        // check if we got successfull response from the server
                        if (status != 'success') {
                            alert('Запрос на получение студента не прошел');
                            return false;
                        }
                    }
                });
                var cur_list = $('#content-column'), new_html = $(data),
                            new_list=new_html.find('#content-column');
                setTimeout(function() {modal.modal('hide');}, 5000);
                setTimeout(function() {
                    cur_list.find(`.stud_id[id=${student_id}]`).html(new_list.find(`.stud_id[id=${student_id}] td`));
                }, 7000);

                // setTimeout(function(){location.reload(true);}, 500);
                }
            }
        });
    }

// $(document).on("ajaxSend", function() {
//     $(".progress").show(); // показываем элемент
// }).on("ajaxStop", function(){
//     $(".progress").hide(); // скрываем элемент
// });




$(document).on("ajaxSend", function() {
    $("input").prop('disabled', true);
    $(".student-edit-form-link").prop('disabled', true);
    // $("input").attr("disabled", true);
});


$(document).on("ajaxStop",
    function () {
    $("input").prop('disabled', false);
    $(".student-edit-form-link").prop('disabled', false);
        setTimeout(function () {
                $(".progress").hide(); // скрываем элемент
            },
            3000);
    }
);


$(document).ready(function (){
    initJournal();
    initGroupSelector();
    initDateFilds();
    initEditStudentPage();
});