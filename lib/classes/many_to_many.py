class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if type(title) is str and len(title) > 0 and hasattr(self, 'title') == False:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = []
        if not isinstance(player, Player):
            raise Exception
        for result in Result.all:
            if result.player == player and result.game == self:
                scores.append(result.score)
        return sum(scores) / len(scores)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @classmethod
    def highest_scored(cls, game):
        if not isinstance(game, Game):
            raise Exception
        if len([result for result in Result.all if result.game == game]) == 0:
            return None
        game_players = [player for player in cls.all if player.played_game(game)]
        high_score = 0
        high_player = None
        for player in game_players:
            average = game.average_score(player)
            if  average > high_score:
                high_player = player
                high_score = game.average_score(player)
        return high_player

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) is str and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_games = set([result.game for result in Result.all if result.player == self])
        return list(unique_games)

    def played_game(self, game):
        if not isinstance(game, Game):
            raise Exception
        for result in Result.all:
            if result.game == game and result.player == self:
                return True
        return False

    def num_times_played(self, game):
        count = 0
        if not isinstance(game, Game):
            raise Exception
        for result in Result.all:
            if result.game == game and result.player == self:
                count += 1
        return count
    

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if type(score) is int and 1 <= score <= 5000 and hasattr(self, 'score') == False:
            self._score = score