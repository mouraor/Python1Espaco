
import pandas as pd
import os
import email_service

# #Configura local de execução do script
# MeuLocal = os.path.dirname(os.path.realpath(__file__))
# local = MeuLocal + 'bkp_DoNOT_UploadToGitHubb/Controle.xlsx'

#Abre aquivo excel
arq = pd.ExcelFile(r'Controle.xlsx')

#Seleciona aba/planilha 2 (indice começa do 0)
Sheet_cadastro = arq.parse(2)
#armazena valores da coluna 'Responsável'
lista_Responsaveis = Sheet_cadastro['Responsável']
print('Carregou aba Responsáveis')

#Para cada Responsável, pega nome e contato
var = 0
for contatos in lista_Responsaveis:
   #Nome responsável
   nomeResp = Sheet_cadastro.loc[[var], ['Responsável']]
   Nome_Dest = nomeResp.to_string(header=None, index=False)#.replace(' ', '')
   Nome_Dest = Nome_Dest[1:]

   #Contao email responsável
   contatoResp = Sheet_cadastro.loc[[var], ['Contato']]
   email_Dest = contatoResp.to_string(header=None, index=False).replace(' ', '')
   
   #nome aluno
   Aluno = ''
   Aluno = Sheet_cadastro.loc[[var], ['Aluno']]
   nome_aluno = Aluno.to_string(header=None, index=False)#.replace(' ', '')
   nome_aluno = nome_aluno[1:]

   print("Enviar para responsável de: ", nome_aluno)

   #Se tiver ';' tem 2 emails de contato
   if email_Dest.count(';') != 0:
      print("...")
      #Primeiro end email (até ;)
      email_1 = email_Dest[0:email_Dest.find(';')]
      #segunda end email (depois ; [soma 3 carry + return] até fim)
      email_2 = email_Dest[email_Dest.find(';')+3:]

      print("Nome: ", Nome_Dest, " / Contato: ", email_1)
      email_service.SendEmail(email_1, Nome_Dest, nome_aluno)
      
      print("Nome: ", Nome_Dest, " / Contato: ", email_2)
      email_service.SendEmail(email_2, Nome_Dest, nome_aluno)
   else:
      #Call the sendEmail service (If the name is not fill the attachment is not sent)
      print("Nome: ", Nome_Dest, " / Contato: ", email_Dest)
      email_service.SendEmail(email_Dest, Nome_Dest, nome_aluno)
   
   #proximo
   var = var + 1
