import socket
import pickle
import time
import random
from models import Pojazd, Ksiazka, Kot

HOST = '127.0.0.1'
PORT = 65432

def run_client(client_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Wyślij ID i sprawdź status
        s.sendall(str(client_id).encode())
        status = s.recv(1024).decode()
        
        print(f"Klient {client_id}: Status połączenia -> {status}")
        
        if status == "OK":
            klasy_do_pytania = ["Pojazd", "Ksiazka", "Kot", "NieIstnieje"]
            for _ in range(3): # Pętla powtórzona kilka razy
                target = random.choice(klasy_do_pytania)
                print(f"Klient {client_id}: Proszę o klasę {target}")
                s.sendall(target.encode())
                
                # Odbiór danych
                raw_data = s.recv(4096)
                data = pickle.loads(raw_data)
                
                # Obsługa błędnego rzutowania i przetwarzanie strumieniowe
                if isinstance(data, list):
                    print(f"Klient {client_id} otrzymał listę:")
                    # "Strumieniowe" wypisanie (map/lambda)
                    list(map(lambda x: print(f"  ID:{client_id} -> {x}"), data))
                else:
                    print(f"Klient {client_id} ERROR: Otrzymano nieprawidłowy typ danych (Błąd rzutowania)!")

if __name__ == "__main__":
    # Uruchomienie z losowym ID
    run_client(random.randint(100, 999))