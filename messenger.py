# Créé par compteadmin, le 27/10/2026 en Python 3.7
from datetime import datetime
import json

server_data = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}

#def load_server_data_from_file () :



def fonction () :
    print('=== Messenger ===')
    print('x. Leave | u : See Users | c : See Channels | +u : Add User | +c : Add Channel' )
    choice = input('Select an option: ')

    if choice == 'x':
        print('Bye!')

    #Afficher les utilisateurs
    elif choice == 'u' :                             
        L=""
        for user in server_data ['users'] :
            L+=str(user['id'])+ ". " + user['name']+ "\n"
        print ('\nLes utilisateurs sont :\n',L)
        
                   
        choix = input("\nr : Retour ?\n")       #Menu principal
        if choix == "r" :
            fonction()

    #Afficher les groupes        
    elif choice == 'c':
        L=""
        for channel in server_data ['channels'] :
            L+=str(channel['id'])+ ". " + channel['name']+ "\n"
            print ('\nLes groupes sont :\n', L)           

        # Afficher les messages d'un groupe
        print("\nmg : Voir les messages d'un groupe\nr : retour")
        choix2 = input ("")

        if choix2 == "r" :     #Menu principal
            fonction()

        #Voir les messages d'un groupe
        elif choix2 == 'mg' :
            groupe = input ("\nEntrez l'id du groupe dont vous souhaitez voir les messages :" )
            L=[]
            bool = False
            for messages in server_data['messages'] :
                if str(messages['channel']) == groupe :
                    bool = True
                    for user in server_data['users'] :
                        if messages["sender_id"] == user['id'] :
                            L.append ((messages["reception_date"], user["name"], messages["content"]))
            def obtenir_date(x):
                return x[0]
            L.sort(key=obtenir_date)
            print ("Les messages de ce groupe sont : \n", L)
            if not bool:
                print("L'id entré n'est pas relié à un groupe ou le groupe ne comporte pas de messages")

            print ("\n Retour ?")                   #Menu principal
            choix = input("oui | non \n")
            if choix == "oui" :
                fonction()

    #Ajouter un utilisateur            
    elif choice == "+u" :
        nom = input ("Quel est le nom de l'utilisateur que vous souhaitez ajouter ?")
        
        bool = False            # on lui attribue un id valable (pas déjà utilisé)
        identifiant = 0
        while not bool :
            identifiant+=1
            bool = True
            for user in server_data['users'] :
                if user['id'] == identifiant :
                    bool = False

        server_data ["users"].append ({'id': identifiant, 'name': nom})

        print ("\n Retour ?")               #Menu principal
        choix = input("oui | non \n")
        if choix == "oui" :
            fonction()

    # Ajouter un groupe
    elif choice == "+c" :
        nom = input ("Quel est le nom du groupe que vous souhaitez ajouter ?")
        
        bool = False            # on lui attribue un id valable (pas déjà utilisé)
        identifiant = 0
        while not bool :
            identifiant+=1
            bool = True
            for channel in server_data['channels'] :
                if channel['id'] == identifiant :
                    bool = False

        L=""
        for user in server_data ['users'] :
            L+=str(user['id']) + ". " + user['name']+ "\n"
        print ('\nLes utilisateurs sont :\n', L)
        member = input ("Quel est l'id des personnes que vous souhaitez ajouter dans le groupe?")
        server_data ["channels"].append ({'id': identifiant, 'name': nom, 'member_ids' : member})
       
        print ("\n Retour ?")               #Menu principal
        choix = input("oui | non \n")
        if choix == "oui" :
            fonction() 
    
    else:
        print('Unknown option:', choice)

        print ("\n Retour ?")
        choix = input("oui | non \n")
        if choix == "oui" :
            fonction()

    return()

fonction()