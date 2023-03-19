import numpy as np
import cv2 as cv

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!

#função importada do notebook da aula da matéria que cria os índices para a matriz do frame da imagem
def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx


def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # definir uma matriz de rotação identidade para ser incrementada
    matriz_rotação_incrementa = np.eye(3)
    # definir uma matriz de rotação para ser multiplicada pela matriz_rotação_incrementa
    matriz_rotação = np.array([[0.98480774002, -0.17364825133, 0], [0.17364825133, 0.98480774002, 0],  [0, 0,1]])
    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.

    gira,contrai = False,False
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255

        #condição para girar a imagem
        if gira == True:
            # Crie uma imagem preta com o mesmo tamanho da imagem original
            image_ = np.zeros_like(image)

            # Crie os índices para a matriz do frame da imagem
            Xd= criar_indices(0, image.shape[0], 0, image.shape[1])
            
            # Adicione uma linha de 1s para facilitar a multiplicação
            Xd = np.vstack((Xd,np.ones((1,Xd.shape[1]))))

            # Crie uma matriz de translação para o centro da imagem
            matriz_translação = np.array([[1, 0, -(image.shape[0]/2)], [0, 1, -(image.shape[1]/2)], [0, 0,1]])        
            # Crie uma matriz única de transformação 
            matriz_transformação = np.linalg.inv(matriz_translação) @ matriz_rotação_incrementa @ matriz_translação

            # Cria uma nova matriz que é o resultado da multiplicação entre o inverso da matriz de transformação, para que todos os pixels da imagem original sejam transformados para a imagem transformada, e a matriz dos índices da imagem original.
            X = np.linalg.inv(matriz_transformação) @ Xd

            # Converter os valores para inteiros
            X = X.astype(int)
            # Converter os valores para inteiros
            Xd = Xd.astype(int)
            

            # Criar um filtro para remover os pontos que não estão na imagem
            filtro = (X[0,:]>=0)&(X[0,:]<image_.shape[0])&(X[1,:]>=0)&(X[1,:]<image_.shape[1])

            # Aplicar o filtro
            Xd = Xd[:,filtro]
            # Aplicar o filtro
            X = X[:,filtro]
           

            # Atribuir os valores da imagem original para a imagem transformada
            image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        
        #Condição para realizar uma contração na imagem   
        elif contrai == True:
             # Crie uma imagem preta com o mesmo tamanho da imagem original
            image_ = np.zeros_like(image)
        
            # Crie os índices para a matriz do frame da imagem
            Xd= criar_indices(0, image.shape[0], 0, image.shape[1])
            
            # Adicione uma linha de 1s para facilitar a multiplicação
            Xd = np.vstack((Xd,np.ones((1,Xd.shape[1]))))

            matriz_contracao = np.array([[0.5, 0, 0], [0, 1, 0], [0, 0,1]])
            matriz_translacao = np.array([[1, 0, 50], [0, 1, 0], [0, 0,1]]) 
            matriz_transformação = matriz_translacao @ matriz_contracao
            X = np.linalg.inv(matriz_transformação) @ Xd

            # Converter os valores para inteiros
            X = X.astype(int)
            # Converter os valores para inteiros
            Xd = Xd.astype(int)
            
            # Criar um filtro para remover os pontos que não estão na imagem
            filtro = (X[0,:]>=0)&(X[0,:]<image_.shape[0])&(X[1,:]>=0)&(X[1,:]<image_.shape[1])

            # Aplicar o filtro
            Xd = Xd[:,filtro]
            # Aplicar o filtro
            X = X[:,filtro]
            
            # Atribuir os valores da imagem original para a imagem transformada
            image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]
        else:
            image_ = image

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)

        # Aguardar 40ms para ver se o usuário apertou a tecla 
        q = cv.waitKey(40)
        
        # Se aperto 'q', encerro o loop
        if q == ord('q'):
            break
        # Se aperto 'a', a imagem começa a girar para direita
        elif q == ord('a'):
            gira = True
            # Incrementar a matriz de rotação
            matriz_rotação_incrementa = matriz_rotação @ matriz_rotação_incrementa  

        # Se aperto 'd', a imagem começa realiza uma expansão
        elif q == ord('d'):
            contrai = True

            
            
            

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    run()