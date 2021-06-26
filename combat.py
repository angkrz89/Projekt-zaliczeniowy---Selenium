import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# dane
valid_search = "teleskop"
valid_search2 = "wiatrówka"
valid_firstname = "Regina"
valid_lastname = "Sobczak"
valid_street = "Kombatantów"
valid_street_number = "6"
valid_city = "Gdańsk"
valid_postcode = "80-464"
valid_phone_number = "22113344"

invalid_email = "adcsea.com"


# Scenariusz testowy:
# Zakupy na stronie combat.pl


class CombatShopping(unittest.TestCase):
    # Warunki wstepne:
    def setUp(self):
        # 1. Uruchomiona przegladarka
        self.driver = webdriver.Chrome()
        # Maksymalizacja okna
        self.driver.maximize_window()
        # 2. Na stronie https://www.combat.pl/
        self.driver.get("https://www.combat.pl/")
        # Włączenie implicitly wait - mechanizmu czekania na elementy max. 40 sekund
        self.driver.implicitly_wait(40)

    # Przypadek testowy 001:
    # Dokonanie zamówienia przy użyciu błędnego adresu e-mail
    def testShoppingByInvalidEmail(self):
        driver = self.driver
        # Kroki
        # 1. Zaakceptuj "ciasteczka"
        accept_btn = driver.find_element_by_id('cookie-accept')
        accept_btn.click()

        # 2. Wyszukaj "teleskop"
        search_input = driver.find_element_by_id('search')
        search_input.send_keys(valid_search)

        # 3. Wybierz model "Teleskop Celestron Perceptor Travel 50 mm"
        driver.find_element_by_xpath('//a[@title="Teleskop Celestron Perceptor Travel 50 mm"]').click()

        # 4. Dodaj go do koszyka
        add_btn = driver.find_element_by_xpath('//button[@title="Dodaj do koszyka"]')
        add_btn.click()

        # Poczekaj 5 sekund
        sleep(5)

        # 5. Wyszukaj "wiatrówka"
        search_input = driver.find_element_by_id('search')
        search_input.send_keys(valid_search2)

        # 6. Wybierz model "Karabinek Hammerli Black Force 800 Combo"
        driver.find_element_by_xpath('//a[@title="Wiatrówka Karabinek Hammerli Black Force 800 Combo..."]').click()

        # 7. Dodaj go do koszyka
        add_btn = driver.find_element_by_xpath('//button[@title="Dodaj do koszyka"]')
        add_btn.click()

        # Poczekaj 5 sekund
        sleep(5)

        # 8. Przejdź do koszyka
        basket_btn = driver.find_element_by_xpath('//a[@href="https://www.combat.pl/checkout/cart/"]')
        basket_btn.click()

        # 9. Przejdź do kasy
        driver.find_element_by_xpath('//button[@title="Przejdź do kasy"]').click()

        # Poczekaj 10 sekund
        sleep(10)

        # 10. Wpisz nieprawidłowy adres e-mail (brak znaku '@')
        email_input = driver.find_element_by_id('customer-email')
        email_input.click()
        email_input.send_keys(invalid_email)

        # 11. Wpisz imię
        imie_input = driver.find_element_by_name('firstname')
        imie_input.send_keys(valid_firstname)

        # 12. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_name('lastname')
        nazwisko_input.send_keys(valid_lastname)

        # 13. Wpisz ulicę
        street_input = driver.find_element_by_name('street[0]')
        street_input.send_keys(valid_street)

        # 14. Wpisz numer domu/lokalu
        street_number_input = driver.find_element_by_name('street[1]')
        street_number_input.send_keys(valid_street_number)

        # 15. Wpisz miasto
        city_input = driver.find_element_by_name('city')
        city_input.send_keys(valid_city)

        # 16. Wpisz kod pocztowy
        street_number_input = driver.find_element_by_name('postcode')
        street_number_input.send_keys(valid_postcode)

        # 17. Wpisz numer telefonu
        phone_number_input = driver.find_element_by_name('telephone')
        phone_number_input.send_keys(valid_phone_number)

        # 18. Wybierz sposób dostawy: Kurier - płatność przy odbiorze
        driver.find_element_by_id('label_method_flatrate_flatrate').click()

        # Scroll page down
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

        # 19. Przejdź do płatności
        driver.find_element_by_xpath('//button[@data-role="opc-continue"]')

        # Wyszukuje wszystkie błędy
        error_messages = driver.find_elements_by_css_selector('div#customer-email-error')
        # Tworzę listę WIDOCZNYCH błędów
        visible_error_notices = list()  # Pusta lista
        for error in error_messages:
            # Jeśli komunikat jest widoczny
            if error.is_displayed():
                # Dodajemy ten komunikat do listy WIDOCZNYCH
                visible_error_notices.append(error)

        # Sprawdzam, czy ta lista WIDOCNYCH komunikatów zawiera tylko jeden błąd
        assert len(visible_error_notices) == 1, "Liczba widocznych komunikatów nie zgadza się!"
        # Z wykorzystaniem unittesta
        self.assertEqual(len(visible_error_notices), 1, msg="Liczba widocznych komunikatów nie zgadza się!")
        # Sprawdzam treść błędu
        self.assertEqual(visible_error_notices[0].text,
                         "Prosimy wprowadzić poprawny adres email (np.: imie@nazwisko.com).")

        # Poczekaj 3 sekundy
        sleep(3)

    def tearDown(self):
        # Zakonczenie testu
        self.driver.quit()


# Jeśli uruchamiamy z tego pliku
if __name__ == "__main__":
    # Użyjmy metody main(), która zajmie się resztą
    unittest.main(verbosity=2)
