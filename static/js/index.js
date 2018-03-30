/**
 * Created by artur on 30.03.18.
 */

const like = document.querySelector('.like__icon');
const likeCount = document.querySelector('.like__count')

console.log(like);

like.onclick = addLike;

function addLike() {
    $.ajax({
      url: "add_like/",
      type: "GET",
      data: {"like": "1"},
      cache: false,
      success: function(data){
        console.log(data);
        likeCount.textContent = data.new_total_likes;
      }
    });
}
