#This service sends a text e-mail to the e-mail destination and with a pdf file attached if it is the case.
#TO use the gmail service smtp sll service it is necessary to modify the setting of gmail account in order to 
#allow external connection for sending the messages.

#on gemail
#Go to MyAccounts management
#Security -> activate the two step verification
#The create a app password on:
#password app

#This password will be used to access the source/sender of the e-mail

#This service loads this information from a json file, locally.

#setting the git io page
# on: https://pages.github.com/

import json
import smtplib, ssl
from email.message import EmailMessage
SENDER = ''
PASSWORD = ''
SUBJECT = ''
EMAIL_TEXT = ''

#For handle the information of the file to be attached
class DataFile:
   def __init__(self):
      self.FileData = 0;
      self.FileName = ""
   FileData:bytes
   FileName:str

Anexo = DataFile()

#Get e-mail access information (após escopo do 'with' a arquivo será fechado)
with open("access.json", 'r') as read_file:
   DadosDeAcesso = json.load(read_file)
   SENDER = DadosDeAcesso["SENDER"]
   PASSWORD = DadosDeAcesso["PSWRD"]
   SUBJECT = DadosDeAcesso["TITLE"]
   EMAIL_TEXT = DadosDeAcesso["BODY"]

#This function called to send a email.
#Dest -> Necessary to inform the e-mail destination
#Name[optional] -> inform the name of the file to be attached (ONLY pdf files)
def SendEmail( Dest='', Name = ''):
   if Dest == '':
      print("Not possible to send to empty destination")
   else:
      DESTINATION = Dest

      #new EmailMessage type.
      msg = EmailMessage()
      msg["Subject"] = SUBJECT
      msg["From"] = SENDER
      msg["To"] = DESTINATION
      msg.set_content(EMAIL_TEXT)

      if Name != '':
         print("Get the file by name", Name)
         file_name = Attach(Name)
         #msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
         msg.add_attachment(Anexo.FileData, maintype='application', subtype='octet-stream', filename=Anexo.FileName)
      else:
         print("No file to attach")

      print("Sendding...")
      #Envia a mensagem
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(SENDER, PASSWORD)
         smtp.send_message(msg)

      print("Sent!")


#Busca arquivo pelo nome informado para busca
def Attach(File=''):
   if File == '':
      print("No file informed")
   else:
      #Buscar e inserir 1 anexo no e-mail
      arquivo = 'Boletos/'+File+'.pdf'
      with open(arquivo, 'rb') as f:
         Anexo.FileData = f.read() # file_data = f.read()
         Anexo.FileName = f.name # file_name = f.name


