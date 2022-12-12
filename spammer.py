import requests, threading, pystyle, colorama, os, json 
from colorama import Fore 
from pystyle import Colorate, Colors 
  
header = { 
         "content-type": "application/json" 
     } 
     
print(Fore.RED + """
████████╗██╗░░░██╗██████╗░███████╗
╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝
░░░██║░░░░╚████╔╝░██████╔╝█████╗░░
░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░
░░░██║░░░░░░██║░░░██║░░░░░███████╗
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝
""") 

print(Fore.BLUE + """
╔══════════════════════════════╗     
║ Herramienta Desarrollada por Type&║
║ Espero que disfruten de esta      ║
║ herramienta para poder spammear   ║
║servidores                         ║
╚══════════════════════════════╝   
""")
  
data = { 
     "content": input(Fore.CYAN + "[ + ] Mensaje de spam: "), 
     "username": input(Fore.RED + "[ + ] Nombre del bot: "), 
     "avatar_url": input(Fore.GREEN + "[ + ] Avatar del bot: ") 
   } 
   
webhooks = input(Fore.YELLOW + "[ + ] URL Del Webhook: ") 
  
def main(webhook): 
   os.system('cls' if os.name=='nt' else 'clear') 
  
  
while True: 
   requests.post(webhooks, headers = header, json = data) 
   print(Fore.MAGENTA + "[ + ] ¡El mensaje ha sido enviado!") 
  
if __name__ == "__main__": 
   for webhook in webhooks: 
     threading.Thread(target=main, args=(webhook,)).start()
