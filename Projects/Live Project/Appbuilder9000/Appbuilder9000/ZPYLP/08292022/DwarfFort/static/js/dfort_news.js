

/* News Page*/
var latest_news = document.getElementById("latest-news");
var mid_news = document.getElementById("mid-news");
var last_news = document.getElementById("last-news");

/* Page 1 Next */
if (document.getElementById("news-btn1") !== null) {
    var news_btn1 = document.getElementById("news-btn1");
    news_btn1.onclick = function() {
        latest_news.style.display = "none";
        mid_news.style.display = "block";
    }
}

/* Page 2 Prev */
if (document.getElementById("news-btn2") !== null) {
    var news_btn2 = document.getElementById("news-btn2");
    news_btn2.onclick = function() {
        latest_news.style.display = "block";
        mid_news.style.display = "none";
    }
}

/* Page 2 Next */
if (document.getElementById("news-btn3") !== null) {
    var news_btn3 = document.getElementById("news-btn3");
    news_btn3.onclick = function() {
        mid_news.style.display = "none";
        last_news.style.display = "block";
    }
}

/* Page 3 Prev */
if (document.getElementById("news-btn4") !== null) {
    var news_btn4 = document.getElementById("news-btn4");
    news_btn4.onclick = function() {
        mid_news.style.display = "block";
        last_news.style.display = "none";
    }
}