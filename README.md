# clipboard_server.py

A simple Python HTTP server that receives clipboard text from an iPhone Shortcut via POST and copies it to the Linux system clipboard using xclip, wl-copy, or xsel.

iPhone Shortcut:  
- Method: POST  
- URL: http://<linux_ip>:5000/set  
- Request Body: Form  
- Key: text  
- Value: Clipboard

---

clipboard_server.py — простой Python HTTP-сервер, который принимает текст буфера обмена с iPhone через POST и вставляет в системный буфер Linux с помощью xclip, wl-copy или xsel.

Ярлык на iPhone:  
- Метод: POST  
- URL: http://<linux_ip>:5000/set  
- Тело запроса: Форма  
- Ключ: text  
- Значение: Буфер обмена
