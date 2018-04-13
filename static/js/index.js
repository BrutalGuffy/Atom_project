/**
 * Created by artur on 30.03.18.
 */

var page = 1;
$(document).ready(function () {
    $('.more').click(function () {
        $.ajax({

            type: "GET",

            url: "more_comments/",

            data: {
                'page': page
            },

            cache: false,

            success: function (data) {
                page++;
                console.log(data);
                console.log(page);
                var coms = data.comments;
                coms.toString();
                console.log(coms[2].comment);
                console.log(coms.length);
                var list = "";
                for (i=0; i<coms.length; i++) {
                    list +="<li>"+coms[i].comment+"</li>";
                    list +="<li>"+coms[i].created_at+"</li>";
                }
                $("#comslist").append(list);
                console.log(list)
            }
        });
    });
});