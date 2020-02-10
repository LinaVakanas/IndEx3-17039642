from flask import render_template, Blueprint, url_for, flash, redirect, request

from app.main.forms import SignupForm, CityBlogSearchForm

bp_main = Blueprint('main', __name__)

#
# @bp_main.route('/')
# def home():
#     search = CityBlogSearchForm(request.form)
#     return render_template('index.html', title='Home', search=search)


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    search = CityBlogSearchForm(request.form)
    if form.validate_on_submit():
        flash('Exciting, you have successfully signed up!')
        return redirect(url_for('main.home',  title='Home', search=search))
    else:
        return render_template('signup.html', form=form, title="Signup")


@bp_main.route('/', methods=['GET', 'POST'])
def home():
    search = CityBlogSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    else:
        return render_template('index.html', search=search, title="Home")
#
#
@bp_main.route('/results/')
def search_results(search):
    results = []
    search_string = search.data['search']
    select_string = search.data['select']
    if search_string == '':
        pass
    if not results:
        if select_string == 'City':
            flash('Hm... looks like we have nothing on {searched}!'.format(searched=search_string.capitalize()))
            return redirect('/')
        else:
            flash("Hm... we don't know '{searched}', looks like you made up that blog!".format(searched=search_string))
            return redirect('/')
    else:
        pass

