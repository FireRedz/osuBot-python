import asyncio
import mpCommands

async def parseCommand(msg, commandList):
    for command in commandList:
        if command in msg:
            return command

    return 'default'

async def pmHandle(client, message, user):
    commands = {
        'default' : mpCommands.default,
        '!bruh' : mpCommands.bruh
    }

    currentCommand = await parseCommand(message, commands.keys())
    commandRunner = commands[currentCommand]
    # run command
    tempRun = await commandRunner.run(client, message, user)

    if tempRun is not None:
        print(tempRun)