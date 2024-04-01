from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import os
from PIL import Image
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
servico = Service(ChromeDriverManager().install())


def tirarPrint(link_site, tempo, name_image, tamanho_print, elemento_login, credencial_login, elemento_senha,
               credencial_senha, elemento_entrar_senha, elemento_entrar_login=''):
    """
    O programa tem como objetivo tirar prints de telas
    :param link_site: link para entrar no site
    :param tempo: tempo de esperar até carregar os valores
    :param name_image: nome dado para a imagem é importante passar o nome da Variavel meusAquivos e o elemento da lista EX: meusAquivos[0] que é 'img01.png'
    :param tamanho_print: Tupla com os valores (X, Y, FX, FY) FX e FY é o tamanho de altura e largura
    :param elemento_login: elemento que aparece parace para fazer o login (XPATH)
    :param credencial_login: O login para entrar EX: Shabalaba@asdas.com
    :param elemento_senha: elemento que aparece parace para fazer a senha (XPATH)
    :param credencial_senha: A senha para entrar EX: Xisfjsh213
    :param elemento_entrar_senha: Botão para entrar na pargina (XPATH)
    :param elemento_entrar_login: Se OUVER o botão para logar antes da senha (XPATH)
    """
    navegador.get(link_site)
    # Tempo de espera para carregar a informações da tela
    time.sleep(3)
    # Se precisar de login na tela
    # Usando XPATH, mas pode mudar
    if len(navegador.find_elements(By.XPATH, elemento_login)) == 1:
        # login
        navegador.find_element(By.XPATH, elemento_login).send_keys(credencial_login)
        if len(elemento_entrar_login) >= 1:
            print('tem valor')
            navegador.find_element(By.XPATH, elemento_entrar_login).click()

    # precisa colocar a senhar
    if len(navegador.find_elements(By.XPATH, elemento_senha)) == 1:
        # senha
        navegador.find_element(By.XPATH, elemento_senha).send_keys(credencial_senha)
        # botão para logar
        navegador.find_element(By.XPATH, elemento_entrar_senha).click()

    time.sleep(tempo)
    # Screenshot e Edição da imagsem
    screnshot(name=name_image, tamanho=tamanho_print)


def printSecundario(elemento_secundario, tempo, name_image, tamanho_print, elemento_login, credencial_login,
                    elemento_senha, credencial_senha, elemento_entrar_senha, elemento_entrar_login=''):
    """
    Esse programa tira print de elementos secundarios que estão na mesma tela mas precisa de CLICAR para entrar e ver os parametros
    :param elemento_secundario: Elemento dentro de uma mesma tela para tirar print
    :param tempo: tempo de esperar até carregar os valores
    :param name_image: nome dado para a imagem é importante passar o nome da Variavel meusAquivos e o elemento da lista EX: meusAquivos[0] que é 'img01.png'
    :param tamanho_print: Tupla com os valores (X, Y, FX, FY) FX e FY é o tamanho de altura e largura
    :param elemento_login: elemento que aparece parace para fazer o login (ID)
    :param credencial_login: O login para entrar EX: Shabalaba (ID)
    :param elemento_senha: elemento que aparece parace para fazer a senha (XPATH)
    :param credencial_senha: A senha para entrar EX: Xisfjsh213 (XPATH)
    :param elemento_entrar_senha: Botão para entrar na pargina (XPATH)
    :param elemento_entrar_login: Se OUVER o botão para logar antes da senha (XPATH)
    """

    navegador.find_element(By.XPATH, elemento_secundario).click()
    time.sleep(3)
    # Se precisar de login na tela
    # Usando XPATH, mas pode mudar
    if len(navegador.find_elements(By.XPATH, elemento_login)) == 1:
        # login
        navegador.find_element(By.XPATH, elemento_login).send_keys(credencial_login)
        if len(elemento_entrar_login) >= 1:
            print('tem valor')
            navegador.find_element(By.XPATH, elemento_entrar_login).click()

    # precisa colocar a senhar
    time.sleep(2)
    if len(navegador.find_elements(By.XPATH, elemento_senha)) == 1:
        # senha
        navegador.find_element(By.XPATH, elemento_senha).send_keys(credencial_senha)
        # botão para logar
        navegador.find_element(By.XPATH, elemento_entrar_senha).click()

    time.sleep(tempo)
    screnshot(name=name_image, tamanho=tamanho_print)


