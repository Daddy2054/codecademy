const team = {
    _players: [
      {
        firstName: 'David',
        lastName: 'Baxes',
        age: 11
      },
      {
        firstName: 'John',
        lastName: 'Baxtin',
        age: 12
      },
      {
        firstName: 'Martin',
        lastName: 'Golod',
        age: 13
      }
    ],
    _games: [
        {
            opponent: 'Tacos',
            teamPoints: 39,
            opponentPoints: 27

        },
        {
            opponent: 'Mares',
            teamPoints: 29,
            opponentPoints: 17

        },
        {
            opponent: 'Locos',
            teamPoints: 41,
            opponentPoints: 37

        },
    ],
    get games() {
      return this._games;
    },
    get players() {
      return this._players;
    },
    addPlayer(firstName, lastName, age) {
      let newPlayer = {
        firstName: firstName,
        lastName: lastName,
        age: age,
      };
      this.players.push(newPlayer);  /// ?????? underscore or not
    },
    addGame(opp, tPts, oppPts)  {
      let newGame = {
        opponent: opp,
        teamPoints: tPts,
        opponentPoints: oppPts,
    };
      this.games.push(newGame);
  },

  };
  team.addPlayer('Steph', 'Curry', 28);
  team.addPlayer('Lisa', 'Leslie', 44);
  console.log(team.players);
  team.addGame('Fresno', 23,32);
  team.addGame('MyLove', 14,35);  
  team.addGame('Phils', 33,22);
  console.log(team.games);