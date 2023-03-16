import numpy as np
import cv2 as cv

#função para rotacionar a imagem para a esquerda ou direita
def rotate_image(matriz_imagem):

    T = np.array([[1, 0, -150], [0, 1, -150], [0, 0,1]])
    R = np.array([[0.7, -0.7, 0], [0.7, 0.7, 0], [0, 0,1]])
    matriz_imagem = np.linalg.inv(T)@R@T@matriz_imagem
    matriz_imagem = matriz_imagem.astype(int)
    return matriz_imagem
   

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!

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

        # Aqui, você pode fazer qualquer coisa com a imagem!
        # Por exemplo, podemos inverter as cores:
        
        
        
            
        
        image = rotate_image(image)



        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    run()