# Função para tirar print
def screnshot(name, tamanho):
    navegador.save_screenshot(caminhoPrint + name)
    img = Image.open(caminhoPrint + name).crop(tamanho)
    img.save(caminhoPrint + name)


def loginWhats():
    """
    Esperar o Usuario Ser o QRcode e entrar no feed do whatsap
    :return:
    """
    navegador.get(r'https://web.whatsapp.com/')
    while True:
        time.sleep(5)
        if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div')) == 1:
            time.sleep(2)
        break
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)


def salvaWhats(nome_contato_grupo):
    """
    Esse Função envia os prints para os grupos e contatos de WhatsApp
    :param nome_contato_grupo: Nome do contato ou do grupo para enviar os prints
    """

    navegador.get(r'https://web.whatsapp.com/')
    # Esperando a tela do whas aparece logo apos o QRcode
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)

    # Colocar o nome do grupo ou contato para entrar
    navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(
        nome_contato_grupo)

    # Espera para carregar as informações
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

    for elemento in meusAquivos:
        caminho_completo = os.path.abspath(f'telas/{elemento}')
        time.sleep(0.5)
        # Seleciona as Opções de envio
        navegador.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span').click()
        time.sleep(0.5)
        # Seleciona enviar Fotos e Videos
        navegador.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input').send_keys(
            caminho_completo)
        # Envia a imagem
        time.sleep(0.5)
        navegador.find_element(By.XPATH,
                               '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()


# Cria a Pasta para Armazenar as imagens
pasta = r'telas'
caminho = os.getcwd()


def criar_pasta_usuario(nome):
    if not os.path.exists(nome):
        os.makedirs(nome)
        print(f"Pasta do usuário '{nome}' criada com sucesso.")
    else:
        print(f"A pasta do usuário '{nome}' já existe.")


# chama a função criar pasta
criar_pasta_usuario(nome=pasta)
# caminho para armazenar a screenshot

caminhoPrint = caminho + '/' + pasta + '/'

# Nome dos arquivos das imagens
# é Importante de passar o a quantidade certa de imagens que vai tirar print
meusAquivos = ['img01.png', 'img02.png']

# Abrir o navegador
navegador = webdriver.Chrome(options=options, service=servico)

# Maximizar o navegador
navegador.maximize_window()

# Horarios para enviar os prints no grupo do Whats
horarios = ['14:02', '14:06']

# variavel para o primeiro login
logar = 0

while True:
    agora = dt.now().strftime('%H:%M')
    if agora in horarios:
        if logar == 0:
            loginWhats()
            tirarPrint(
                link_site='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKJshixVPp52x4Svu8txPuLbbBWbpODwFD5SGwG_fjFxxHakXTlua8NYAuOE9yNLFhLN478kYg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1123450843%3A1711321428792581&theme=mn&ddm=0',
                tempo='5',
                # É precisico selecionar em qual posição você quer salvar a imagens na lista no meusAquivos[0] <- troque o numero
                name_image=meusAquivos[0], tamanho_print=(256, 125, 1295, 584), elemento_login='identifierId',
                credencial_login='rweqrjop@gmail.com', elemento_entrar_login='//*[@id="identifierNext"]/div/button',
                elemento_senha='//*[@id="password"]/div[1]/div/div[1]/input', credencial_senha='fwohfposfo313123DF',
                elemento_entrar_senha='//*[@id="passwordNext"]/div/button')
            salvaWhats('Nome do Grupo ou Contato')
            logar += 1
        else:
            tirarPrint(
                link_site='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKJshixVPp52x4Svu8txPuLbbBWbpODwFD5SGwG_fjFxxHakXTlua8NYAuOE9yNLFhLN478kYg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1123450843%3A1711321428792581&theme=mn&ddm=0',
                tempo='5',
                # É precisico selecionar em qual posição você quer salvar a imagens na lista no meusAquivos[1] <- troque o numero
                name_image=meusAquivos[1], tamanho_print=(256, 125, 1295, 584), elemento_login='identifierId',
                credencial_login='rweqrjop@gmail.com', elemento_entrar_login='//*[@id="identifierNext"]/div/button',
                elemento_senha='//*[@id="password"]/div[1]/div/div[1]/input', credencial_senha='fwohfposfo313123DF',
                elemento_entrar_senha='//*[@id="passwordNext"]/div/button')
            salvaWhats('Nome do Grupo ou Contato')
    time.sleep(30)
