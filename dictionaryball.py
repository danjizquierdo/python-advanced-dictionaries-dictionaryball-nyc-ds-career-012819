game_dictionary = {
    "home": {
        "team_name":"Brooklyn Nets",
        "colors": ["Black", "White"],
        "players": {
            "Alan Anderson": {
                "number":0,
                "shoe":16,
                "points":22,
                "rebounds":12,
                "assists":12,
                "steals":3,
                "blocks":1,
                "slam_dunks":1
               },
            "Reggie Evans": {
                "number":30,
                "shoe":14,
                "points":12,
                "rebounds":12,
                "assists":12,
                "steals":12,
                "blocks":12,
                "slam_dunks":7
                },
            "Brook Lopez": {
                "number":11,
                "shoe":17,
                "points":17,
                "rebounds":19,
                "assists":10,
                "steals":3,
                "blocks":1,
                "slam_dunks":15
                },
            "Mason Plumlee": {
                "number":1,
                "shoe":19,
                "points":26,
                "rebounds":12,
                "assists":6,
                "steals":3,
                "blocks":8,
                "slam_dunks":5
                },
            "Jason Terry": {
                "number":31,
                "shoe":15,
                "points":19,
                "rebounds":2,
                "assists":2,
                "steals":4,
                "blocks":11,
                "slam_dunks":1
                }
        }
    },
    "away": {
        "team_name":"Charlotte Hornets",
        "colors":["Turquoise","Purple"],
        "players": {
            "Jeff Adrian": {
                "number":4,
                "shoe":18,
                "points":10,
                "rebounds":1,
                "assists":1,
                "steals":2,
                "blocks":7,
                "slam_dunks":2
                },
        "Bismak Biyombo": {
                "number":0,
                "shoe":16,
                "points":12,
                "rebounds":4,
                "assists":7,
                "steals":7,
                "blocks":15,
                "slam_dunks":10
                },
            "DaSagna Diop": {
                "number":2,
                "shoe":14,
                "points":24,
                "rebounds":12,
                "assists":12,
                "steals":4,
                "blocks":5,
                "slam_dunks":5
                },
            "Ben Gordon": {
                "number":8,
                "shoe":15,
                "points":33,
                "rebounds":3,
                "assists":2,
                "steals":1,
                "blocks":1,
                "slam_dunks":0
                },
            "Brendan Haywood": {
                "number":33,
                "shoe":15,
                "points":6,
                "rebounds":12,
                "assists":12,
                "steals":22,
                "blocks":5,
                "slam_dunks":12
                    }
        }
    }
}


def game_dict():
    return game_dictionary

def num_points_scored(name):
    for team in game_dict():
        if name in game_dict()[team]['players'].keys():
            return game_dict()[team]['players'][name]['points']
    return None

print(num_points_scored('Ben Gordon'))

def shoe_size(name):
    for team in game_dict():
        if name in game_dict()[team]['players'].keys():
            return game_dict()[team]['players'][name]['shoe']
    return None
print(shoe_size('Brendan Haywood'))

def team_colors(name):
    for team in game_dict():
        if name in game_dict()[team].values():
            return game_dict()[team]['colors']
    return None
print(team_colors('Brooklyn Nets'))

def team_names():
    team_name=[]
    for team in game_dict():
        team_name.append(game_dict()[team]['team_name'])
    return team_name
print(team_names())

def player_numbers(team_name):
    numbers=[]
    for team in game_dict():
        for player in game_dict()[team]['players']:
            numbers.append(game_dict()[team]['players'][player]['number'])
    return numbers
print(player_numbers('Brooklyn Nets'))

def player_stats(name):
    for team in game_dict():
        if name in game_dict()[team]['players'].keys():
            return game_dict()[team]['players'][name]
    return None
print (player_stats('Jeff Adrian'))

def big_shoe_rebounds():
    max=0
    big_shoe=[]
    rebounds=0
    for team in game_dict():
        for player in game_dict()[team]['players']:
            if game_dict()[team]['players'][player]['shoe']>max:
                big_shoe=[player]
                max=game_dict()[team]['players'][player]['shoe']
                rebound=game_dict()[team]['players'][player]['rebounds']
            elif game_dict()[team]['players'][player]['shoe']==max:
                big_shoe.append(player)
    return rebound
print(big_shoe_rebounds())

def good_practices():
    for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
            import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list?
        # When would the following line of code break?
        for item in data:
            print(item)
