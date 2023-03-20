# APS3_ALGLIN

Esse é um projeto da matéria de Algebra Linear e Teoria da Informação do Insper para o curso de Ciência da Computação.

## Descrição do Projeto
O projeto consiste em fazer um processador de efeito de vídeo em tempo real que faça o seu *streaming* de vídeo ficar "girando" na tela

## Descrição Matemática de cada função
### Funcao criar_indices
A função *criar_indices* recebe quatro argumentos: min_i, max_i, min_j e max_j. Importa o módulo "itertools" e usa a função "product" desse módulo para criar uma lista "L" que contêm todos os pares ordenados possíveis (i,j) com i variando entre min_i e max_i e j variando entre min_j e max_j. Depois, a função cria dois arrays numpy "idx_i" e "idx_j", que contêm, respectivamente, todos os valores de i e j da lista "L". E assim, a função empilha os arrays "idx_i" e "idx_j" verticalmente, usando a função "vstack" do numpy, para criar uma matriz de índices com duas linhas e N colunas (onde N é o número de pares ordenados possíveis), em que a primeira linha contém todos os valores de i e a segunda linha contém todos os valores de j. E por fim, retorna a matriz de índices criada.

### Funcao run
A função *run* é responsável por abrir a câmera do computador e mostrar a imagem capturada em tempo real. A largura e altura da imagem são definidas, width = 320 e height = 240 e uma dica é fornecidas para otimizar o processamento, imagens menores precisam de menos processamento. Em seguida, é verificado se outros dispositivos estão acessando a câmera. É definida uma matriz de rotação identidade para ser incrementada, e outra matriz de rotação para ser multiplicada pela primeira. Em seguida, é iniciado um loop que é encerrado quando 'q' é pressionado no teclado. A cada iteração, um novo frame é capturado da câmera, o tamanho do frame é reduzido para reduzir o processamento necessário nas próximas etapas e é verificado se o frame foi capturado com sucesso. A imagem é girada ou contraiada de acordo com o teclado pressionado pelo usuário, ultilizando as teclas 'a' e 'd', no qual a contração é uma transformação que reduz as dimensões de uma imagem. Depois de todas as transformações, a imagem resultante é exibida na tela por 40ms. Se 'q' é pressionado, o loop é encerrado e os recursos são devolvidos ao sistema.

## Como rodar o projeto
Para rodar o projeto e testar o projeto, basta acessar e rodar o arquivo demo.py, nesse arquivo você pode visualizar a sua camera. Com as teclas "A" ou D" fazer sua camera rodar e a tecla "Q" para fechar a janela da imagem exibida.
    
## Prévia

![Screen Recording 2023-03-19 at 8 17 17 PM](https://user-images.githubusercontent.com/89090868/226216337-89e914f3-29e2-432b-bf71-e53f08e71586.gif)

## Autores

- [@st4pzz](https://github.com/st4pzz)
- [@WeeeverAlex](https://github.com/WeeeverAlex)
