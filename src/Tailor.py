# Código 1
!sudo apt-get update -y && sudo apt-get install -y zstd

!curl -fsSL https://ollama.com/install.sh | sh

import subprocess
import time
import os
import json

subprocess.Popen(["ollama", "serve"])
time.sleep(5) 

!ollama pull llama3.2:1b
!pip install -q ollama

os.makedirs('data', exist_ok=True)

guia_medicao = {
    "instrucoes_gerais": "Para descobrir o tipo de corpo, use uma fita métrica sem apertar a pele.",
    "passos_medicao": [
        "1. Ombro/Busto: Meça na parte mais larga do peito/ombros.",
        "2. Cintura: Meça a parte mais estreita do tronco (normalmente logo acima do umbigo).",
        "3. Quadril: Meça na parte mais larga do bumbum/quadril."
    ],
    "regra_identificacao": [
        "Triângulo Invertido (V): Busto/Ombros visivelmente maiores que o Quadril.",
        "Ampulheta: Busto e Quadril de tamanhos similares, com Cintura bem marcada.",
        "Retângulo: Busto, Cintura e Quadril com medidas muito parecidas.",
        "Triângulo (Pêra): Quadril visivelmente maior que os Ombros/Busto.",
        "Oval: Região da cintura mais volumosa ou alinhada ao busto/quadril."
    ]
}

estilos_moda = [
    {
        "nome_estilo": "Casual (Clean Girl / Clean Boy)",
        "descricao": "Visual minimalista, básico e alinhado. Peças neutras, caimento impecável e aparência leve.",
        "pecas_chave": ["Camisetas básicas de algodão pesado", "Tênis branco minimalista", "Jeans reto neutro", "Regatas lisas", "Blazers leves"]
    },
    {
        "nome_estilo": "Elegante",
        "descricao": "Sofisticado e atemporal. Foco em tecidos de alta qualidade e caimentos alinhados.",
        "pecas_chave": ["Calças de alfaiataria", "Camisas de botão em linho ou tricoline", "Mocassins/Scarpins", "Cintos finos de couro", "Vestidos de corte reto/envelope"]
    },
    {
        "nome_estilo": "Corporativo / Formal",
        "descricao": "Profissional, sério e elegante para ambientes de trabalho e reuniões.",
        "pecas_chave": ["Ternos e blazers estruturados", "Calças sociais/alfaiataria", "Camisas sociais engomadas", "Sapatos de couro ou salto bloco"]
    },
    {
        "nome_estilo": "Streetwear",
        "descricao": "Urbano, moderno e confortável, influenciado pela cultura das ruas, skate e esportes.",
        "pecas_chave": ["Camisetas oversize", "Calças cargo ou wide leg", "Tênis esportivos/sneakers em destaque", "Moletom pesado", "Acessórios como bonés e correntes"]
    },
    {
        "nome_estilo": "Dark (Emo / Gótico)",
        "descricao": "Expressivo, alternativo e predominantemente em tons escuros ou pretos.",
        "pecas_chave": ["Jaquetas de couro preto", "Coturnos e botas pesadas", "Calças/saias pretas com correntes ou ilhós", "Roupas com sobreposição e texturas de renda/couro"]
    }
]

