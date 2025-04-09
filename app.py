from flask import Flask, render_template, request
from models import db, NHL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nhl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
def seed_data():
    rungtynes = [
        NHL(data="2025-04-09", komanda_1="Colorado Avalanche", komanda_2="Vegas Golden Knights", taškai_1=3, taškai_2=2),
        NHL(data="2025-04-09", komanda_1="Seattle Kraken", komanda_2="Dallas Stars", taškai_1=1, taškai_2=5),
        NHL(data="2025-04-09", komanda_1="Vancouver Canucks", komanda_2="Nashville Predators", taškai_1=3, taškai_2=4),
        NHL(data="2025-04-09", komanda_1="New York Islanders", komanda_2="Buffalo Sabres", taškai_1=6, taškai_2=2),
        NHL(data="2025-04-09", komanda_1="Carolina Hurricanes", komanda_2="Columbus Blue Jackets", taškai_1=0, taškai_2=7),
        NHL(data="2025-04-09", komanda_1="Ottawa Senators", komanda_2="Florida Panthers", taškai_1=2, taškai_2=3),
        NHL(data="2025-04-09", komanda_1="Toronto Maple Leafs", komanda_2="Montreal Canadiens", taškai_1=1, taškai_2=5),
        NHL(data="2025-04-09", komanda_1="Detroit Red Wings", komanda_2="New Jersey Devils", taškai_1=1, taškai_2=5),
        NHL(data="2025-04-09", komanda_1="Boston Bruins", komanda_2="Pittsburgh Penguins", taškai_1=7, taškai_2=5),
        NHL(data="2025-04-08", komanda_1="Chicago Blackhawks", komanda_2="Anaheim Ducks", taškai_1=2, taškai_2=3),
        NHL(data="2025-04-08", komanda_1="Edmonton Oilers", komanda_2="Los Angeles Kings", taškai_1=2, taškai_2=3),
        NHL(data="2025-04-08", komanda_1="Seattle Kraken", komanda_2="San Jose Sharks", taškai_1=2, taškai_2=3),
        NHL(data="2025-04-08", komanda_1="Calgary Flames", komanda_2="Winnipeg Jets", taškai_1=3, taškai_2=2),
        NHL(data="2025-04-08", komanda_1="St. Louis Blues", komanda_2="New York Rangers", taškai_1=3, taškai_2=1),
        NHL(data="2025-04-07", komanda_1="Vancouver Canucks", komanda_2="Vegas Golden Knights", taškai_1=2, taškai_2=4),
        NHL(data="2025-04-07", komanda_1="Nashville Predators", komanda_2="Montreal Canadiens", taškai_1=3, taškai_2=2),
        NHL(data="2025-04-07", komanda_1="Buffalo Sabres", komanda_2="Boston Bruins", taškai_1=6, taškai_2=3),
        NHL(data="2025-04-07", komanda_1="Chicago Blackhawks", komanda_2="Pittsburgh Penguins", taškai_1=2, taškai_2=3),
        NHL(data="2025-04-07", komanda_1="Detroit Red Wings", komanda_2="Florida Panthers", taškai_1=4, taškai_2=5),
        NHL(data="2025-04-07", komanda_1="Ottawa Senators", komanda_2="Columbus Blue Jackets", taškai_1=4, taškai_2=7),
        NHL(data="2025-04-06", komanda_1="Minnesota Wild", komanda_2="Dallas Stars", taškai_1=4, taškai_2=5),
        NHL(data="2025-04-06", komanda_1="New York Islanders", komanda_2="Washington Capitals", taškai_1=2, taškai_2=1),
        NHL(data="2025-04-06", komanda_1="Calgary Flames", komanda_2="Vegas Golden Knights", taškai_1=2, taškai_2=1),
        NHL(data="2025-04-06", komanda_1="San Jose Sharks", komanda_2="Seattle Kraken", taškai_1=5, taškai_2=3),
        NHL(data="2025-04-06", komanda_1="Boston Bruins", komanda_2="Carolina Hurricanes", taškai_1=2, taškai_2=1),
        NHL(data="2025-04-06", komanda_1="Buffalo Sabres", komanda_2="Tampa Bay Lightning", taškai_1=3, taškai_2=2),
        NHL(data="2025-04-06", komanda_1="Montreal Canadiens", komanda_2="Philadelphia Flyers", taškai_1=3, taškai_2=2),
    ]

    db.session.bulk_save_objects(rungtynes)
    db.session.commit()
    seed_data()
    print("Duomenys sėkmingai įkelti!")
with app.app_context():
    db.create_all()
    # seed_data()



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('stats.html')

@app.route('/add')
def add():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)