import os

# Importe as funções de cada módulo específico
from documents_convert import *
from images_convert import *
from videos_convert import *
from samples_convert import *

def show_menu():
    print("Selecione a categoria:")
    print("1. Documentos")
    print("2. Imagens")
    print("3. Vídeos")
    print("4. Áudio")
    print("5. Sair")

def main():
    while True:
        show_menu()
        category_option = input("Digite o número da categoria desejada: ")

        if category_option == "1":
            document_conversion_menu()
        elif category_option == "2":
            image_conversion_menu()
        elif category_option == "3":
            video_conversion_menu()
        elif category_option == "4":
            audio_conversion_menu()
        elif category_option == "5":
            print("Saindo. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
