# APS3_ALGLIN

Esse é um projeto da matéria de Algebra Linear e Teoria da Informação do Insper para o curso de Ciência da Computação.

## Descrição do Projeto
O projeto consiste em fazer um processador de efeito de vídeo em tempo real que faça o seu *streaming* de vídeo ficar "girando" na tela

## Descrição Matemática de cada função
### Funcao criar_indices
A função *criar_indices* recebe quatro argumentos: min_i, max_i, min_j e max_j. Importa o módulo "itertools" e usa a função "product" desse módulo para criar uma lista "L" que contêm todos os pares ordenados possíveis (i,j) com i variando entre min_i e max_i e j variando entre min_j e max_j. Depois, a função cria dois arrays numpy "idx_i" e "idx_j", que contêm, respectivamente, todos os valores de i e j da lista "L". E assim, a função empilha os arrays "idx_i" e "idx_j" verticalmente, usando a função "vstack" do numpy, para criar uma matriz de índices com duas linhas e N colunas (onde N é o número de pares ordenados possíveis), em que a primeira linha contém todos os valores de i e a segunda linha contém todos os valores de j. E por fim, retorna a matriz de índices criada.

### Funcao run
A função *run* é responsável por abrir a câmera do computador e mostrar a imagem capturada em tempo real, permitindo que o usuário aplique transformações interativas na imagem. Para isso, ela usa a biblioteca OpenCV (cv) para acessar a câmera e capturar cada quadro da imagem. O tamanho da imagem é definido com width = 320 e height = 240, o que permite que o processamento necessário nas próximas etapas seja reduzido. A função utiliza um loop que captura cada frame da câmera e aplica uma série de transformações nele, permitindo que o usuário manipule a imagem em tempo real. Dentro do loop, a função aplica uma matriz de rotação de 10 graus sobre a imagem, que pode ser incrementada ou decrementada a cada loop, dependendo da entrada do usuário. Em seguida, a função realiza uma transformação na imagem usando uma matriz de transformação que envolve uma matriz de rotação, uma matriz de translação e a inversa da matriz de translação. Também é criada uma matriz de índices para mapear cada ponto da imagem original para a imagem transformada. Também é feita a contração ou *scaling down* que faz transformação, reduzindo as dimensões da imagem. Ela é realizada pela multiplicação da matriz da imagem original por uma matriz de transformação que especifica o fator de escala de cada dimensão. Em seguida, as duas matrizes de transformação são multiplicadas para formar uma única matriz de transformação no qual, as coordenadas da imagem original são multiplicadas pela matriz de transformação invertida para obter as coordenadas da imagem transformada. Deste modo, a imagem original é contraída pela metade em largura e movida para a direita em 50 pixels. Além disso, a função cria um filtro para remover os pontos que não estão dentro da imagem. Por fim, a função atribui os valores da imagem original para a imagem transformada e mostra a imagem transformada na tela. O loop só é interrompido quando o usuário pressiona a tecla 'Q' no teclado e a função permite que o usuário rotacione a imagem para a esquerda ou para a direita ao pressionar as teclas 'A' ou 'D', respectivamente. Por tanto, quando o loop é interrompido, a função libera os recursos da câmera e fecha a janela da imagem exibida na tela.

## Como rodar o projeto
Para rodar o projeto e testar o projeto, basta acessar e rodar o arquivo demo.py, nesse arquivo você pode visualizar a sua camera. Com as teclas "A" ou D" fazer sua camera rodar e a tecla "Q" para fechar a janela da imagem exibida.
    
## Prévia

![Screen Recording 2023-03-19 at 8 17 17 PM](https://user-images.githubusercontent.com/89090868/226216337-89e914f3-29e2-432b-bf71-e53f08e71586.gif)

## Autores

- [@st4pzz](https://github.com/st4pzz)
- [@WeeeverAlex](https://github.com/WeeeverAlex)
