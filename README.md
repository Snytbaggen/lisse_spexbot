This repo is built upon discord.py

Documentation: https://discordpy.readthedocs.io/en/stable/

The current implementation is using the `discord.ext.commands` framework.

To write a simple command:

```
@bot.command(name='CommandName')
async def _commandName(ctx):
    # Put any logic you want here
    await ctx.send('Your message')
```
