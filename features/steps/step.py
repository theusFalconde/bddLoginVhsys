from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


@given(u'o navegador "{navegador}"')
def step_impl(context, navegador):
    if navegador == "Chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.headless = True
        context.webdriver = webdriver.Chrome(options=options)
    if navegador == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.headless = True
        context.webdriver = webdriver.Firefox(options=options)

@given(u'a tela de login do vhsys')
def step_impl(context):
    context.webdriver.get("https://app.vhsys.com.br")

@when(u'clicado no botão entrar')
def step_impl(context):
    element = context.webdriver.find_element(By.ID, "btnLogar")
    element.click()
    time.sleep(3)

@then(u'deve apresentar a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    element = context.webdriver.find_element(By.ID, "resultadoLogar")
    assert(element.text == mensagem)
