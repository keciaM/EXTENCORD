from bot_core.scripts.config import TOKEN, MUSIC_TOKEN, VERSION
from bot_core.scripts.debug_manager import LoggerManager
from bot_core.scripts.packages import PackageManager
import asyncio

# Initialize logger for both bots
log_manager = LoggerManager("discord_bot").get_logger()
music_log_manager = LoggerManager("music_discord_bot").get_logger()

async def run_bots():
    from bot_core.scripts.core import DiscordBot
    from music_addon.scripts.core import MusicExtension

    log_manager.info("Initializing main bot...")
    bot = DiscordBot(logger=log_manager)

    log_manager.info("Initializing music extension bot...")
    botmusicext = MusicExtension(logger=music_log_manager)

    try:
        await asyncio.gather(
            bot.start(TOKEN),
            botmusicext.start(MUSIC_TOKEN),
        )
    except Exception as e:
        log_manager.exception(f"Unexpected error while running bots: {e}")

# If you want to run both bots
# WARNING! In this case it MAY not show all errors and warnings in the console. Not recommended for debugging use
if __name__ == "__main__":

    log_manager.info("Initializing needed components...")
    manager = PackageManager(logger=log_manager)
    manager.check_and_install_packages()
    
    log_manager.info("Successfully loaded all packages...")
    asyncio.run(run_bots())
    log_manager.info("Bots shutdown completed.")

# If you want to run only the main bot
# if __name__ == "__main__":
#     bot = DiscordBot(logger=log_manager)
#     bot.run(TOKEN)

# If you want to run only the music bot
# if __name__ == "__main__":
#     botmusicext = DiscordMusicExt(logger=log_manager)
#     botmusicext.run(MUSIC_TOKEN)