recomendacoes_corpo = {
    "triangulo_invertido": {
        "tipo_corpo": "Triângulo Invertido (Corpo V)",
        "foco": "Traga volume/atenção para a parte inferior do corpo, equilibra com os ombros.",
        "sugestoes": ["Calças pantalona, cargo ou wide leg", "Saias evasê ou plissadas", "Decote V aplana o tronco"],
        "evitar": ["Ombreiras", "Babados nos ombros", "Decote ombro a ombro"]
    },
    "v": {
        "tipo_corpo": "Triângulo Invertido (Corpo V)",
        "foco": "Trazer volume/atenção para a parte de inferior do corpo, equilibra com os ombros.",
        "sugestoes": ["Calças pantalona, cargo ou wide leg", "Saias evasê ou plissadas", "Decote V aplana o tronco"],
        "evitar": ["Ombreiras", "Babados nos ombros", "Decote ombro a ombro"]
    },
    "triangulo": {
        "tipo_corpo": "Triângulo (Corpo Pêra)",
        "foco": "O volume/atenção na parte de cima do tronco, equilibra com quadril mais largo.",
        "sugestoes": ["Blusas com babados, estampas ou mangas bufantes", "Decote canoa, ciganinha", "Jaquetas estruturadas", "Calças e saias de corte reto em cores escuras"],
        "evitar": ["Calças com muitos bolsos laterais (cargo)", "Estampas chamativas na parte de baixo", "Saias muito armadas no quadril"]
    },
    "pera": {
        "tipo_corpo": "Triângulo (Corpo Pêra)",
        "foco": "Trazer volume e atenção para a parte de cima do tronco para equilibrar com o quadril mais largo.",
        "sugestoes": ["Blusas com babados, estampas ou mangas bufantes", "Decote canoa ou ciganinha", "Jaquetas estruturadas", "Calças e saias de corte reto em cores escuras"],
        "evitar": ["Calças com muitos bolsos laterais (cargo)", "Estampas chamativas na parte de baixo", "Saias muito armadas no quadril"]
    },
    "ampulheta": {
        "tipo_corpo": "Ampulheta",
        "foco": "Valorizar a cintura natural sem criar volumes desproporcionais.",
        "sugestoes": ["Vestidos e blusas envelope", "Cintos na cintura", "Calças de cintura alta"],
        "evitar": ["Roupas excessivamente saco ou sem nenhuma estrutura no meio do corpo"]
    },
    "retangulo": {
        "tipo_corpo": "Retângulo",
        "foco": "Criar ilusão de curvas ou aproveitar o caimento reto de forma moderna.",
        "sugestoes": ["Cortes assimétricos", "Cintos contrastantes", "Sobreposições e jaquetas acinturadas"],
        "evitar": ["Cortes muito retos sem nenhum detalhe visual"]
    },
    "oval": {
        "tipo_corpo": "Oval",
        "foco": "Alongar a silhueta, criar linhas verticais e trazer estrutura sem apertar a região central do corpo.",
        "sugestoes": ["Decote V ou U profundo", "Terceira peça aberta (blazers, cardigans compridos)", "Look monocromático", "Tecidos encorpados de caimento fluido"],
        "evitar": ["Cintos muito apertados na cintura", "Roupas excessivamente coladas ou extremamente largas"]
    }
}

with open('data/guia_medicao.json', 'w', encoding='utf-8') as f:
    json.dump(guia_medicao, f, ensure_ascii=False, indent=2)

with open('data/estilos_moda.json', 'w', encoding='utf-8') as f:
    json.dump(estilos_moda, f, ensure_ascii=False, indent=2)

with open('data/recomendacoes_corpo.json', 'w', encoding='utf-8') as f:
    json.dump(recomendacoes_corpo, f, ensure_ascii=False, indent=2)

print("✅ Ambiente configurado, Ollama pronto e pasta 'data/' criada com sucesso!")

# Código 2
!ollama pull qwen2.5:7b


# Código 3
!pip install -q gradio ollama transformers torch

import json
import subprocess
import time
import re
import ollama
import gradio as gr
from transformers import pipeline

def garantir_ollama():
    try:
        ollama.list()
    except Exception:
        print("Iniciando Ollama...")
        subprocess.Popen(["ollama", "serve"])
        time.sleep(5)

garantir_ollama()

NOME_MODELO = "qwen2.5:7b"

try:
    ollama.show(NOME_MODELO)
except Exception:
    print(f"Baixando modelo {NOME_MODELO}...")
    ollama.pull(NOME_MODELO)

