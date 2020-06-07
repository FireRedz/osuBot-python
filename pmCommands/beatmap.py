from utils import osuApi

async def run(client,message,user):
    try:
        tempMsg = message.split()[1]
    except:
        await client.sendPM(user, 'Give me beatmap id >:)')
        return f'Not parameter given by {user}'

    '''
        todo
        
        * add error handler on osuApi.getBeatmap
        * add ripple api (not rly used, but might be useful in the future)
        * add osu api
        * finish this function
        * its a mirror command ok
    '''
    mapData = osuApi.getBeatmap(tempMsg)
    if mapData == None:
        await client.sendPM(user, 'Failed to get beatmap information rip lol')
        return f'Failed to completed mirror command for {user}'

    await client.sendPM(user, '{} {} [{}]'.format(mapData['artist'], mapData['title'], mapData['version']))
    return f'Completed Mirror Command for {user}'