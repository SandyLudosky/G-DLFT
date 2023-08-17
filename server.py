import json
from datetime import datetime
from flask import Flask, render_template, request, \
    redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():

    club = [club for club in clubs if club['email'] ==
            request.form['email']]

    if club:
        return render_template('welcome.html', club=club[0],
                               competitions=competitions)
    elif request.form['email'] == '':
        flash("Please enter your email.")
        return render_template('index.html'), 401
    else:
        flash("No account related to this email.")
        return render_template('index.html'), 401

    # except IndexError:
    #     if request.form['email'] == '':
    #         flash("Please enter your email.", 'error')
    #     else:
    #         flash("No account related to this email.", 'error')
    #     return render_template('index.html'), 401


@app.route('/book/<competition>/<club>')
def book(competition, club):
    club = [c for c in clubs if c['name'] == club][0]

    try:
        competition = [c for c in competitions if c['name'] == competition][0]

        if datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            flash("This competition is over.", 'error')
            status_code = 400

        else:
            return render_template('booking.html', club=club,
                                   competition=competition)

    except IndexError:
        flash("Something went wrong-please try again", 'error')
        status_code = 404

    return render_template(
        'welcome.html',
        club=club,
        competitions=competitions,
    ), status_code


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] ==
                   request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]

    try:
        places_required = int(request.form['places'])

        if places_required > int(competition['numberOfPlaces']):
            flash('Not enough places available.', 'error'), 400

        elif places_required * 3 > int(club['points']):
            flash("You don't have enough points.", 'error')

        elif places_required > 12:
            flash("You cannot book more than 12 places in a competition.", 'error'), 400
        else:
            try:
                competition['numberOfPlaces'] = \
                int(competition['numberOfPlaces']) - places_required
                club['points'] = int(club['points']) - (places_required * 3)
                flash('Great-booking complete!', 'success')

                return render_template(
                    'welcome.html',
                    club=club,
                    competitions=competitions
                )

            except ValueError as error_message:
                flash(error_message, 'error')

    except ValueError:
        flash('Please enter a number between 0 and 12.', 'error')

    return render_template('booking.html', club=club, competition=competition), 400





# TODO: Add route for points display
@app.route('/displayPoints')
def displayPoints():
    return render_template('dashboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


app.config['DEBUG'] = True
app.config['TESTING'] = True