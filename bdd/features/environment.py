from selenium import webdriver

# funcção a ser utilizada antes dos casos de teste
def before_all(context):
    # print('acho que chegou aqui primeiro')
    context.web = webdriver.Chrome()

def after_step(context, step):
    pass

def after_all(context):
    context.web.quit()
