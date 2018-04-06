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
        document.getElementById(count_id).textContent = data.new_total_likes;
      }
    });
}

$('.like__icon').click(function () {
    const id = $(this).attr('id');
    const count_id = 'count ' + id;
    addLike(id, count_id);
});