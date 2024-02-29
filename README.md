# Format Converter

Este repositório contém uma coleção de scripts em Python para converter diferentes formatos de mídia. Cada script realiza uma conversão específica, e os diretórios organizam os scripts por tipo de conversão.

## Conversões Disponíveis

### Documentos (`documents_convert`)

1. **`convert_txt_to_csv.py`:** Converte um arquivo de texto (TXT) para um arquivo CSV.
    ```bash
    python convert_txt_to_csv.py --input /caminho/do/seu/arquivo.txt --output /caminho/do/seu/output.csv
    ```

2. **`convert_csv_to_json.py`:** Converte um arquivo CSV para um arquivo JSON.
    ```bash
    python convert_csv_to_json.py --input /caminho/do/seu/arquivo.csv --output /caminho/do/seu/output.json
    ```

3. **`convert_xml_to_json.py`:** Converte um arquivo XML para um arquivo JSON.
    ```bash
    python convert_xml_to_json.py --input /caminho/do/seu/arquivo.xml --output /caminho/do/seu/output.json
    ```

### Imagens (`images_convert`)

4. **`convert_png_to_jpg.py`:** Converte uma imagem PNG para JPEG.
    ```bash
    python convert_png_to_jpg.py --input /caminho/do/seu/imagem.png --output /caminho/do/seu/output.jpg
    ```

5. **`convert_jpg_to_png.py`:** Converte uma imagem JPEG para PNG.
    ```bash
    python convert_jpg_to_png.py --input /caminho/do/seu/imagem.jpg --output /caminho/do/seu/output.png
    ```

6. **`convert_gif_to_jpg.py`:** Converte um GIF para JPEG.
    ```bash
    python convert_gif_to_jpg.py --input /caminho/do/seu/arquivo.gif --output /caminho/do/seu/output.jpg
    ```

7. **`convert_jpg_to_gif.py`:** Converte uma imagem JPEG para GIF.
    ```bash
    python convert_jpg_to_gif.py --input /caminho/do/seu/imagem.jpg --output /caminho/do/seu/output.gif
    ```

### Áudio (`samples_convert`)

8. **`convert_mp3_to_wav.py`:** Converte um arquivo MP3 para WAV.
    ```bash
    python convert_mp3_to_wav.py --input /caminho/do/seu/arquivo.mp3 --output /caminho/do/seu/output.wav
    ```

9. **`convert_wav_to_mp3.py`:** Converte um arquivo WAV para MP3.
    ```bash
    python convert_wav_to_mp3.py --input /caminho/do/seu/arquivo.wav --output /caminho/do/seu/output.mp3 --bitrate 192k
    ```

10. **`convert_flac_to_wav.py`:** Converte um arquivo FLAC para WAV.
    ```bash
    python convert_flac_to_wav.py --input /caminho/do/seu/arquivo.flac --output /caminho/do/seu/output.wav
    ```

11. **`convert_wav_to_flac.py`:** Converte um arquivo WAV para FLAC.
    ```bash
    python convert_wav_to_flac.py --input /caminho/do/seu/arquivo.wav --output /caminho/do/seu/output.flac
    ```

12. **`convert_mp3_to_flac.py`:** Converte um arquivo MP3 para FLAC.
    ```bash
    python convert_mp3_to_flac.py --input /caminho/do/seu/arquivo.mp3 --output /caminho/do/seu/output.flac
    ```

### Vídeos (`videos_convert`)

14. **`convert_mov_to_mp4.py`:** Converte um vídeo MOV para MP4.
    ```bash
    python convert_mov_to_mp4.py --input /caminho/do/seu/video.mov --output /caminho/do/seu/output.mp4 --bitrate 1000k --resolution 1280 720
    ```

15. **`convert_mp4_to_gif.py`:** Converte um vídeo MP4 para GIF.
    ```bash
    python convert_mp4_to_gif.py --input /caminho/do/seu/video.mp4 --output /caminho/do/seu/output.gif
    ```

16. **`convert_avi_to_mp4.py`:** Converte um vídeo AVI para MP4.
    ```bash
    python convert_avi_to_mp4.py --input /caminho/do/seu/video.avi --output /caminho/do/seu/output.mp4 --bitrate 1000k --resolution 1280 720
    ```

17. **`convert_mp4_to_wav.py`:** Converte um vídeo MP4 para WAV.
    ```bash
    python convert_mp4_to_wav.py --input /caminho/do/seu/video.mp4 --output /caminho/do/seu/output.wav
    ```

18. **`convert_wav_to_mp4.py`:** Combina um áudio WAV com um vídeo MP4.
    ```bash
    python convert_wav_to_mp4.py --audio /caminho/do/seu/audio.wav --video /caminho/do/seu/video.mp4 --output /caminho/do/seu/output.mp4 --bitrate 1000k
    ```

---

**Observações:**
- Certifique-se de ter as bibliotecas necessárias instaladas (`pip install moviepy pydub`).
- Ajuste os caminhos de entrada e saída conforme necessário.
- Alguns scripts podem precisar de ajustes dependendo dos requisitos específicos do seu projeto.
