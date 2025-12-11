import time

class AnalisadorDeReclamacoes: 
    def __init__(self):
        self.palavras_urgentes = ["fogo", "acidente", "morte", "socorro", "emergência", "armado", "sequesto", "assalto"]
        self.palavras_saude = ["doença", "hospital", "médico", "remédio", "sintomas", "dor", "tratamento", "consulta"]
        
    def analisar_risco(self, descricao: str):
        
        print("Analisando reclamação com IA...")
        time.sleep(5)
        print("Análise concluída!")
        
        texto = descricao.lower()
        
        # Lógica 1: Define a Categoria
        categoria = "Geral"
        
        if any(p in texto for p in self.palavras_urgentes):
            categoria = "Urgente"
        elif "buraco" in texto or "asfalto" in texto or "lixo" in texto:
            categoria = "Infraestrutura"
            
        # Lógica 2: Define o Nível de Urgência
        urgente = any(p in texto for p in self.palavras_urgentes)
        
        return {
            "categoria": categoria,
            "urgencia": urgente,
            "score_risco": 0.99 if urgente else 0.20
        }