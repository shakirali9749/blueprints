from flask import Blueprint, render_template

bowler = Blueprint('bowler',__name__,template_folder='newbowler')
@bowler.route('/bowler')
def boll():
	return render_template('bowler.html')

