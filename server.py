import socket
import threading
import pickle
import time
import random
from models import Pojazd, Ksiazka, Kot

# Konfiguracja
HOST = '127.0.0.1'
PORT = 65432
MAX_CLIENTS = 3  # Limit klientów
current_clients = 0
lock = threading.Lock()

# Tworzenie mapy obiektów (wymóg: 3 klasy po 4 obiekty)
obiekty_mapa = {}
for i in range(1, 5):
    obiekty_mapa[f"Pojazd_{i}"] = Pojazd(f"Marka_{i}", 2010 + i)
    obiekty_mapa[f"Ksiazka_{i}"] = Ksiazka(f"Tytul_{i}", f"Autor_{i}")
    obiekty_mapa[f"Kot_{i}"] = Kot(f"Imie_{i}", f"Rasa_{i}")

def handle_client(conn, addr):
    global current_clients
    try:
        # 1. Odbierz ID klienta
        client_id = conn.recv(1024).decode()
        
        with lock:
            if current_clients >= MAX_CLIENTS:
                print(f"[REJECT] Klient {client_id} odrzucony (limit: {MAX_CLIENTS})")
                conn.sendall("REFUSED".encode())
                return
            else:
                current_clients += 1
                print(f"[OK] Rejestracja klienta ID: {client_id}. Aktualnie: {current_clients}")
                conn.sendall("OK".encode())

        # 2. Pętla obsługi żądań
        while True:
            # Symulacja losowego opóźnienia
            time.sleep(random.uniform(0.5, 2.0))
            
            requested_class = conn.recv(1024).decode()
            if not requested_class: break
            
            # Pobieranie obiektów danej klasy z mapy
            kolekcja = [obj for klucz, obj in obiekty_mapa.items() if klucz.startswith(requested_class)]
            
            # Jeśli nie ma obiektów, wyślij "błędny" obiekt (np. string zamiast listy)
            if not kolekcja:
                data_to_send = "BŁĄD: Nie ma takiej klasy!" 
            else:
                data_to_send = kolekcja

            # Serializacja i wysyłka
            print(f"[SEND] Przesyłam obiekty {requested_class} do Klienta {client_id}")
            conn.sendall(pickle.dumps(data_to_send))

    finally:
        with lock:
            current_clients -= 1
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Serwer wystartował na {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()