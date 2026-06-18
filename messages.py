


class Messages:
    
    
    @staticmethod
    def welcome_message(name) -> str:
        return f"Olá, {name} tudo bem com você?"
   
    
    @staticmethod
    def approved_message(name) -> str:
        return (
            f"Olá, {name}! 🏆\n\n"
            "É com grande alegria que informamos: você foi *APROVADO(A)*!\n\n"
            "Parabéns pela sua dedicação e desempenho ao longo do processo.\n\n"
            "Em breve você receberá mais detalhes sobre os próximos passos. Bem-vindo(a) ao time! 🚀"
        )
    