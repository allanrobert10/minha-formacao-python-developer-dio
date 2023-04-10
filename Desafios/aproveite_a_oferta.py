''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''

''' 
TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
      para obtenção dos valores.
TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
         aproveitar ao máximo a oferta.
'''

T = int(input()) # Número de testes


for i in range(T):
     N, K = input().split() # Tratamento dos dados inseridos
     N = int(N)
     K = int(K)
     
     total = int((N % K) + (N / K)) # Resto da divisão de 'N' e 'K' mais o resultado da divisão dos mesmos
     
     print(total) # Imprime o resultado