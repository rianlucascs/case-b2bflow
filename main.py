from logger import reset_log
from db import Database
from whatsapp import WhatsApp
from messages import Messages


class MessagingService:
    
    """Classe principal para orquestrar a leitura do banco de dados e o envio de mensagens via WhatsApp."""
    
    def __init__(self):
        
        reset_log()
        
        self.db = Database()
        self.whatsapp = WhatsApp()
        self.messages = Messages()
        
    def main(self) -> None:
        
        leads = self.db.select_all(limit=1)
        
        for nome, contato in leads.iloc[:, [2, 3]].values:
            
            # Gerar mensagem personalizada
            message = self.messages.welcome_message(nome)
            
            # Enviar mensagem via WhatsApp
            self.whatsapp.send_text(contato, message)
            
            
if __name__ == "__main__":
    
    messaging_service = MessagingService()
    messaging_service.main()



