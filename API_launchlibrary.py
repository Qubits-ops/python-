# Importation des bibliothèques
import requests # Permet de gérer les requêtes 'requests.get'
import operator # Permet de trier selon un item 'operator.itemgetter()''

# Lance la requête
resp = requests.get('https://launchlibrary.net/1.3/launch?next=100')
# Détection d'erreur
if resp.status_code != 200:
    # Si status_code vaut 200, cela veut dire que la requête a rencontré un problème
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# On récupère la valeur associé à la clé 'launches'
reponse = resp.json()['launches'] # reponse contient alors la liste des lancements
# Création de la liste des lanceurs.
lanceurs = {'Angara':0, 'Soyuz':0, 'Falcon':0, 'Ariane':0 , 'Delta':0, 'Atlas':0}
compteur = 0#initialisation du compteur
for j in reponse:#pour j dans liste des lancements
    nom_lanc_fal = j['name']#on recupere le nom du lanceur via la cle 'name'
    if('Falcon' in nom_lanc_fal):#on regarde si "falcon" est present dans le nom des lanceurs
        compteur+=1#on incremente
print("le nombre de lancement pour falcon est de ",compteur)#on affiche compteur pour connaitre le nombre de lanc pour falcon
for i in reponse:#pour i dans reponse
    nom_lanc = i['name'].split()[0]# On recupere le nom du lanceur via la cle 'name' et split() permet  de renvoyer la liste des éléments séparés par des espaces et index a 0 [0] pour renvoyer exemple:'ANGARA'
    for k in lanceurs:#pour k dans lanceurs
        if k in i['name']:#si le lanceurs ici (k) est dans le dico des lanceurs
            lanceurs[k]+=1#on incremente
    if nom_lanc not in lanceurs:#si nom_lanc n'est pas dans le dico lanceurs
        lanceurs[nom_lanc] = 1#on creer la cle nom_lanc de valeur 1
lanceurs_mis_a_jour = sorted(lanceurs.items())#trie ascendant du dico via la fonction sorted() qui trie une liste dans l'ordre alphabetique on prend le.items() car on prend la cle et la valeur .
lanceurs_mis_a_jour
