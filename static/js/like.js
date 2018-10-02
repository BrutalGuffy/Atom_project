/**
 * Created by artur on 03.04.18.
 */

function addLike(img_id, count_id) {
    $.ajax({
      url: "/add_like/",
      type: "GET",
        data: {
          'event_id': img_id
        },
      dataType: 'json',
      cache: false,
      success: function(data){
        document.getElementById(count_id).textContent = `Likes `+data.new_total_likes;
        var isLiked = $('.like__icon').css("fill");
        if (isLiked === 'rgb(255, 0, 0)') {
            $('.like__icon').css({fill: '#ffb8b8'});
        }
        else {
            $('.like__icon').css({fill: '#ff0000'});
        }
      }
    });
}

$('.like__icon').click(function () {
    const id = $(this).attr('id');
    const count_id = 'count ' + id;
    addLike(id, count_id);
});