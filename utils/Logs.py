import utils.Utility as util

async def SendLog(bot, log_text):
    bot_log_channel = util.get_topic_channel(bot, f"{bot.user.name}콘솔")

    if not bot_log_channel:
        print("Log channel is not set.")
        return

    for guild_channels in bot_log_channel.values():
        for channel in guild_channels:
            await channel.send(log_text)
