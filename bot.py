from FaucetCryptoBot import FaucetCryptoBot

def faucet_bot():

    bot = FaucetCryptoBot()
    while True:
        try:
            bot.login_handler()
            bot.get_user_balance()
            bot.get_user_level()
            bot.get_current_coin_rate()
            bot.get_main_reward()
            bot.get_ptc_ads()
            bot.get_shortlink_ads()
            # bot.get_achievements()
            bot.sleep(10)

        except Exception as e:
            bot.error_handler(e)
            bot.sleep(1)
        except KeyboardInterrupt:
            bot.quit()


if __name__ == "__main__":

    faucet_bot()
