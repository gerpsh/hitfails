$('#parent-comment-form').on('submit', () ->
	form = $(this)
	$.post(form.attr('action'), form.serialize())
	.done((data) ->
		alert "comment posted!"		
	)
	.fail((xhr, status, error) ->
	)
)