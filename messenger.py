# Créé par compteadmin, le 27/10/2026 en Python 3.7
from datetime import datetime
import json
from colorama import Fore

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

class User :
    def __init__(self, id: int, name: str):
        self.id=id
        self.name= name


class Channel :
    def __init__(self, id: int, name: str, member_ids:list):
        self.id=id
        self.name= name
        self.member_ids = member_ids


class Message :
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id=id
        self.reception_date=reception_date
        self.sender_id=sender_id
        self.channel=channel
        self.content = content


def load_server_data_from_file () :
    data = json.load(open("storage.json"))
    L_user=[]
    for user in data['users'] :
        L_user.append(User(user['id'], user['name']))
    data['users']=L_user

    L_channel=[]
    for channel in data['channels'] :
        L_channel.append(Channel(channel['id'], channel['name'], channel['member_ids']))
    data['channels']=L_channel

    L_message=[]
    for message in data['messages'] :
        L_message.append(Message(message['id'], message['reception_date'], message['sender_id'], message['channel'], message['content']))
    data['messages']=message
    return (data)

server_data = load_server_data_from_file ()


#ajouter des utilisateurs
def see_user () :
    L=""
    for user in server_data ['users'] :
        print(type(user))
        L+=str(user['id'])+ ". " + user['name']+ "\n"
    print ('\nLes utilisateurs sont :\n',L)
    return()



#retour au menu principal
def retour () : 
    choix = input("\nr : Retour ?\n")      
    if choix == "r" :
        fonction()
    return()


#voir les groupes
def see_channels() :
    L=""
    for channel in server_data ['channels'] :
        L+=str(channel['id'])+ ". " + channel['name']+ "\n"
    print('\nLes groupes sont :\n', L)    
    return()       


#voir les messages
def see_messages(groupe) :
    L=[]
    bool = False
    for messages in server_data['messages'] :
        if str(messages['channel']) == groupe :
            bool = True
            for user in server_data['users'] :
                if messages["sender_id"] == user['id'] :
                    L.append ((messages["reception_date"], user["name"], messages["content"]))
    #def obtenir_date(x):
        #return x[0]
    L_triee= sorted (L, key=lambda x: x[2])
    print ("Les messages de ce groupe sont : \n")
    for i in range (len(L_triee)) :
        print(Fore.LIGHTBLACK_EX + str(L[i][0]) + " : " + Fore.BLUE + str(L[i][1]) + Fore.RESET + "-->" + str(L[i][2]))

    if not bool:
        print("L'id entré n'est pas relié à un groupe ou le groupe ne comporte pas de messages")
    return ()


#ajouter un utilisateur
def add_user() :
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
    serialisation(server_data)
    return()


#ajouter un groupe
def add_channel() :
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
    while member != 'non' : 
        member = input ("Souhaitez vous ajouter quelqu'un d'autre ?\nSi oui, tapez son id\nSi non, tapez non\n")
        server_data ["channels"].append ({'id': identifiant, 'name': nom, 'member_ids' : member})
    serialisation(server_data)
    return()

#ajouter des messages dans un groupe
def add_messages(id_groupe) :
    print ("Les utilisateurs de ce groupe sont :\n", see_users_groupe (id_groupe))
    id_sender = input ("Quel est votre id ? ")
    content = input ("Ecrivez votre message : ")
    reception_date = datetime.now()[:19]

    bool = False            # on attribue au message un id valable (pas déjà utilisé)
    identifiant = 0
    while not bool :
        identifiant+=1
        bool = True
        for channel in server_data['messages'] :
                if channel['id'] == identifiant :
                    bool = False

    server_data ["messages"].append ({'id': identifiant, 'reception_date': str(reception_date), 'sender_id' : int(id_sender), 'channel' : int(id_groupe), 'content' : content })
    serialisation(server_data)
    return()


#afficher les utilisateurs d'un groupe
def see_users_groupe (id_groupe) :
    L=""
    for channel in server_data['channels'] :
        if str(channel['id']) == id_groupe :
            L_users = channel['member_ids'] 
    for id_membres in L_users :
        for id_membres2 in server_data['users'] :
            if id_membres == id_membres2['id'] :
                L+=str(id_membres)+". "+str(id_membres2['name'])+"\n"
    return (L)
        



##################################--FONCTION--########################################################################""

def fonction () :
    print('=== Messenger ===')
    print('x. Leave | u : See Users | c : See Channels | +u : Add User | +c : Add Channel' )
    choice = input('Select an option: ')

    if choice == 'x':
        print('Bye!')

    #Afficher les utilisateurs
    elif choice == 'u' :  
        see_user()
        retour()
              
    #Afficher les groupes        
    elif choice == 'c':
        see_channels()        

        # Afficher les messages d'un groupe
        choix2 = input("\nmg : Voir les messages d'un groupe\nr : retour\n")

        if choix2 == "r" :     #Menu principal
            fonction()

        #Voir les messages d'un groupe
        elif choix2 == 'mg' :
            id_groupe = input ("\nEntrez l'id du groupe dont vous souhaitez voir les messages : " )
            see_messages(id_groupe)
            choix3 = input("\n+m : ajouter un message dans ce groupe\nr : retour\n")
            if choix3 == "r" :
                fonction()

            elif choix3 == "+m" :
                add_messages (id_groupe)
                retour()

 

    #Ajouter un utilisateur            
    elif choice == "+u" :
        add_user()
        retour()
        

    # Ajouter un groupe
    elif choice == "+c" :
        add_channel()
        retour()


    else:
        print('Unknown option:', choice)

        retour()


    return()


def serialisation(server_data):
    with open("storage.json", "w", encoding="utf-8") as f:
        json.dump(server_data, f, ensure_ascii=False, indent=4)


fonction()