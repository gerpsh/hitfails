$(function() {

  mark = function(postId, el) {
    $.post( "/posts/add-mark/" + postId + "/", function(data) {
      if(data.status == 1) {
        $(el).removeClass("unmarked");
        $(el).addClass("marked");
        var currentMarks = "Upvoted | " + data.marks + " upvotes";
        $(el).attr("onclick", "unmark(" + postId.toString() + ", this)");
        $(el).html(currentMarks);
      } else {
        window.location = "/site-auth/login/";
      }
    });
  }

  unmark = function(postId, el) {
    $.post( "/posts/remove-mark/" + postId + "/", function(data) {
      if(data.status == 1) {
        $(el).removeClass("marked");
        $(el).addClass("unmarked");
        $(el).attr("onclick", "mark(" + postId.toString() + ", this)");
        var currentMarks = "Upvote | " + data.marks + " upvotes";
        $(el).html(currentMarks);
      } else {
        window.location = "/site-auth/login/";
      }
    });
  }

});
