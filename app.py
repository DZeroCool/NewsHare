from flask import Flask, render_template, request, make_response
from jinja2 import Markup, PackageLoader, Environment

app = Flask(__name__)
app.config.from_pyfile('config.py')

loader = PackageLoader(__name__, '')
env = Environment(loader=loader)
def include_file(name):
	if ".." in name:
		return "please dont try to hack me"
	return Markup(loader.get_source(env, "includes/" + name)[0])
env.globals['include_file'] = include_file

@app.route('/')
@app.route('/index.html')
def home():
	return env.get_template('templates/home.html').render(url=request.url, development_version="quadric", categories=[x.replace("_", " ") for x in "Technology Business USA_politics Asia Europe University Health Law Food Travel Music Entertainment Crypto Space Climate World_Affairs xkcd".split()], catfiles=[x for x in request.args.get('files', default='').split(',') if x])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True, use_reloader=True)
else:
	application = app

# hopefully this works
