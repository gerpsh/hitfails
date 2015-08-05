readUrl = (input, num) ->
	if input.files and input.files[0]
		reader = new FileReader()
		reader.onload = (e) ->
			$("#picture-#{num}-preview").attr("src", e.target.result)

		reader.readDataAsURL(input.files[0])

$("#id_picture1").change(() ->
	readUrl(this, "1"))

$("#id_picture2").change(() ->
	readUrl(this, "2"))

$("#id_picture3").change(() ->
	readUrl(this, "3"))
