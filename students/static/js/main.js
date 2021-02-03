function initJournal(){
    var indicator = $('#ajax-progress-indicator');
    var danger = $('#alert-danger');


    $('.day-box input[type="checkbox"]').click(function(event){
        var box = $(this);
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


// function initDateFildsBut(){
//     $('#calendar-button').datetimepicker({ 'format': 'YYYY-MM-DD' });
// }

// $(function initDateFildsBut () {
//              $('#datetimepicker2').datetimepicker();
//          });
//
// function initDateFildsBut(){
//     $('#datetimepicker2').datetimepicker();
//
// }


$(document).ready(function (){
    initJournal();
    initGroupSelector();
    initDateFilds();
    // initDateFildsBut();
});