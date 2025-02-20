import discord
from discord.ext import commands
import logging

# Konfiguriere das Logging
logging.basicConfig(level=logging.INFO)

# Erstelle eine Instanz des Bots
bot = commands.Bot(command_prefix="!")  # Ersetze das mit deinem gewünschten Prefix

@bot.event
async def on_ready():
    logging.info(f"Bot ist eingeloggt als: {bot.user.name}")

# Führe den Bot mit deinem Token aus
bot.run("MTM0MDA1MzQxNjgwOTk5MjMzMg.G6NHO9.pMlw2ITYV2rL3KJWg6E9m6URhblDYWs899Yhso")  # Ersetze mit deinem Bot-Token
