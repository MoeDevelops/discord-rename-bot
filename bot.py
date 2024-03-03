from discord import Client, Intents, Interaction, Member, app_commands

intents: Intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
tree = app_commands.CommandTree(client)


def start(token: str):
    client.run(token)

@client.event
async def on_ready():
    await tree.sync()
    print("Commands got synced!")

@tree.command(name="rename", description="Renames a user")
async def rename(interaction: Interaction, user: Member, new_name: str):
    print(f"Renaming '{user.nick}' ('{user.name}') to '{new_name}'")

    if (len(new_name) > 32):
        await interaction.response.send_message("New name is too long")

    await user.edit(nick=new_name)
    await interaction.response.send_message("User renamed successfully")