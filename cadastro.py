
import pandas as pd
import email_service, os      

MeuLocal = os.path.dirname(os.path.realpath(__file__))
local = MeuLocal + 'bkp_DoNOT_UploadToGitHubb/Controle.xlsx'

arq = pd.ExcelFile(r'bkp_DoNOT_UploadToGitHubb/Controle.xlsx')
#sheet start Start from 0
Sheet_cadastro = arq.parse(1)
lista_Responsaveis = Sheet_cadastro['Responsável']

#Para cada Responsável, pega nome e contato
var = 0
for contatos in lista_Responsaveis:
   nomeResp = Sheet_cadastro.loc[[var], ['Responsável']]
   Nome_Dest = nomeResp.to_string(header=None, index=False).replace(' ', '')
   
   contatoResp = Sheet_cadastro.loc[[var], ['Contato']]
   email_Dest = contatoResp.to_string(header=None, index=False).replace(' ', '')

   print("Enviar para: ")
   print("Nome: ", Nome_Dest, " / Contato: ", email_Dest)

   #Call the sendEmail service (If the name is not fill the attachment is not sent)
   email_service.SendEmail(email_Dest, Nome_Dest)
   var = var + 1
