from gtts import gTTS

def main():
    text = input("Ingrese el texto que desea convertir a voz: ")
    tts = gTTS(text, lang='es-us')
    tts.save('audio.mp3')
    print("Archivo creado y guardado como audio.mp3")

if __name__ == '__main__':
    main()
