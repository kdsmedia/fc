from colorama import init, Fore

init(autoreset=True)


def draw_banner():
    print(
        Fore.LIGHTGREEN_EX
        + """
    ___________                            __   _________                        __
    \_   _____/____   __ __  ____   ____ _/  |_ \_   ___ \___________ ________ _/  |_  ____
      |  ___) \__  \ |  |  \/ ___\_/ __ \\   __\/    \  \/\_  __ \   |  |____ \\   __\/ __ \\
      |  \__   / __ \_  |  /  \___\  ___/_|  |  \     \____|  | \/\___  |  |_\ \|  | (  \_\ )
      /___  / (____  /____/ \___  /\___  /|__|   \______  /|__|   / ____|   ___/|__|  \____/
          \/        \/           \/     \/               \/        \/    |__|

                                            Bot v2.98
                                            
                      Github: https://github.com/souravrs999/FaucetCryptoBot
     """
        + Fore.RESET
    )
