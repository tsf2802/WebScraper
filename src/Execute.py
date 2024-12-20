import time
from PokemonCenter import PokemonCenter
from DiscordNotify import DiscordNotify
import json

def main():
    # Load configuration
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    discord_notifier = DiscordNotify(config["discord_webhook"])
    pokemon_center_monitor = PokemonCenter()

    while True:
        updates = pokemon_center_monitor.get_product_updates()
        if "error" in updates:
            print(f"Error during monitoring: {updates['error']}")
        else:
            for product in updates:
                message = f"Product Found: {product['name']} - {product['url']}"
                #discord_notifier.send_message(message)
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    main()
