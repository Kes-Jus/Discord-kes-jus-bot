from riotwatcher import LolWatcher, ApiError
import pandas as pd
api_key = 'RGAPI-bbc75bd7-4a8f-4be3-a8d0-2a6b43303966'
watcher = LolWatcher(api_key)

# golbal variables
def lol_api(username, region):
    me = watcher.summoner.by_name(region, username)
    print(me['summonerLevel'])
    my_matches = watcher.match.matchlist_by_account(region, me['accountId'])

    # fetch last match detail
    last_match = my_matches['matches'][0]
    match_detail = watcher.match.by_id(region, last_match['gameId'])
    print(match_detail)
    #print("Wins :"+match_detail['stats']['win']+", Kills :"+match_detail['stats']['kills']+", Deaths :"+match_detail['stats']['deaths'])
    """
        participants_row['champion'] = row['championId']
        participants_row['spell1'] = row['spell1Id']
        participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        participants_row['item0'] = row['stats']['item0']
        participants_row['item1'] = row['stats']['item1']
        participants.append(participants_row)
    """
lol_api('Doublelift', 'na1')


"""
@bot.command(name='rank', help='Do !!summoner <username> <region>')
async def rank(ctx, username:str):
    try:
        response = "Your Rank is : " + str(rank_api(username)['tier'] + " " + str(rank_api(username)['rank'])
    except :
        response = "Try Again"

    await ctx.send(response)


<Message id=805958334166597665
channel=<TextChannel
id=784009778615287828
name='commandes'
position=1
nsfw=False
news=False
category_id=608444765926850562> 
type=<MessageType.default: 0>
author=<Member id=575466144216121355 name='NouAr' discriminator='3693' bot=False nick=None guild=<Guild id=608444765389717506 name='kes jus' shard_id=None chunked=False member_count=71>> flags=<MessageF
lags value=0>>






<Message id=805958713735249922 channel=<TextChannel id=784009778615287828 name='commandes' position=1 nsfw=False news=False category_id=608444765926850562> type=<MessageType.default: 0> author=<
Member id=575466144216121355 name='NouAr' discriminator='3693' bot=False nick=None guild=<Guild id=608444765389717506 name='kes jus' shard_id=None chunked=False member_count=71>> flags=<MessageF
lags value=0>>

"""
