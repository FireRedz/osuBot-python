import asyncio
import channelCommands

async def parseCommand(msg, commandList):
    for command in commandList:
        if command in msg:
            return command

    return 'default'

async def chHandle(client, message, user, channel):
    commands = {
        'default' : channelCommands.default
    }

    currentCommand = await parseCommand(message, commands.keys())
    commandRunner = commands[currentCommand]
    # run command
    tempRun = await commandRunner.run(client, message, user, channel)

    if tempRun is not None:
        print(tempRun)