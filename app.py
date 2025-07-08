from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''
    Toronto, July 18, Acqua Supper Club, friday,19+
    July 25 - New York , Lou Lou Club, friday, 21+
    July 26 - Los Angeles ,Kookaburra Club, saturday, 18+
    '''
    events = [
        {
            'city': 'Toronto',
            'date': 'July 18',
            'day': 'Friday',
            'time': '',
            'club': 'Acqua Supper Club',
            'url': 'https://whitenightstour.eventbrite.ca'
        },
        {
            'city': 'New York',
            'date': 'July 25',
            'day': 'Friday',
            'time': '',
            'club': 'Lou Lou Club',
            'url': 'https://bazzarny.eventbrite.ca'
        },
        {
            'city': 'Los Angeles',
            'date': 'July 26',
            'day': 'Saturday',
            'time': '',
            'club': 'Kookaburra Club',
            'url': 'https://bazzarla.eventbrite.ca'
        }
    ]
    return render_template('index.html', events=events)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
