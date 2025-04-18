from flask import Flask, render_template, request, redirect, flash
from models import db, NHL




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nhl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "labai_saugus_ir_unikalus_raktas_12345"

db.init_app(app)


def seed_data():
    if NHL.query.first():  # Tikrinama, ar lentelėje yra įrašų
        print("Duomenys jau egzistuoja. Naujų įrašų neįterpiama.")
        return

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
    print("Duomenys sėkmingai įkelti!")


with app.app_context():
    db.create_all()

    seed_data()


@app.route('/')
@app.route('/page/<int:page>')
def home(page=1):
    per_page = 10

    pagination = NHL.query.paginate(page=page, per_page=per_page)
    return render_template('index.html', pagination=pagination)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        rezultatai = NHL.query.filter(
            (NHL.komanda_1.ilike(f"%{query}%")) |
            (NHL.komanda_2.ilike(f"%{query}%")) |
            (NHL.data.ilike(f"%{query}%"))
        ).all()
        return render_template('search.html', rezultatai=rezultatai, query=query)
    else:
        return render_template('search.html', rezultatai=[], query=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    rungtynes = NHL.query.get_or_404(id)
    if request.method == 'POST':
        rungtynes.data = request.form['data']
        rungtynes.komanda_1 = request.form['komanda_1']
        rungtynes.taškai_1 = request.form['taškai_1']
        rungtynes.komanda_2 = request.form['komanda_2']
        rungtynes.taškai_2 = request.form['taškai_2']
        db.session.commit()
        flash("Rungtynių duomenys sėkmingai atnaujinti!", "success")
        return redirect('/')
    return render_template('edit.html', rungtynes=rungtynes)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    rungtynes = NHL.query.get_or_404(id)
    db.session.delete(rungtynes)
    db.session.commit()
    flash("Rungtynės sėkmingai ištrintos!", "success")
    return redirect('/')

@app.route('/stats')
def stats():
    statistika_query = db.session.query(
        NHL.komanda_1.label('komanda'),
        db.func.count(NHL.taškai_1 > NHL.taškai_2).label('laimėjimų_skaičius'),
        db.func.sum(NHL.taškai_1).label('pelnyti_taškai')
    ).group_by(NHL.komanda_1).order_by(
        db.desc('laimėjimų_skaičius'),
        db.desc('pelnyti_taškai'),
        NHL.komanda_1
    ).all()

    statistika = []
    for index, komanda in enumerate(statistika_query, start=1):
        statistika.append({
            "pozicija": index,
            "komanda": komanda[0],
            "laimėjimų_skaičius": komanda[1],
            "pelnyti_taškai": komanda[2]
        })

    return render_template('stats.html', statistika=statistika)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        rungtynes = NHL(
            data=request.form['data'],
            komanda_1=request.form['komanda_1'],
            taškai_1=request.form['taškai_1'],
            komanda_2=request.form['komanda_2'],
            taškai_2=request.form['taškai_2']
        )
        db.session.add(rungtynes)
        db.session.commit()
        flash("Rungtynės sėkmingai pridėtos!", "success")
        return redirect('/')
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)