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
                for (i=0; i<coms.length; i++) {
                    $("#comslist").append(`<div class="card mb-2">
                        <div class="card-body p-3">
                            <div class="row mb-3">
                                <div class="col-6">
                                    <strong class="text-muted" id="comslist">`+coms[i].created_by__username+`</strong>
                                </div>
                                <div class="col-6 text-right">
                                    <small class="text-muted">`+coms[i].created_at+`</small>
                                </div>
                            </div> `+coms[i].comment+`
                        </div>
                    </div>`);
                }
            }
        });
    });
});