Projekt: Aplikacja Klient-Serwer (Python)

Opis projektu:
Aplikacja realizuje model klient-serwer z obsługą wielowątkowości, serializacji obiektów oraz limitowaniem połączeń.

Technologie:
* Język: Python 3.x
* Biblioteki: `socket` (sieć), `threading` (wątki), `pickle` (serializacja).

Instrukcja uruchomienia:
1. Uruchom serwer: `python server.py`
2. Uruchom klientów (w oddzielnych terminalach): `python client.py`

Funkcjonalności:
* **Wielowątkowość:** Serwer obsługuje wielu klientów naraz przy użyciu biblioteki `threading`.
* **Limit połączeń:** Stała `MAX_CLIENTS` ogranicza liczbę aktywnych sesji.
* **Serializacja:** Obiekty klas `Pojazd`, `Ksiazka`, `Kot` są przesyłane za pomocą modułu `pickle`.
* **Obsługa błędów:** Klient weryfikuje typ odebranych danych (symulacja rzutowania).
