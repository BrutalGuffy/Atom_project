/**
 * Created by artur on 30.03.18.
 */

const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    timezone: 'UTC',
    hour: 'numeric',
    minute: 'numeric',
};

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
                    $("#comslist").append(`
                    <div class="card mb-2">
                        <div class="card-header p-3">
                            <div class="row mb-3">
                                <div class="col-6">
                                    <strong class="text-muted" id="comslist">`+coms[i].created_by__username+`</strong>
                                </div>
                                <div class="col-6 text-right">
                                    <small class="text-muted">`+new Date(coms[i].created_at).toLocaleString("ru", options).replace(',', '')+`</small>
                                </div>
                            </div>
                        </div>
                        <div class="card-body p-3">
                            <div class="row">
                                <div class="col-12">
                                    <strong id="comslist">`+coms[i].comment+`</strong>
                                </div>                               
                            </div>
                        </div>
                            <div class="card-footer">
                            <div class="row mb-3">
                                <div class="col-2">
                                    <button class="btn btn-light like like_com__icon d-flex justify-content-start" id="{{ event.id }}" style="fill: #ff0000; color: #0000cc">
                                        <svg version="1.1" width="25%" height="25%" x="0px" y="0px"viewBox="0 0 50 50" style="enable-background:new 0 0 50 50;" xml:space="preserve" class="d-flex align-self-center">
                                            <path d="M24.85,10.126c2.018-4.783,6.628-8.125,11.99-8.125c7.223,0,12.425,6.179,13.079,13.543
                                            c0,0,0.353,1.828-0.424,5.119c-1.058,4.482-3.545,8.464-6.898,11.503L24.85,48L7.402,32.165c-3.353-3.038-5.84-7.021-6.898-11.503
                                            c-0.777-3.291-0.424-5.119-0.424-5.119C0.734,8.179,5.936,2,13.159,2C18.522,2,22.832,5.343,24.85,10.126z"/>
                                        </svg>
                                        <span>
                                            &ensp;
                                        </span>
                                        <span class="like__count d-flex align-self-center">`+"Likes "+coms[i].like_count+`</span>
                                    </button>
                                </div>                               
                            </div>
                            </div>
                        </div>
                    </div>`);
                }
            }
        });
    });
});