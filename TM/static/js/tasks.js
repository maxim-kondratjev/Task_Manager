document.body.onload = function() {
    var page = 2;
    var pages = true;
    window.onscroll = function() {
        var scrollTop = (window.pageYOffset || document.documentElement.scrollTop) + document.documentElement.clientHeight;
        var scrollHeight = Math.max(
          document.body.scrollHeight, document.documentElement.scrollHeight,
          document.body.offsetHeight, document.documentElement.offsetHeight,
          document.body.clientHeight, document.documentElement.clientHeight
        );

        if ((scrollHeight - scrollTop < 10) && pages){
            pages = false;
            $.ajax({
                type: 'GET',
                url: 'page/?page=' + page.toString(),

                success: (result) => {
                    $('#tasks').append(result);
                    page = page + 1;
                    pages = true;
                },

                error: (result) => {
                    pages = false;
                }
            });
        }
    }
};
