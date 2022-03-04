from crypt import methods
from flask import Flask, render_template, request, url_for
from connexion import Connexion

app = Flask(__name__)

@app.route('/')
def index():
    ligne = Connexion.lister_lignes()
    return render_template('index.html', a_afficher = ligne)

@app.route('/client', methods = ['POST', 'GET'])
def client():
    lignes = Connexion.lister_lignes()
    return render_template('client.html', lignes=lignes)

@app.route('/arret/<int:id_lignes>')
def afficher_arrets(id_ligne):
    arrets= Connexion.lister_arrets(id_ligne)
    return render_template("arrets.html", a_afficher=arrets)

@app.route('/identification')
def identifier():
    
    return render_template("form_identifier.html")


@app.route('/autorisation', methods=['POST'])
def autoriser():
    pseudo_saisie = request.values.get("pseudo")
    mdp_saisie = request.values.get("mdp")
    oui = Connexion.identifier(pseudo_saisie, mdp_saisie)

    return render_template("identifier.html", qui = pseudo_saisie, reponse = oui)

@app.route('/autorisation/ajouter', methods = ['GET', 'POST'])
def ajouter_bus():
    id_lignes_input = Connexion.select_lignes()

    if request.method == 'POST':
        immatriculation = request.values.get('immatriculation')
        numero = request.values.get('numero')
        nombre_places = request.values.get('nombre_places')
        id_ligne = request.values.get('id_lignes')

        print(immatriculation, numero, nombre_places, id_ligne)
        Connexion.ajouter_bus(numero,immatriculation, nombre_places, id_ligne)
    return render_template("ajout_bus.html", id_lignes=id_lignes_input)


@app.route('/autorisation/modifier', methods = ['GET', 'POST'])
def modifier_bus():
    id_bus_input = Connexion.select_id_bus()
    id_lignes_input = Connexion.select_lignes()

    if request.method == 'POST':
        immatriculation = request.values.get('immatriculation')
        numero = request.values.get('numero')
        nombre_places = request.values.get('nombre_places')
        id_ligne = request.values.get('id_lignes')
        id_bus = request.values.get('id_bus')

        print(immatriculation, numero, nombre_places, id_ligne, id_bus)
        Connexion.modifier_bus(id_bus, numero, immatriculation, nombre_places, id_ligne)

    return render_template("modifier_bus.html", id_bus=id_bus_input, id_lignes=id_lignes_input)

@app.route('/autorisation/supprimer', methods = ['GET', 'POST'])
def supprimer_bus():

    if request.method == 'POST':
        id_bus = request.values.get('id_bus')
        Connexion.supprimer_bus(id_bus)

    id_bus_input = Connexion.select_id_bus()
    return render_template("supprimer_bus.html", id_bus=id_bus_input)


@app.route ('/form_identifier')
def formuler():
    return render_template("form_identifier.html")



    
if __name__ == "__main__":
    app.run(debug=True)