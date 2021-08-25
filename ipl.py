from pycricbuzz import Cricbuzz #pip install pycricbuzz
from json import dumps
from win10toast import ToastNotifier #pip install win10toast
from time import sleep

c = Cricbuzz()
all_match = c.matches() # returns list [value1,value2,value3]
# print(all_match)
# print(dumps(all_match,indent=4))

# For Generating Name of the Match and Match ID
for matches in all_match:
    print(f"Match Name : {matches['team1']['name']} vs {matches['team2']['name']}, Match ID : {matches['id']}")

def live_score(mid):
    try:
        while True:
            lscore = c.livescore(mid)
            batsman1_name = lscore['batting']['batsman'][0]['name']
            batsman1_runs = lscore['batting']['batsman'][0]['runs']

            batsman2_name = lscore['batting']['batsman'][1]['name']
            batsman2_runs = lscore['batting']['batsman'][1]['runs']

            bowler_name = lscore['bowling']['bowler'][0]['name']
            bowler_wickets = lscore['bowling']['bowler'][0]['wickets']
            bowler_runs = lscore['bowling']['bowler'][0]['runs']

            batting_team = lscore['batting']['team']
            batting_team_runs = lscore['batting']['score'][0]['runs']
            batting_team_wickets = lscore['batting']['score'][0]['wickets']
            
            overs = lscore['batting']['score'][0]['overs']
            # print(dumps(lscore, indent=4, sort_keys=True))
            toaster = ToastNotifier()
            toaster.show_toast('Score Notification',
                f"{batting_team}'s Score : {batting_team_runs}-{batting_team_wickets} ({overs}) \
                \n\n--- Batsman --- \
                \n{batsman1_name} : {batsman1_runs} \
                \n{batsman2_name} : {batsman2_runs} \
                \n\n--- Bowler --- \
                \n{bowler_name} : {bowler_wickets}-{bowler_runs}",duration=30)

            sleep(10)

    except KeyError:
        print('Match Not Started Yet...Please Try Again Later :)')

match_id = input('\nEnter a Match ID : ')
live_score(match_id)