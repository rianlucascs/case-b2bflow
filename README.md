# case-b2bflow

Automação de envio de mensagens WhatsApp para leads via Twilio + Supabase.

---

## Configuração do banco de dados

Crie a tabela `Leads` no Supabase com a seguinte estrutura:

```sql
CREATE TABLE "Leads" (
    id        SERIAL PRIMARY KEY,
    criado_em TIMESTAMP DEFAULT NOW(),
    nome      TEXT NOT NULL,
    contato   TEXT NOT NULL
);
```

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@db.SEU_PROJECT_ID.supabase.co:5432/postgres

TWILIO_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_FROM=whatsapp:+14155238886
```

> **Atenção:** caracteres especiais na senha (ex: `@`) devem ser codificados em URL (ex: `%40`).

---

## Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar
python src.py
```
