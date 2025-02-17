from flask import Blueprint, render_template

selection_route = Blueprint('selection', __name__)

@selection_route.route('/')
def selection(): return render_template('selection.html')