print("Carregando modelo de classificação de escopo (Hugging Face)...")
classificador_escopo = pipeline(
    "zero-shot-classification",
    model="cross-encoder/nli-deberta-v3-small"
)
print("Classificador de escopo pronto!")


with open('data/guia_medicao.json', 'r', encoding='utf-8') as f:
    guia_medicao = json.load(f)
with open('data/estilos_moda.json', 'r', encoding='utf-8') as f:
    estilos_moda = json.load(f)
with open('data/recomendacoes_corpo.json', 'r', encoding='utf-8') as f:
    recomendacoes_corpo = json.load(f)


PALAVRAS_EVENTO = {
    "reunião", "reuniao", "casamento", "festa", "jantar", "aniversário", "aniversario", 
    "formatura", "batizado", "encontro", "evento", "balada", "trabalho", "entrevista", "15"
}

TEXTO_MENU = """Olá! Sou o **Tailor**, seu consultor de estilo pessoal. 👔

Como posso ajudar no seu visual hoje? Você pode escolher uma das opções abaixo ou me fazer uma pergunta direta:

1️⃣ **Descobrir seu tipo de corpo** (passo a passo de medição)
2️⃣ **Conhecer peças ideais para cada biotipo**
3️⃣ **Explorar estilos para eventos e ocasiões**
4️⃣ **Encerrar atendimento**"""

LISTA_ESTILOS_TEXTO = """Qual destes estilos mais combina com o ambiente ou sua preferência?

1️⃣ **Casual** (descontraído e leve)
2️⃣ **Elegante** (sofisticado e alinhado)
3️⃣ **Corporativo / Formal** (profissional e sério)
4️⃣ **Streetwear** (urbano e moderno)
5️⃣ **Dark** (expressivo e tons escuros)

Digite o **número** ou o **nome** do estilo!"""

def extrair_texto_str(conteudo):
    if isinstance(conteudo, str):
        return conteudo
    if isinstance(conteudo, list):
        textos = []
        for elem in conteudo:
            if isinstance(elem, dict):
                textos.append(elem.get('text', str(elem)))
            else:
                textos.append(str(elem))
        return " ".join(textos)
    if isinstance(conteudo, dict):
        return conteudo.get('text', str(conteudo))
    return str(conteudo)

def eh_pergunta_explicativa(texto):
    t = texto.lower()
    padroes = ["por que", "porque", "como assim", "qual o motivo", "origem", "explique", "explicar", "detalhe", "detalhar", "me fale mais", "por qual razão"]
    return any(p in t for p in padroes) or "?" in t

def eh_pedido_detalhado(texto):
    t = texto.lower()
    termos = ["explique", "explicar", "detalhe", "detalhar", "por que", "porque", "como assim", "aprofundar", "mais detalhes", "descreva", "por qual razão", "qual motivo", "me diga mais"]
    return any(term in t for term in termos)

def verificar_se_e_sobre_moda(texto):
    t = texto.strip().lower()

  
    if t in ["1", "2", "3", "4", "5", "sair", "exit", "menu", "oi", "ola", "olá", "ajuda", "voltar", "inicio", "início"]:
        return True
        
    labels = [
        "moda, vestuário, roupas, alfaiataria, caimento e estilo de vestir",
        "outros assuntos gerais, piadas sem relação com roupas, cultura pop, celebridades, gastronomia, tecnologia"
    ]
    
    resultado = classificador_escopo(texto, candidate_labels=labels)
    top_label = resultado['labels'][0]
    score = resultado['scores'][0]
    
    if top_label == labels[0] and score >= 0.40:
        return True
    return False

