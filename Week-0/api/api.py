import flask
from flask import request, jsonify

# create the flask application objecet, which contains data about the 
# the applicaiton and also methods (object functions) that tell the application to do certain actions.
app = flask.Flask(__name__)
# start the debugger. with, this line, if your code is malformed, you'll see an error when you visit your app.
app.config["DEBUG"] = True

# create some test data for our caralog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
	# jsonify converts a python dictionary into a JSON file
	return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
	# check if an ID was provided as part of the URL.
	# if ID is provided, assign it to a variable.
	# if no ID is provided, display an error in the browser.
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided. Please specify an id."

	# create an empty list for our results
	results = []

	# Loop through the data and match results that fit the requested ID.
	# IDs are unique, but other fields might return many results
	for book in books:
		if book['id'] == id:
			results.append(book)

	return jsonify(results)

app.run()