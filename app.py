import re

def simple_calculator():
    print("Prosty kalkulator - obsługiwane operacje: +, -, *, /")
    print("Wpisz 'exit', aby zakończyć.")

    while True:
        try:
            # Pobierz wyrażenie od użytkownika
            user_input = input("Wprowadź wyrażenie do obliczenia: ").strip()
            
            if user_input.lower() == 'exit':
                print("Do widzenia!")
                break

            # Walidacja wprowadzonego wyrażenia
            if not re.match(r'^[\d+\-*/().\s]+$', user_input):
                raise ValueError("Nieprawidłowe znaki w wyrażeniu. Użyj tylko cyfr i operatorów (+, -, *, /).")

            # Oblicz wynik
            result = eval(user_input)
            print(f"Wynik: {result}")
        except ZeroDivisionError:
            print("Błąd: Nie można dzielić przez zero.")
        except ValueError as ve:
            print(f"Błąd: {ve}")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

# Uruchom kalkulator
if __name__ == "__main__":
    simple_calculator()