def extrair_medidas(texto):
    texto_lower = texto.lower()
    busto_match = re.search(r'(?:busto|ombro)s?[\s:=]*(\d+[\.,]?\d*)', texto_lower)
    cintura_match = re.search(r'cinturas?[\s:=]*(\d+[\.,]?\d*)', texto_lower)
    quadril_match = re.search(r'quadrils?[\s:=]*(\d+[\.,]?\d*)', texto_lower)
    
    if busto_match and cintura_match and quadril_match:
        try:
            b = float(busto_match.group(1).replace(',', '.'))
            c = float(cintura_match.group(1).replace(',', '.'))
            q = float(quadril_match.group(1).replace(',', '.'))
            return b, c, q
        except ValueError:
            return None
    return None

def calcular_biotipo_por_medidas(b, c, q):
    if b <= 0 or c <= 0 or q <= 0:
        return None
    if c >= b and c >= q:
        return "oval"
    maior_bq = max(b, q)
    diferenca_percentual_bq = abs(b - q) / maior_bq
    if diferenca_percentual_bq <= 0.08:
        if c <= (b * 0.82) and c <= (q * 0.82):
            return "ampulheta"
        else:
            return "retangulo"
    else:
        if b > q:
            return "triangulo_invertido"
        else:
            return "triangulo"

def extrair_biotipo_exato(texto):
    texto_norm = texto.lower()
    if "invertido" in texto_norm or "tipo v" in texto_norm or "corpo v" in texto_norm:
        return "triangulo_invertido"
    elif "triangulo" in texto_norm or "triângulo" in texto_norm or "pera" in texto_norm or "pêra" in texto_norm:
        return "triangulo"
    elif "oval" in texto_norm or "barriga" in texto_norm:
        return "oval"
    elif "ampulheta" in texto_norm:
        return "ampulheta"
    elif "retangulo" in texto_norm or "retângulo" in texto_norm:
        return "retangulo"
    return None

def formatar_resposta_biotipo(dados):
    tipo = dados.get("tipo_corpo", "Seu Biotipo")
    foco = dados.get("foco", "")
    sugestoes = dados.get("sugestoes", [])
    evitar = dados.get("evitar", [])
    
    resposta = f"Para o biotipo **{tipo}**, a estratégia principal é {foco.lower() if foco else 'valorizar suas proporções'}.\n\n"
    if sugestoes:
        itens_usar = ", ".join(sugestoes) if isinstance(sugestoes, list) else sugestoes
        resposta += f"✨ **Peças que valorizam muito:** {itens_usar}.\n\n"
    if evitar:
        itens_evitar = ", ".join(evitar) if isinstance(evitar, list) else evitar
        resposta += f"⚠️ **Peças para ter atenção ou evitar:** {itens_evitar}.\n\n"
        
    resposta += "Quer sugestões de combinações específicas para algum evento ou peça em particular?"
    return resposta

def extrair_estilo_exato(texto):
    texto_norm = texto.lower().strip()
    if "casual" in texto_norm or "clean" in texto_norm:
        return 0
    elif "elegante" in texto_norm:
        return 1
    elif "formal" in texto_norm or "corporativo" in texto_norm:
        return 2
    elif "streetwear" in texto_norm or "street" in texto_norm or "urbano" in texto_norm:
        return 3
    elif "dark" in texto_norm or "gotico" in texto_norm or "gótico" in texto_norm or "emo" in texto_norm:
        return 4
    return None

def formatar_resposta_estilo(estilo_dict):
    nome = estilo_dict.get("nome_estilo", "")
    desc = estilo_dict.get("descricao", "")
    pecas = estilo_dict.get("pecas_chave", [])
    
    resposta = f"O estilo **{nome}** traz uma proposta {desc.lower()}.\n\n"
    resposta += "👔 **Peças-chave para compor esse visual:**\n"
    resposta += "\n".join([f"• {item}" for item in pecas])
    resposta += "\n\nPrecisa de ajuda para adaptar esse estilo ao seu tipo de corpo?"
    return resposta

