$(function() {

  /*
    Since Django relies on a csrf token to verify form submissions,
    we need to fake it here.  This grabs the token from the cookie store.
  */
  // This function gets cookie with a given name
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  /*
    The functions below will create a header with csrftoken
  */

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  function sameOrigin(url) {
      // test that a given url is a same-origin URL
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
          (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
          // or any other URL that isn't scheme relative or absolute i.e relative.
          !(/^(\/\/|http:|https:).*/.test(url));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
              // Send the token to same-origin, relative URLs only.
              // Send the token only if the method warrants CSRF protection
              // Using the CSRFToken value acquired earlier
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  $('#parent-comment-form').submit(function(event) {
      event.preventDefault();
      create_parent_post();
      return false; //prevent default sychronous submit
  });

  function create_parent_post() {
      var postId = $(location).attr('href').split("/")[4];
      var bodyText = $('#add-parent-body').val()
      $("#no-comments-yet").remove();
      $.ajax({
          url : "/posts/add-comment/" + postId + "/",
          type : "POST",
          data : { body : bodyText },
          success : function(json) {
            if(bodyText != ''){
              $("#empty-comment-warning").hide(50, function() {});
              $('#add-parent-body').val(''); //clear input box
              var comment = "<div class='row latest-parent-comment'><div class='col-md-8 parent-comment-container'><p class='parent-comment-header'><span class='parent-comment-time'><strong>" + json.time + "</strong></span></p><p class='parent-comment-body'>" + json.body + "</p><p></p></div></div><br>";
              $(comment).prependTo("#comments-container");
              $(".latest-parent-comment").show(500, function() {});
            } else {
              $("#empty-comment-warning").show(50, function() {});
            }
          },
          // handle a non-successful response
          error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText);
          }
      });
  };

});
