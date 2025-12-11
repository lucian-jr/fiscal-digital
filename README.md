# 🏙️ Fiscal Digital - Sistema de Monitoramento Urbano (GovTech)

Sistema de triagem e monitoramento de denúncias cidadãs em tempo real, desenvolvido como POC (Prova de Conceito) para arquiteturas de Cidades Inteligentes.

## 🚀 Tecnologias Utilizadas
- **Python 3.9 + FastAPI**: API de alta performance e assíncrona.
- **WebSockets**: Comunicação Full-Duplex para alertas em tempo real.
- **Docker**: Containerização completa da aplicação.
- **IA/NLP (Simulado)**: Classificação automática de urgência e categorização de denúncias.
- **Background Tasks**: Processamento assíncrono de dados para evitar latência.

## ⚙️ Arquitetura
O sistema recebe denúncias via API REST, processa a análise de risco em segundo plano e, caso detecte palavras-chave de alta prioridade (ex: "fogo", "acidente"), dispara um alerta instantâneo para todos os painéis de monitoramento conectados via WebSocket.

## 🛠️ Como Rodar

### Pré-requisitos
- Docker instalado

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/lucian-jr/fiscal-digital.git