def responder_tailor(mensagem, historico):
    txt_usr = str(mensagem).lower().strip()
    
    if txt_usr in ["4", "sair", "exit", "quit"]:
        return "Foi um prazer ajudar! Se precisar de mais dicas de estilo no futuro, estarei por aqui. Até logo!"
        
    if txt_usr in ["menu", "0", "ajuda", "inicio", "início", "olá", "ola", "oi", "voltar"]:
        return TEXTO_MENU

    ultimo_msg_assistente = ""
    if historico:
        item_ultimo = historico[-1]
        if isinstance(item_ultimo, (list, tuple)) and len(item_ultimo) > 1:
            ultimo_msg_assistente = extrair_texto_str(item_ultimo[1]).lower()
        elif isinstance(item_ultimo, dict) and item_ultimo.get("role") == "assistant":
            ultimo_msg_assistente = extrair_texto_str(item_ultimo.get("content", "")).lower()

    em_contexto_estilos = "qual destes estilos" in ultimo_msg_assistente or "estilo você prefere" in ultimo_msg_assistente or "dress codes" in ultimo_msg_assistente

    if em_contexto_estilos and txt_usr in ["1", "2", "3", "4", "5"]:
        mapeamento_estilos_num = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
        idx = mapeamento_estilos_num[txt_usr]
        if idx < len(estilos_moda):
            return formatar_resposta_estilo(estilos_moda[idx])

    
    if txt_usr in ["1", "passo", "medir", "como me medir", "como medir", "medicao", "medição"]:
        return """Para descobrir seu biotipo, meça com uma fita métrica:
1. **Busto/Ombro:** Na parte mais larga do peito.
2. **Cintura:** Na parte mais estreita do tronco (acima do umbigo).
3. **Quadril:** Na parte mais larga do quadril/bumbum.

Quando tiver os valores, me envie assim: *'busto 90, cintura 70, quadril 95'* que eu calculo para você!"""

    if txt_usr == "2" or "peças ideais" in txt_usr:
        return "Posso indicar os melhores caimentos para os biotipos: **Triângulo Invertido (V)**, **Triângulo (Pêra)**, **Ampulheta**, **Retângulo** e **Oval**.\n\nVocê já sabe qual é o seu corpo ou prefere me enviar suas medidas?"

    if txt_usr == "3":
        return LISTA_ESTILOS_TEXTO

    
    medidas = extrair_medidas(txt_usr)
    if medidas:
        b, c, q = medidas
        if b < 40 or c < 40 or q < 40 or b > 220 or c > 220 or q > 220:
            return f"As medidas informadas (**busto {b}cm, cintura {c}cm, quadril {q}cm**) parecem fora do padrão em centímetros.\n\nPor favor, verifique se os números foram digitados em **centímetros** (exemplo: *busto 90, cintura 70, quadril 95*)."
            
        biotipo_calculado = calcular_biotipo_por_medidas(b, c, q)
        if biotipo_calculado and biotipo_calculado in recomendacoes_corpo:
            resposta_base = formatar_resposta_biotipo(recomendacoes_corpo[biotipo_calculado])
            return f"Analisando suas medidas (**Busto:** {b}cm | **Cintura:** {c}cm | **Quadril:** {q}cm):\n\n{resposta_base}"

  
    palavras_digitadas = set(re.findall(r'\b\w+\b', txt_usr))
    if bool(palavras_digitadas.intersection(PALAVRAS_EVENTO)):
        return f"Com certeza! Para eu te dar a recomendação perfeita para o seu evento, {LISTA_ESTILOS_TEXTO}"

  
    if not eh_pergunta_explicativa(txt_usr):
        biotipo_detectado = extrair_biotipo_exato(txt_usr)
        if biotipo_detectado and biotipo_detectado in recomendacoes_corpo:
            return formatar_resposta_biotipo(recomendacoes_corpo[biotipo_detectado])

        idx_estilo = extrair_estilo_exato(txt_usr)
        if idx_estilo is not None and idx_estilo < len(estilos_moda):
            return formatar_resposta_estilo(estilos_moda[idx_estilo])

   
    if not verificar_se_e_sobre_moda(mensagem):
        return f"Desculpe, sou um assistente especializado exclusivamente em **consultoria de moda, vestuário e estilo**. Não converso sobre outros assuntos.\n\n{TEXTO_MENU}"

    
    garantir_ollama()
    
    e_detalhado = eh_pedido_detalhado(txt_usr)
    if e_detalhado:
        instrucao_tamanho = "O usuário pediu uma explicação. Seja didático, explicativo e completo (até 200 palavras)."
        tokens_max = 550
    else:
        instrucao_tamanho = "Seja direto, sucinto, prático e objetivo (máximo 90 palavras)."
        tokens_max = 350

    system_instruction = f"""
Você é EXCLUSIVAMENTE o Tailor, um consultor de moda pessoal especialista em vestuário e alfaiataria.

TRAVA ABSOLUTA DE ESCOPO:
1. SEU ÚNICO DOMÍNIO É MODA, VESTUÁRIO, ALFAIATARIA E CONSULTORIA DE ESTILO.
2. NUNCA responda sobre outros assuntos (celebridades, piadas gerais, filmes, comida, etc.).
3. NUNCA diga que sabe conversar sobre outras áreas.
4. IDIOMA: Responda EXCLUSIVAMENTE em Português do Brasil.
5. EXTENSÃO DA RESPOSTA: {instrucao_tamanho}

REGRAS DE LÓGICA DE ALFAIATARIA:
- TERMOS PROIBIDOS: NUNCA invente termos inexistentes (ex: 'sobrecroppado', 'semicropped', 'retofit'). Use apenas termos reais (paletó trespassado, lapela picada, bainha dobrada).
- Para ENCURTAR / COMPACTAR silhuetas (pessoas muito altas que querem parecer menos compridas):
  • Recomende cores contrastantes entre blazer e calça (color blocking) para quebrar a linha vertical.
  • Paletó de abotoamento duplo (trespassado) e calças com barra dobrada (bainha).
  • JAMAIS recomende listras verticais ou looks monocromáticos para quem quer encurtar!
- Para ALONGAR silhuetas: Recomende looks monocromáticos e listras verticais.

CONTEXTO TÉCNICO DE MODA:
{json.dumps(recomendacoes_corpo, ensure_ascii=False)}
{json.dumps(estilos_moda, ensure_ascii=False)}
"""

    mensagens_payload = [{"role": "system", "content": system_instruction}]
    
    if historico:
        for item in historico:
            if isinstance(item, (list, tuple)):
                if len(item) > 0 and item[0]:
                    mensagens_payload.append({"role": "user", "content": extrair_texto_str(item[0])})
                if len(item) > 1 and item[1]:
                    mensagens_payload.append({"role": "assistant", "content": extrair_texto_str(item[1])})
            elif isinstance(item, dict):
                role = item.get("role", "user")
                content = extrair_texto_str(item.get("content", ""))
                mensagens_payload.append({"role": role, "content": content})
                
    mensagens_payload.append({"role": "user", "content": txt_usr})

    try:
        resposta = ollama.chat(
            model=NOME_MODELO,
            messages=mensagens_payload,
            options={
                "temperature": 0.1,
                "repeat_penalty": 1.2,
                "num_predict": tokens_max
            }
        )
        return resposta['message']['content']
    except Exception as e:
        return f"Desculpe, tive um problema ao consultar meu sistema de estilo: {e}"


demo = gr.ChatInterface(
    fn=responder_tailor,
    title="👔 Tailor - Consultor de Moda Pessoal",
    description=TEXTO_MENU,
    examples=[
        "1",
        "busto 90cm, cintura 70cm, quadril 95cm",
        "Tenho uma reunião de trabalho",
        "Estilo Elegante"
    ]
)

demo.launch(share=True)
