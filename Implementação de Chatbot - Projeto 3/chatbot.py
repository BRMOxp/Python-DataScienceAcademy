import openai
# API do ChatGPT, que deve ser adquirida em: https://openai.com/pricing
openai.api_key = "minha_chave_api"

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):
    response = openai.Completion.create(
    # Modelo usado
    engine = "text-davinci-003",
    # Texto inicial da conversa com o chatbot
    prompt = texto,
    # Comprimento da resposta gerada pelo modelo
    max_tokens = 150,
    # Conclusões a serem geradas para cada prompt
    n = 5,
    # O texto retornado não conterá a sequência de parada
    stop = None,
    # Uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
    temperature = 0.8,
)

    return response.choices[0].text.strip()
# Função principal do programa em Python
def main():
    print("\nBem vindo ao GPT-4 Chatbot do Projeto 3 do Curso na Data Science Academy!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")
    # Loop
    while True:
        # Coletar a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")
        # Se a mensagem for 'sair' finalizar o programa
        if user_message.lower() == 'sair':
            break
        # Colocar a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"
        # Obter a resposta do modelo executando a função gera_texto()
        chatbot_response = gera_texto(gpt4_prompt)
        # Imprimir a resposta do chatbot
        print(f"\nChatbot: {chatbot_response}")
# Execução do programa (bloco main) em Python
if __name__ == "__main__":
    main()