
import mysql.connector as mysqlpy

class Connexion:
    __USER = 'root'
    __PWD = 'root'
    __HOST = 'localhost'
    __PORT = '8081'
    __DB = 'breizhibus2'
    __cursor = False

    @classmethod
    def ouvrir_connexion(cls) :
           if cls.__cursor == None :
                cls.__bdd = mysqlpy.connect(user = cls.__USER, password = cls.__PWD, host = cls.__HOST, port = cls.__PORT, database = cls.__DB)
                cls.__cursor = cls.__bdd.cursor()
    
    @classmethod
    def select_lignes(cls):
        cls.ouvrir_connexion()
        requete = "SELECT id_ligne FROM lignes"
        cls.__cursor.execute(requete)
        result = cls.__cursor.fetchall()

        cls.fermer_connexion()
        return result
    
    @classmethod
    def select_id_bus(cls):
        cls.ouvrir_connexion()
        requete = "SELECT id_bus FROM bus"
        cls.__cursor.execute(requete)
        result = cls.__cursor.fetchall()

        cls.fermer_connexion()
        return result

    @classmethod
    def lister_lignes(cls):
        cls.ouvrir_connexion()

        requete = "SELECT l.nom, a.nom, a.adresse  \
                FROM lignes l\
                JOIN arrets_lignes al ON al.id_ligne = l.id_ligne\
                JOIN arrets a ON al.id_arret = a.id_arret;"
        cls.__cursor.execute(requete)
        result = cls.__cursor.fetchall()
        cls.fermer_connexion()
        return result
            
    

    # méthode pour trouver tous les arréts d'une ligne précise
    @classmethod
    def lister_arrets(cls, id_ligne):
        cls.ouvrir_connexion()

        requete = "SELECT a.id_arret, a.nom, a.adresse, l.nom \
                FROM lignes l \
                JOIN arrets_lignes al ON al.id_ligne = l.id_ligne \
                JOIN arrets a ON al.id_arret = a.id_arret \
                WHERE l.id_ligne = %s "
        param = (id_ligne, )
        cls.__cursor.execute(requete, param)
        result = cls.__cursor.fetchall()
        cls.fermer_connexion()
        return result


    @classmethod
    def identifier(cls, pseudo_saisie, mdp_saisie):
        
        ok = False
        cls.ouvrir_connexion()
        requete = "SELECT pseudo, mdp FROM utilisateurs WHERE pseudo = %s AND mdp = %s"
        vals = (pseudo_saisie, mdp_saisie)
        cls.__cursor.execute(requete, vals)

        if cls.__cursor.fetchone() != None:
            ok = True

        cls.fermer_connexion()

        return ok
        
    @classmethod
    def ajouter_bus(cls, numero_saisie, immatriculation_bus, places_saisie, ligne_saisie):
        
        cls.ouvrir_connexion()

        requete = "INSERT INTO bus (numero, immatriculation, nombre_place, id_ligne) VALUES (%s, %s, %s, %s)"
        param = (numero_saisie, immatriculation_bus, places_saisie, ligne_saisie, )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

        cls.fermer_connexion()
        pass

    @classmethod
    def modifier_bus(cls, id_bus_a_modifier, numero_saisie, immatriculation_bus, places_saisie, ligne_saisie):
        cls.ouvrir_connexion()

        requete = "UPDATE bus SET numero = %s, immatriculation = %s, nombre_place = %s, id_ligne = %s WHERE id_bus = %s"
        param = (numero_saisie, immatriculation_bus, places_saisie, ligne_saisie, id_bus_a_modifier, )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

        cls.fermer_connexion()

    @classmethod
    def supprimer_bus(cls,id_bus_byebye):
        cls.ouvrir_connexion()

        requete = "DELETE FROM bus WHERE id_bus = %s"
        param = (id_bus_byebye, )
        cls.__cursor.execute(requete, param)
        cls.__bdd.commit()

        cls.fermer_connexion()


        


    @classmethod
    def fermer_connexion(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None



# print('test identification')
# print(Connexion.identifier('aaaa', 'aaaa'))
# print(Connexion.identifier('admin', '1234'))








        # query = "SELECT id_ligne FROM lignes"
        # cls.__cursor.execute(query)
        # ligne = []
        # for lign in cls.__cursor:
        #     post = {}
        #     post['id_ligne'] = lign[0]
        #     ligne.append(post)
        # print(lign)
        # return ligne
        
# def lister_lignes(cls):
#         query = "SELECT nom FROM lignes"
#         cls.cursor.execute(query)
#         promo = []

#         for ligne in cls.cursor:
#             post = {}
#             post['nom'] = ligne[0]
#             promo.append(post)
#         print(ligne)
#         return promo
        # query="SELECT id_ligne, id_arret, nom, adresse FROM arrets"
        # cls.__cursor.execute(query)
        # arret = []
        # for aret in cls.__cursor:
        #     post1 = {}
        #     post1['id_ligne', 'id_arret', 'nom', 'adresse'] =aret=[0]
        #     arret.append(post1)
        # print(arret)
        # return arret
