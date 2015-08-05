// Generated by CoffeeScript 1.9.3
(function() {
  var passwordPasses, passwordsMatch, usernameAvailable, usernamePasses;

  usernamePasses = function(username) {
    var usernameRegex;
    usernameRegex = /^[a-zA-Z0-9_]{3,16}$/;
    return username.match(usernameRegex);
  };

  passwordPasses = function(password) {
    var passwordRegex;
    passwordRegex = /^[0-9a-zA-Z!@#\$\-_]{7,}$/;
    return password.match(passwordRegex);
  };

  passwordsMatch = function(p1, p2) {
    return (p1 === p2) && (p1 !== '');
  };

  usernameAvailable = function(username) {
    var checkUrl;
    checkUrl = "site-auth/username-check/" + username + "/";
    return $.get(checkUrl, function(data) {
      if (data === 'fail') {
        return true;
      } else {
        return false;
      }
    });
  };


  /*
  prevents user from submitting unless all conditions are met:
  password meets format, passwords match, username meets format, and username not already taken
   */

  $('#password').keyup(function() {
    var checkUrl, p1, p2, un;
    un = $('#username').val();
    p1 = $('#password').val();
    p2 = $('#password-again').val();
    if (passwordPasses(p1)) {
      $('#password').css('background-color', '#00FF80');
      checkUrl = "site-auth/username-check/" + un + "/";
      return $.get(checkUrl, function(data) {
        if (data === 'fail') {
          $('#username-taken').show();
          return $('#submit-form').prop('disabled', true);
        } else {
          $('#username-taken').hide();
          if (passwordsMatch(p1, p2) && usernamePasses(un) && passwordPasses(p1)) {
            return $('#submit-form').prop('disabled', false);
          } else {
            return $('#submit-form').prop('disabled', true);
          }
        }
      });
    } else {
      $('#password').css('background-color', '#FA5858');
      return $('#submit-form').prop('disabled', true);
    }
  });

  $('#password-again').keyup(function() {
    var checkUrl, p1, p2, un;
    un = $('#username').val();
    p1 = $('#password').val();
    p2 = $('#password-again').val();
    if (passwordsMatch(p1, p2)) {
      $('#password-again').css('background-color', '#00FF80');
      checkUrl = "site-auth/username-check/" + un + "/";
      return $.get(checkUrl, function(data) {
        if (data === 'fail') {
          $('#username-taken').show();
          return $('#submit-form').prop('disabled', true);
        } else {
          $('#username-taken').hide();
          if (passwordsMatch(p1, p2) && usernamePasses(un) && passwordPasses(p1)) {
            return $('#submit-form').prop('disabled', false);
          } else {
            return $('#submit-form').prop('disabled', true);
          }
        }
      });
    } else {
      $('#password-again').css('background-color', '#FA5858');
      return $('#submit-form').prop('disabled', true);
    }
  });

  $('#username').keyup(function() {
    var checkUrl, p1, p2, un;
    un = $('#username').val();
    p1 = $('#password').val();
    p2 = $('#password-again').val();
    if (usernamePasses(un)) {
      $('#username').css('background-color', '#00FF80');
      checkUrl = "site-auth/username-check/" + un + "/";
      return $.get(checkUrl, function(data) {
        if (data === 'fail') {
          $('#username-taken').show();
          return $('#submit-form').prop('disabled', true);
        } else {
          $('#username-taken').hide();
          if (passwordsMatch(p1, p2) && usernamePasses(un) && passwordPasses(p1)) {
            return $('#submit-form').prop('disabled', false);
          } else {
            return $('#submit-form').prop('disabled', true);
          }
        }
      });
    } else {
      $('#username').css('background-color', '#FA5858');
      return $('#submit-form').prop('disabled', true);
    }
  });

}).call(this);
