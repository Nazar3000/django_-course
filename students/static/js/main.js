function initJournal(){
    var indicator = $('#ajax-progress-indicator');
    var danger = $('#alert-danger');

    // Обрабатываем клик по чекбоксам журнала, отправляем запрос при каждом клике
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
            // Отображаем индикатор отправки запроса перед самим запрососм
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


// Обрабатываем изменения выпадающего списка групп на странице
// пишем выбранную группу в куки браузера для /
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
        // location.reload(true);

        // or update page with ajax

        // получаем текущуюю ссылку страницы
        url = window.location.href;
        // вызываем функцию обновление контента аяксом
        updateContent(url);
        return true;
    });
}

function initLangSelector(){
$('#lang-selector select').change(function(event){
    // get value of currently selected lang
    var lang = $(this).val();

    if (lang) {
        // set cookie with expiratin date 1 year since now;
        // cookie creation function takes period in days
        $.cookie('django_language', lang, {'path': '/', 'expires': 365}
        );
    }



    else {
        // otherwise we delete the cookie
    $.removeCookie('django_language', {'path': '/'});
}
    // and reload a page
    location.reload(true);
    return true;
});
}

// Виджет календаря
function initDateFilds(){
    $('#datetimepicker2').datetimepicker({
        'format': 'YYYY-MM-DD',
        'locale': 'ru',

    }).on('dp.hide', function (event){
        $(this).blur();
    });
}



// Показываем модальное
function initEditStudentPage() {
    $('a.student-edit-form-link').click(function(event){
        var link = $(this), progress = $(".progress"), url=link.attr('href');
        $.ajax({
            'url': url,
            // 'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'beforeSend': function () {
                $(progress).show();
            },

            'success': function(data, status, xhr){
                changeUrl(url);


                // check if we got successfull response from the server
                if(status !='success'){
                    alert(gettext('There was an error on the server. Please, try again a bit later'));
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
                EventListener(modal);
                // addAtrperview(form);
                // window.history.pushState({page: data, type:"page"}, null, link.attr('href'));
                // window.history.forward()
            },
            'error': function (){
                alert(gettext('There was an error on the server. Please, try again a bit later'));
                return false;
            }

        });
        return false;
    });
}

// Обрабатываем постзапрос на аяксе для модального окна,
// после применения изменений обновляем редактированного студента в спске
function initEditStudentForm(form, modal) {
    var butons = modal.find(".form-actions"),
        progress = $(".progress");
    // attach datepicker
    initDateFilds();
    addAtrperview(form);

    // close modal window on Cacncel button click
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });

    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function (){
            alert(gettext('There was an error on the server. Please, try again a bit later'));
            return false;
        },

        // progres indicator for ajax show

        'beforeSend': function (data, status, xhr){
            modal.find('.form-actions').append(progress);
            $(progress).show();
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
                $('#frame').hide();

                // if no form, it means success and we need to reload page
                // to get updated students list;
                // reload after 2 seconds, so that user can read
                // success message

                // Вытаскиваем обновленный список студентов чтобы после вытащить из него обновленного студента
                //и вставить его в текущий список
                $.ajax({
                    'url': "/",
                    'async': true,
                    'dataType': 'html',
                    'type': 'get',
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]'
                    ).val(),
                    'success': function (data, status, xhr) {

                        // check if we got successfull response from the server
                        if (status != 'success') {
                            alert(gettext('Student request failed'));
                            return false;
                        }
                    }
                });
                //Обновляем студетна в списке студентов на странице
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

function bookmarksListUpdate(){
    $('.nav-link').click(function (event){
        var link = $(this), url=link.find('.bookmarks-link').attr('href');
        // вызываем обновление контента с помощью аякса
        updateContent(url);
        changeUrl(url);
        return false;
    });
}
function navigationAjax(){
    $('.pag-vs-ajax').click(function (event){
        var obj=$(this), url=obj.attr('href');
        updateContent(url);
        // alert(url)
        return false;
        });
}

function updateContent(url){
    $.ajax({
            'url': url,
            'async': true,
            'dataType': 'html',
            'type': 'get',
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]'
            ).val(),
            'success': function (data, status, xhr){
                new_content = $(data);

                // записываем в кеш браузера полученные данные запроса
                NavigationCache[url] = data;

                // Тут есть проблемма, после нижней строки функция срабатывает через одну вкладку
                // видимо как-то криво вставляется панель навигации аяксом,
                // разобраться позже c $('.col-xs-12').html(new_content.find('#nav-tabs'));
                $('.col-xs-12').html(new_content.find('#nav-tabs'));
                $('#content-colums').html(new_content.find('#content-column'));


                if (status != 'success') {
                        alert(gettext('Student request failed'));
                        return false;
                    }
            }
        });

}

// $(document).on("ajaxSend", function() {
//     $(".progress").show(); // показываем элемент
// }).on("ajaxStop", function(){
//     $(".progress").hide(); // скрываем элемент
// });

// изменяем текущую ссылку страницы на новую, записывая событе в кеш браузера
function changeUrl(url) {
    // window.history.pushState({}, null, url);
    history.pushState(null, null, url);
}

function EventListener(modal) {
    window.addEventListener("popstate", function () {
        modal.modal('hide');
    });
}

$(document).on("ajaxSend", function() {
    $("input").prop('disabled', true);
    $(".student-edit-form-link").prop('disabled', true);

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

// При загрузке сайта, будет создан массив просмотренных страниц.
// При каждом переходе по ajax-ссылке, в этот массив будет записываться код страницы.
var NavigationCache = new Array();
$(document).ready(function(){
  NavigationCache[window.location.pathname] = $('body').html();
  // alert('NavigationCache works');
  history.pushState({page: window.location.pathname, type: "page"}, null, window.location.pathname);
});


// Это событие, будет срабатывать, по нажатию кнопок вперед-назад в браузере,
// все что от него требуется — вставлять в блок содержимое из кэша,
// когда пользователь возвращается на предыдующую страницу.
$(document).ready(function() {
    if (history.pushState) {
        window.onpopstate = function (event) {
            if (event.state.type.length > 0) {
                if (NavigationCache[event.state.page].length>0) {
                    $('body').html(NavigationCache[event.state.page]);

                }
            }
        }
    }
});

// $(document).ready(function() {
//   // $(".clearablefileinput").dropzone({ url: "/file/post" });
//     $(".clearablefileinput").dropzone({ window.Dropzone });
// });

// превью загружаемого фото на форме
function preview() {
    frame.src=URL.createObjectURL(event.target.files[0]);
    $('#frame').show();
}


// добавляем атребут вызова функции превю
function addAtrperview(form) {
    var frame = $('#img_frame > img'), photo_container= $(form.find('#div_id_photo .controls'));
    $(photo_container).append(frame);
    $('.clearablefileinput').html(form.find('.clearablefileinput').attr('onchange','preview()'));
}
$(document).ready(function (){
    initJournal();
    initGroupSelector();
    initDateFilds();
    initEditStudentPage();
    bookmarksListUpdate();
    navigationAjax();
    initLangSelector();

});