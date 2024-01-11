from flask import render_template, Blueprint

batsman = Blueprint('batsman',__name__,template_folder='templates')
@batsman.route('/batsman')
def bats():
	return render_template('batsman.html')

