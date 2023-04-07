# Zadanie 1: Konfiguracja oprogramowania.
## Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?
Zdecydowałam się aby wziąć udział w tym challenge'u, ponieważ chciałabym zapoznać się z tematyką testowania automatycznego. Mam nadzieję znaleźć pierwszą pracę w IT i być może będzie to obszar, który będzie tym jedynym. Jestem zmotywowana tym, że w tym wyzwaniu będzie wiele praktycznych zadań, które poprzez robienie ich pomogą mi zdobyć doświadczenie i poszerzyć portfolio w CV, które jest tak bardzo potrzebne do znalezienia pracy w IT.

## Podzadanie 4*: Zadanie dla chętnych.
Quiz PURPUROWY http://getistqb.com/#quizzes
Wynik: 
UDZIELONO ODPOWIEDZI DOBRZE NA 10 Z 14

# ZADANIE 2: selektory
Elementy na stronie wraz z przykładami selektorów:

### Examples 

- scouts_panel_title_xpath
```
//*[@id="__next"]/form/div/div[1]/h5
//h5[contains(@class,"MuiTypography-h5")]
//child::div/h5
```
- login_field_xpath
```
//*[@id="login"]
//input[@name="login"]
//child::div/input[@name="login"]
```
- password_field_xpath
```
//*[@id="password"]
//input[@name="password"]
//child::div//input [@type="password"]
```
- remaind_password_hyperlink_xpath
```
//*[@id="__next"]/form/div/div[1]/a
//a [text()="Remind password"]
//a[contains(text(),"password")]
```
- listbox_language_xpath
```
//*[@id="__next"]/form/div/div[2]/div/div
//div[@role="button"]
//div[text()="English"]
```
- sign_in_button_xpath
```
//*[@id="__next"]/form/div/div[2]/button
//button[@type="submit"]
//child::div/button
```