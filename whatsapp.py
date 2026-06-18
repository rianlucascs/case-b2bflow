import os
from dotenv import load_dotenv
from twilio.rest import Client
from logger import get_logger

    
class WhatsApp:
    """Classe para enviar mensagens de texto via WhatsApp usando a API do Twilio."""
    

    def __init__(self):
        
        self.log = get_logger("whatsapp")
        
        load_dotenv()
        self.load()

    def load(self) -> None:
        
        try:
        
            self.client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_TOKEN"])
            self.client.api.accounts(os.environ["TWILIO_SID"]).fetch()
        
        except Exception as e:
            
            self.log.error(f"Erro ao inicializar o cliente Twilio: {e}")
            
            raise
            
    def send_text(self, to: str, message: str):
        
        try:
        
            result = self.client.messages.create(
                from_=os.environ["TWILIO_FROM"],
                to=f"whatsapp:{to}",
                body=message
            )
        
        except Exception as e:
            
            self.log.error(f"Erro ao enviar mensagem para {to}: {e}")
            
            raise
        
        self.log.info(f"Mensagem enviada para {to} | SID: {result.sid} | Status: {result.status}")
        
        return result