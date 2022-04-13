# exel
## Tworzenie srodowiska pracy
python -m venv .venv
## Aktywowanie srodowiska pracy (.venv)
.venv\Scripts\activate.bat # zamykanie do zamkniętego środowiska

# Jesli instalujesz jakis nowy pakiet uzyj komendy ponizej aby dodac, 
# pakiet do requirements.txt aby inni mogli latwo zainstalowac wszystkie potrzebne pakiety.
 pip freeze > requirements.txt  
# Aby zainstalowac.
pip install -r requirements.txt