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
import smtplib, ssl, os
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

MeuLocal = os.path.dirname(os.path.realpath(__file__))

#Get e-mail access information (após escopo do 'with' a arquivo será fechado)
with open(MeuLocal + "//bkp_DoNOT_UploadToGitHubb//access.json", 'r', encoding='utf8') as read_file:
   DadosDeAcesso = json.load(read_file)
   SENDER = DadosDeAcesso["SENDER"]
   PASSWORD = DadosDeAcesso["PSWRD"]
   SUBJECT = DadosDeAcesso["TITLE"]
   EMAIL_TEXT = DadosDeAcesso["BODY"]

#This function called to send a email.
#Dest -> Necessary to inform the e-mail destination
#Name[optional] -> inform the name of the file to be attached (ONLY pdf files)
def SendEmail( Dest='', Name = '', Ref = ''):
   if Dest == '':
      print("Not possible to send to empty destination")
   else:
      DESTINATION = Dest

      #new EmailMessage type.
      msg = EmailMessage()
      msg["Subject"] = SUBJECT + ' Ref.: ' + Ref
      msg["From"] = SENDER
      msg["To"] = DESTINATION
      msg.set_content(EMAIL_TEXT)

      if Name != '':
         print("Anexar Boleto com nome: ", Name)
         file_name = Attach(Name)

         #Somente envia se encontrar arquivo do boleto
         if file_name != 0:
            #msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            msg.add_attachment(Anexo.FileData, maintype='application', subtype='octet-stream', filename=Anexo.FileName)

            print("Sendding...")
            #Envia a mensagem
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
               smtp.login(SENDER, PASSWORD)
               smtp.send_message(msg)

            print("Sent!\n")

      else:
         #caso queira enviar sem anexo

         print("Sem anexo - Envio abortado")

         # print("Sendding...")
         # #Envia a mensagem
         # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         #    smtp.login(SENDER, PASSWORD)
         #    smtp.send_message(msg)

         # print("Sent!")


#Busca arquivo pelo nome informado para busca
#Caso o retorno de erro, então retorna 0
def Attach(File=''):
   
   #Tenta buscar e inserir 1 anexo no e-mail    
   try:
      arquivo = 'Boletos/'+File+'.pdf'
      with open(arquivo, 'rb') as f:
         Anexo.FileData = f.read() # file_data = f.read()
         Anexo.FileName = f.name # file_name = f.name
   except IOError:
      print(" ************************************ \n")
      print(" **** NÃO FOI ENCONTRADO BOLETO ***** \n")
      print(" ************************************ \n")
      return 0

