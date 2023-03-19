import numpy as np
import cv2 as cv

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
# Para instalar, rode o comando abaixo no terminal:
# pip install opencv-python

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

    matriz_rotação_incrementa = np.eye(3)
    matriz_rotação = np.array([[np.cos(np.radians(10)), -np.sin(np.radians(10)), 0], [np.sin(np.radians(10)), np.cos(np.radians(10)), 0],  [0, 0,1]])
    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
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
        image_ = np.zeros_like(image)
        Xd= criar_indices(0, image.shape[0], 0, image.shape[1])
        Xd = np.vstack((Xd,np.ones((1,Xd.shape[1]))))
        matriz_translação = np.array([[1, 0, -(image.shape[0]/2)], [0, 1, -(image.shape[1]/2)], [0, 0,1]])        
        matriz_transformação = np.linalg.inv(matriz_translação) @ matriz_rotação_incrementa @ matriz_translação
        X = np.linalg.inv(matriz_transformação) @ Xd
        X = X.astype(int)
        Xd = Xd.astype(int)
        # Criar um filtro para remover os pontos que não estão na imagem
        filtro = (X[0,:]>=0)&(X[0,:]<image_.shape[0])&(X[1,:]>=0)&(X[1,:]<image_.shape[1])
        Xd = Xd[:,filtro]
        X = X[:,filtro]
        # Atribuir os valores da imagem original para a imagem transformada
        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break
        elif cv.waitKey(1) == ord('a'):
            matriz_rotação_incrementa = matriz_rotação @ matriz_rotação_incrementa  
        elif cv.waitKey(1) == ord('d'):
            matriz_rotação_incrementa = np.linalg.inv(matriz_rotação) @ matriz_rotação_incrementa
        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)
        
    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    run()