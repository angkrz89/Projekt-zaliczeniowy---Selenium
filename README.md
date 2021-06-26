# Test strony https://www.combat.pl/

Tytuł: Próba dokonania zakupów przez użytkownika używając niepoprawnego adresu e-mail.

Środowisko: Chrome wersja  91.0.4472.77, Ubuntu 20.04.2 LTS

Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zarejestrowany.

<b>Kroki:</b>

1. Wejdź na stronę "https://www.combat.pl/"
2. Zamknij „cookies”
3. Wyszukaj „teleskop”
4. Wybierz model "TTeleskop Celestron Perceptor Travel 50 mm"
5. Dodaj go do koszyka
6. Wyszukaj „wiatrówka”
7. Wybierz model "Karabinek Hammerli Black Force 800 Combo"
8. Dodaj go do koszyka
9. Przejdź do koszyka
10. Przejdź do kasy
11. Wprowadź niepoprawny e-mail
12. Wprowadź imię
13. Wprowadź nazwisko
14. Wprowadź ulicę
15. Wprowadź numer domu/lokalu
16. Wprowadź miasto
17. Wprowadź kod pocztowy
18. Wprowadź numer telefonu
19. Wybierz sposób dostawy
20. Przewiń stronę do dołu
21. Przejdź do płatności

<b>Oczekiwany rezultat:</b>

Zakupy nie powodzą się.
Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny.

Uruchomienie testu:

$ python3 combat.py

<b>Uwagi końcowe:</b>

Automatyzacja przypadku testowego (test funkcjonalny) powiodła się. Test może być wrażliwy na zmianę struktury strony z powodu konieczności stosowania długich ścieżek w lokalizatorach XPATH i CSS Selector. Ponadto mogą występować problemy przy wyszukiwaniu, gdy zmianie ulegną nazwy produktów oraz w sytuacji, gdy nie będą one dostępne.
