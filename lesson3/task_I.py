class TeamStat():
    def __init__(self, name):
        self.name = name
        self.games_cnt = 0
        self.goals_cnt = 0
        self.opens_cnt = 0

    @property
    def mean_goals(self):
        return self.goals_cnt / self.games_cnt

    def __repr__(self):
        return f"{self.games_cnt}, {self.goals_cnt}, {self.opens_cnt}"


class PlayerStat():
    def __init__(self, name):
        self.name = name
        self.opens_cnt = 0
        self.goals = {}
        self.player_team = ""

    @property
    def goals_cnt(self):
        return sum(self.goals.values())

    def update_goals_stats(self, minute, team_name):
        self.goals[minute] = self.goals.get(minute, 0) + 1
        self.player_team = team_name

    def calc_mean_goals(self, team_games):
        return self.goals_cnt / team_games

    def goals_on_first(self, t):
        return sum(dict(filter(lambda x: x[0] <= t, self.goals.items())).values())

    def goals_on_last(self, t):
        return sum(dict(filter(lambda x: 91 - t <= x[0] <= 90, self.goals.items())).values())

    def __repr__(self):
        return f"{self.goals_cnt}, {self.opens_cnt}"


def play_football(data: list[str]) -> list[str]:

    teams_stats, players_stats, res = {}, {}, []

    cursor = 0
    while cursor < len(data):

        row = data[cursor]

        if '"' in row and "-" in row:  # match info
            split = row.split('"')
            team1 = split[1]
            team2 = split[3]
            goals = split[4]
            goal1, goal2 = map(int, goals.split(":"))
            total_goals = goal1 + goal2

            for team_name, team_goals in zip([team1, team2], [goal1, goal2]):
                team_stats = teams_stats.get(team_name, TeamStat(name=team_name))
                team_stats.goals_cnt += team_goals
                team_stats.games_cnt += 1
                teams_stats[team_name] = team_stats

            player_names_set = set()

            temp_cnt = 0
            fg_player, fg_player_team, fg_time = None, None, 999
            for i in range(total_goals):
                cursor += 1
                goal_info = data[cursor]

                split = goal_info.split()

                player_name = " ".join(split[:-1])
                player_names_set.add(player_name)
                goal_minute = int(split[-1][:-1])
                player_team = team1 if temp_cnt < goal1 else team2

                # is min goals?
                if goal_minute < fg_time:
                    fg_time = goal_minute
                    fg_player = player_name
                    fg_player_team = player_team

                player_stats = players_stats.get(player_name, PlayerStat(name=player_name))
                player_stats.update_goals_stats(goal_minute, player_team)
                players_stats[player_name] = player_stats

                temp_cnt += 1

            # update opens
            if fg_player and fg_player_team:
                teams_stats[fg_player_team].opens_cnt += 1
                players_stats[fg_player].opens_cnt += 1

        else:   # request
            request = data[cursor]

            if "Total goals for" in request:
                team_name = request.split('"')[-2]
                team_stats = teams_stats.get(team_name)
                if not team_stats:
                    answer = 0
                else:
                    answer = team_stats.goals_cnt

            elif "Mean goals per game for" in request:
                team_name = request.split('"')[-2].strip()
                team_stats = teams_stats.get(team_name)
                if not team_stats:
                    answer = 0
                else:
                    answer = team_stats.mean_goals

            elif "Score opens by" in request:
                by = request.split(" by ")
                if '"' in request:
                    team_name = request.split('"')[-2]
                    team_stats = teams_stats.get(team_name)
                    if not team_stats:
                        answer = 0
                    else:
                        answer = team_stats.opens_cnt
                else:
                    player_name = by[-1].strip()
                    player_stats = players_stats.get(player_name)
                    if not player_stats:
                        answer = 0
                    else:
                        answer = player_stats.opens_cnt

            elif "Total goals by" in request:
                player_name = request.split(' by ')[-1].strip()
                player_stats = players_stats.get(player_name)
                if not player_stats:
                    answer = 0
                else:
                    answer = player_stats.goals_cnt

            elif "Mean goals per game by" in request:
                player_name = request.split(' by ')[-1].strip()
                player_stats = players_stats.get(player_name)
                player_team = player_stats.player_team

                total_team_games = teams_stats.get(player_team).games_cnt

                if not player_stats:
                    answer = 0
                else:
                    answer = player_stats.goals_cnt / total_team_games

            elif "Goals on minute" in request:
                player_name = request.split(' by ')[-1].strip()
                minute = int(request.split(' by ')[0].split()[-1].strip())
                player_stats = players_stats.get(player_name)

                if not player_stats:
                    answer = 0
                else:
                    answer = player_stats.goals.get(minute, 0)

            elif "Goals on first" in request:
                player_name = request.split(' by ')[-1].strip()
                minute = int(request.split(' by ')[0].split()[-2].strip())
                player_stats = players_stats.get(player_name)

                if not player_stats:
                    answer = 0
                else:
                    answer = player_stats.goals_on_first(minute)

            elif "Goals on last" in request:
                player_name = request.split(' by ')[-1].strip()
                minute = int(request.split(' by ')[0].split()[-2].strip())
                player_stats = players_stats.get(player_name)

                if not player_stats:
                    answer = 0
                else:
                    answer = player_stats.goals_on_last(minute)
            else:
                answer = f"not processed: {request}"

            res.append(answer)
        cursor += 1

    return res


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.readlines()
    res = play_football(data)
    for item in res:
        print(item)
