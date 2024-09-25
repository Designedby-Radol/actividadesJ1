equipos = []

def add_team(team_name):
    equipos.append([team_name, [], [], []])  # Initialize team with empty players, coaches, and plantel lists
    return equipos

def add_player(team_name, player_info):
    for team in equipos:
        if team[0] == team_name:
            team[1].append(player_info)  # Add player info to the team's players list
            break
    return equipos

def add_coach(team_name, coach_info):
    for team in equipos:
        if team[0] == team_name:
            team[2].append(coach_info)  # Add coach info to the team's coaches list
            break
    return equipos

# Example usage:
while True:
    print("1. Add team")
    print("2. Add player to team")
    print("3. Add coach to team")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        team_name = input("Enter team name: ")
        equipos = add_team(team_name)
        print("Equipos:", [team[0] for team in equipos])

    elif choice == "2":
        team_name = input("Enter team name: ")
        player_name = input("Enter player's name: ")
        player_position = input("Enter player's position: ")
        player_number = input("Enter player's number: ")
        player_info = [player_name, player_position, player_number]
        equipos = add_player(team_name, player_info)
        print("Equipos:", [team[0] for team in equipos])
        for team in equipos:
            print(f"Equipo {team[0]}:")
            for player in team[1]:
                print(f"  {player[0]} - {player[1]} ({player[2]})")

    elif choice == "3":
        team_name = input("Enter team name: ")
        coach_name = input("Enter coach's name: ")
        coach_position = input("Enter coach's position: ")
        coach_info = [coach_name, coach_position]
        equipos = add_coach(team_name, coach_info)
        print("Equipos:", [team[0] for team in equipos])
        for team in equipos:
            print(f"Equipo {team[0]}:")
            for coach in team[2]:
                print(f"  {coach[0]} - {coach[1]}")

    elif choice == "4":
        break

    else:
        print("Invalid option. Try again!")