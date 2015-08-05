usernamePasses = (username) ->
	usernameRegex = /^[a-zA-Z0-9_]{3,16}$/
	return username.match usernameRegex

passwordPasses = (password) ->
	passwordRegex = /^[0-9a-zA-Z!@#\$\-_]{7,}$/
	return password.match passwordRegex

passwordsMatch = (p1, p2) ->
	return (p1 is p2) and (p1 isnt '')

usernameAvailable = (username) ->
	checkUrl = "site-auth/username-check/#{username}/"
	$.get checkUrl, (data) -> 
		if data is 'fail'
			return true
		else
			return false

###
prevents user from submitting unless all conditions are met:
password meets format, passwords match, username meets format, and username not already taken
###
$('#password').keyup ->
	un = $('#username').val()
	p1 = $('#password').val()
	p2 = $('#password-again').val()

	if passwordPasses(p1)
		$('#password').css('background-color', '#00FF80')
		checkUrl = "site-auth/username-check/#{un}/"
		$.get checkUrl, (data) ->
			if data is 'fail'
				$('#username-taken').show()
				$('#submit-form').prop('disabled', true)
			else
				$('#username-taken').hide();
				if passwordsMatch(p1,p2) and usernamePasses(un) and passwordPasses(p1)
					$('#submit-form').prop('disabled', false)
				else
					$('#submit-form').prop('disabled', true)
	else
		$('#password').css('background-color', '#FA5858');
		$('#submit-form').prop('disabled', true);

$('#password-again').keyup ->
	un = $('#username').val()
	p1 = $('#password').val()
	p2 = $('#password-again').val()

	if passwordsMatch(p1,p2)
		$('#password-again').css('background-color', '#00FF80')
		checkUrl = "site-auth/username-check/#{un}/"
		$.get checkUrl, (data) ->
			if data is 'fail'
				$('#username-taken').show()
				$('#submit-form').prop('disabled', true)
			else
				$('#username-taken').hide();
				if passwordsMatch(p1,p2) and usernamePasses(un) and passwordPasses(p1)
					$('#submit-form').prop('disabled', false)
				else
					$('#submit-form').prop('disabled', true)
	else
		$('#password-again').css('background-color', '#FA5858');
		$('#submit-form').prop('disabled', true);


$('#username').keyup ->
	un = $('#username').val()
	p1 = $('#password').val()
	p2 = $('#password-again').val()

	if usernamePasses(un)
		$('#username').css('background-color', '#00FF80')
		checkUrl = "site-auth/username-check/#{un}/"
		$.get checkUrl, (data) ->
			if data is 'fail'
				$('#username-taken').show()
				$('#submit-form').prop('disabled', true)
			else
				$('#username-taken').hide();
				if passwordsMatch(p1,p2) and usernamePasses(un) and passwordPasses(p1)
					$('#submit-form').prop('disabled', false)
				else
					$('#submit-form').prop('disabled', true)
	else
		$('#username').css('background-color', '#FA5858');
		$('#submit-form').prop('disabled', true);



