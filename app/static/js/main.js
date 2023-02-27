//меню личный кабинет
let content = document.getElementById("menu__sub-list");
let show = document.getElementById("showContent");

function submenu__open() {
    const viewport_width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    if(viewport_width > 967){
        content.classList.toggle("show");
    }
}

document.addEventListener("click", (e) => {
    const viewport_width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    if(viewport_width > 967){
        if(!show.contains(e.target)){
            content.classList.remove("show");
        }
    }
});

//меню бургер
const iconMenu = document.querySelector('.menu__icon');
if(iconMenu){
    const menuBody = document.querySelector('.menu__body');
    iconMenu.addEventListener("click", function (e) {
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    })
}

//чекбоксы переключения страниц
$('#site_list').attr('checked', true);
$('#filter_map').attr('checked', false);
$('#sektsii_list').attr('checked', false);

function site() {
    var test = $('#site_list').prop("checked");
    if(test == true) {
        document.getElementById('grid_main_page').hidden = false;
        document.getElementById('map').hidden = true;  
        document.getElementById('sektsii').hidden = true;

        document.getElementById('filter_map').checked = false;    
        document.getElementById('sektsii_list').checked = false; 
    }
};

function map() {
    var test = $('#filter_map').prop("checked");
    if(test == true) {
        document.getElementById('grid_main_page').hidden = true;
        document.getElementById('map').hidden = false;  
        document.getElementById('sektsii').hidden = true;

        document.getElementById('site_list').checked = false;    
        document.getElementById('sektsii_list').checked = false;
        //document.getElementsByClassName('layout-control-group _side_left')[0].classList.add('_hidden')
    }
};

function sektsii() {
    var test = $('#sektsii_list').prop("checked");
    if(test == true) {
        document.getElementById('grid_main_page').hidden = true;
        document.getElementById('sektsii').hidden = false;
        document.getElementById('map').hidden = true;  

        document.getElementById('filter_map').checked = false;    
        document.getElementById('site_list').checked = false; 
    }
};


//меню описания новостей
let news = document.getElementById("hidden_div");
let publish_textbox = document.getElementById("main-block__body-publish_textbox");
let news_theme = document.getElementById("news_theme");
let news_description = document.getElementById("news_description");

function news_description__open() {
    news.classList.toggle("show");
}

setInterval(function() {
    let url = window.location.href;
    var param = decodeURIComponent(url.split("/")[4]);

    if (param == "Футбол") {
        var ids1 = ["1", "2", "6", "9", "10", "11", "12", "13", "14"];
        request = $.ajax({
            url: "http://127.0.0.1:8000/maps/Футбол/",
            dataType: "html",
            success: function(html){
                ids1.forEach(id => $("#chat-content" + id).html($($.parseHTML(html)).find("#chat-content" + id).html()));
            }
        });
    } else if (param == "Баскетбол") {
        var ids2 = ["7", "8"];
        request = $.ajax({
            url: "http://127.0.0.1:8000/maps/Баскетбол/",
            dataType: "html",
            success: function(html){
                ids2.forEach(id => $("#chat-content" + id).html($($.parseHTML(html)).find("#chat-content" + id).html()));
            }
        });
    } else if (param == "Волейбол") {
        var ids3 = ["15", "16"];
        request = $.ajax({
            url: "http://127.0.0.1:8000/maps/Волейбол/",
            dataType: "html",
            success: function(html){
                ids3.forEach(id => $("#chat-content" + id).html($($.parseHTML(html)).find("#chat-content" + id).html()));
            }
        });
    } else {
        console.log("");
    }

}, 1000);

var request;

$(".info_chats").submit(function(event){
    event.preventDefault();

    if (request) {
        request.abort();
    }
    var $form = $(this);

    var id_for_url = $form.attr('id').slice(-2).replace(/[a-zA-Z]/g, '');
    var prepared_url = id_for_url + "/add_message/";

    var $inputs = $form.find("input, select, button, textarea");

    var serializedData = $form.serialize();

    $inputs.prop("disabled", true);

    request = $.ajax({
        url: prepared_url,
        type: "post",
        data: serializedData
    });

    request.always(function () {
        $inputs.prop("disabled", false);
    });
});

document.addEventListener("click", (e) => {
        if(!publish_textbox.contains(e.target) && !news_theme.contains(e.target) && !news_description.contains(e.target)){
            news.classList.remove("show");
        }
});


function send_message(clicked_id) {
    let group_id = clicked_id.slice(-2).replace(/[a-zA-Z]/g, '');
    let chat = document.getElementById("grid__item grid_item-chat"+group_id);
    let item = document.getElementById("grid__item"+group_id);

    chat.classList.remove("show");
    item.classList.remove("hide");
}

//переход в чат

function chat_open0(clicked_id) {
    let group_id = clicked_id.slice(-2).replace(/[a-zA-Z]/g, '');
    let chat = document.getElementById("grid__item grid_item-chat"+group_id);
    let item = document.getElementById("grid__item"+group_id);

    chat.classList.toggle("show");
    item.classList.toggle("hide");
}
function chat_close0(clicked_id) {
    let group_id = clicked_id.slice(-2).replace(/[a-zA-Z]/g, '');
    let chat = document.getElementById("grid__item grid_item-chat"+group_id);
    let item = document.getElementById("grid__item"+group_id);

    chat.classList.remove("show");
    item.classList.remove("hide");
}


//переход в подробнее
function menu_more__open0(clicked_id) {
    let group_id = clicked_id.slice(-2).replace(/[a-zA-Z]/g, '');
    console.log(clicked_id.slice(-2).replace(/[a-zA-Z]/g, ''));
    let menu_more0 = document.getElementById("menu__more"+group_id);
    let button_more0 = document.getElementById("button-more"+group_id);

    menu_more0.classList.toggle("show");
}

document.addEventListener("click", (e) => {
        if(!button_more0.contains(e.target)){
            menu_more0.classList.remove("show");
        }
});
