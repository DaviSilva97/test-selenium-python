from selenium import webdriver

drive = webdriver.Chrome()

drive.get("https://google.com.br") # Abre a página do google


element = drive.find_element_by_name("q") # Seleciona o input de pesquisa do google. Processo selemelhante à manipulação do DOM (Javascript)
element.click() # Click no elemento selecionado, no nosso caso o input de pesquisa
element.send_keys("tradutor") # digita o texto "tradutor" 
element.submit() # Realiza a busca