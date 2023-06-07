This repo is built upon discord.py

### Requirements

* Python 3.11 or newer
* Packages: `python-dotenv` and `discord.py`
* A valid Discord bot token
* A `.env` file in the project root containing `TOKEN=´YOUR_TOKEN_HERE´`

Documentation for `discord.py` can be found at https://discordpy.readthedocs.io/en/stable/, this bot is mainly using the `discord.ext.commands` framework.

### Example 

To write a simple command:

```
@bot.command(name='CommandName')
async def _commandName(ctx):
    # Put any logic you want here
    await ctx.send('Your message')
```
