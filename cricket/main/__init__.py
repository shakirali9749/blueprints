from flask import Blueprint, render_template

main = Blueprint('main',__name__,template_folder='mainTemplates')
@main.route('/')
def index():
	return render_template('index.html')