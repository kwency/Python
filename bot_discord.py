import discord
from classe import CommandHistory
from discord.ext import commands


intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

# Créer une instance de CommandHistory pour stocker l'historique des commandes
command_history = CommandHistory()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!"):
        # Ajouter la commande dans l'historique
        user_id = str(message.author.id)
        command_name = message.content[1:]
        command_history.add_command(user_id, command_name)

        # Exécuter la commande
        await client.process_commands(message)


@client.command()
async def last_command(ctx):
    # Obtenir la dernière commande de l'utilisateur
    user_id = str(ctx.author.id)
    last_command = command_history.get_last_command(user_id)
    if last_command is not None:
        await ctx.send(f"ta derniere commande est: {last_command}")
    else:
        await ctx.send("pas de commandes trouvé dans ton historique.")


@client.command()
async def all_commands(ctx):
    # Obtenir toutes les commandes de l'utilisateur
    user_id = str(ctx.author.id)
    commands = command_history.get_all_commands(user_id)
    if len(commands) > 0:
        await ctx.send(f"Voici votre historique de commande: \n{' > '.join(commands)}")
    else:
        await ctx.send("pas de commandes dispo dans votre historique")


@client.command()
async def prev_command(ctx):
    # Obtenir la commande précédente de l'utilisateur
    user_id = str(ctx.author.id)
    prev_command = command_history.get_previous_command(user_id)
    if prev_command is not None:
        await ctx.send(f"ta commande precedente est: {prev_command}")
    else:
        await ctx.send("pas de commandes precedente dans ton historique.")


@client.command()
async def next_command(ctx):
    # Obtenir la commande suivante de l'utilisateur
    user_id = str(ctx.author.id)
    next_command = command_history.get_next_command(user_id)
    if next_command is not None:
        await ctx.send(f"ta prochaine commande est: {next_command}")
    else:
        await ctx.send("il n'y a pas de commandes trouvés dans ton historique.")


@client.command()
async def clear_history(ctx):
    # Effacer l'historique de l'utilisateur
    user_id = str(ctx.author.id)
    command_history.clear_history(user_id)
    await ctx.send("ton historique de commande a été nettoyer.")


@client.command()
async def ban(ctx, user: discord.User, reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


@client.command()
async def unban(ctx, user, reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    # Ici on sait que lutilisateur na pas ete trouvé
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


@client.command()
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} à été kick.")


@client.command()
async def clears(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()

client.run(
    "MTA5MTI2NDI0MzM2NzY5MDMyMQ.GvP3aY.QeHypvJWTIGyFAinaGCchtItkj0EiUVckWDCPM")
