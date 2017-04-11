import AI_card_logic
import card_logic
import random


def get_rand_type():
    """
    Funciton that grabs a random card type that is used within PY-UNO.

    O(15) = O(1)
    """
    card_type = ["p", "s", "r", "c", "d", "0",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return random.choice(card_type)


def get_rand_color():
    """
    Funciton that grabs a random card color that is used within PY-UNO.

    O(4) = O(1)
    """
    colors_name = ["b", "r", "g", "y"]
    return random.choice(colors_name)


def play_win(board, deck, player, players):
    """
    O(n) runtime
    """
    (max_hate, hate_player) = fetch_hate_priority(
        player, players)  # O(n)
    target = hate_player

    # if no color was selected set it to most common_color
    selected_color = fetch_most_common_color(player)  # O(n)`

    card_index = 0
    for card in player.hand:  # O(n)
        if card.color == "w":  # skip wild cards
            player.play_card(board, card_index)

            # figure out what do within the game from AI played card
            AI_card_logic.AI_card_played_type(
                board, deck, player, players, target, selected_color)  # O(1) or recuse Main_Decision_Tree

        card_index += 1

    # if one last non wild card remains
    if len(player.hand) == 1:
        player.play_card(board, 0)

        # figure out what do within the game from AI played card
        AI_card_logic.AI_card_played_type(
            board, deck, player, players)  # O(n) or recuse Main_Decision_Tree
    else:
        board.color = get_rand_color()


def fetch_most_common_color(player):
    """
    Returns the most common color in a players hand.

    O(n) runtime where n is the size of the players hand
    """
    color_dict = dict()
    for card in player.hand:  # O(n)

        if card.color == "w":
            continue

        try:
            color_dict[card.color] = color_dict[card.color] + 1
        except KeyError:
            color_dict[card.color] = 1

    if color_dict == {}:  # if no colors were prefered pick a random color
        return get_rand_color()

    return max(color_dict, key=color_dict.get)  # O(4) only 4 colors


def fetch_most_common_color_playable(board, player):
    """
    Returns the most common color in a players hand that is also playable.

    O(n) runtime where n is the size of the players hand
    """
    color_dict = dict()

    allowed_cards = card_logic.card_allowed(board, player)  # O(n)
    for i in allowed_cards:  # O(n)
        allowed_card = player.hand[i]

        if allowed_card.color == "w":  # skip wild cards
            continue

        try:
            color_dict[allowed_card.color] = 0
        except KeyError:
            color_dict[allowed_card.color] = 0

    for card in player.hand:  # O(n)
        if card.color in color_dict.keys():
            color_dict[card.color] += 1

    if color_dict == {}:  # if no colors were prefered pick a random color
        return get_rand_color()

    return max(color_dict, key=color_dict.get)  # O(4) only 4 colors


def fetch_most_common_type(player):
    """
    Returns the most common card type from a players hand.

    O(n) runtime where n is the size of the players hand
    """
    type_dict = dict()
    for card in player.hand:  # O(n)
        try:
            type_dict[card.type] = type_dict[card.type] + 1
        except KeyError:
            type_dict[card.type] = 1
    max_type = max(type_dict, key=type_dict.get)  # worst O(15) all card types
    if len(max_type) > 1:
        max_type = max_type[0]
    return max_type


def fetch_most_common_type_playable(board, player):
    """
    Returns the most common card type from a players hand that is also
    playable.

    O(n) runtime where n is the size of the players hand
    """
    type_dict = dict()

    allowed_cards = card_logic.card_allowed(board, player)
    for i in allowed_cards:  # O(n)
        allowed_card = player.hand[i]

        try:
            type_dict[allowed_card.type] = 0
        except KeyError:
            type_dict[allowed_card.type] = 0

    for card in player.hand:  # O(n)
        if card.type in type_dict.keys():
            type_dict[card.type] += 1

    return max(type_dict, key=type_dict.get)  # worst O(15) all card types


def fetch_oldest_card(board, player):
    """
    Returns the oldest playable card card's index in players hand.

    O(n) runtime where n is the size of the players hand
    """

    card_index = 0
    maxi = 0
    maxi_index = 0
    playable_indexes = card_logic.card_allowed(board, player)  # O(n)
    for card in player.hand:  # O(n)
        if card.old_val >= maxi and not card.color == "w" and card_index in playable_indexes:
            maxi = card.old_val
            maxi_index = card_index
        card_index += 1

    return (maxi, maxi_index)


def fetch_possible_winner(board, AI_player, players):
    """
    Checks to see if any posible winners are on the current board state
    eg: someone with only 1 card. If so return a tuple containing Logic
    True and a list of possible_winners. If no possible_winners are found
    it returns logical false and None in a tuple.

    Returns: (True or false, possible_winners)

    O(n) runtime where n is the length of players
    """
    possible_winners = []

    # grab a list of possible_winners (players with
    # hands smaller than 2)
    for player in players:  # O(n)
        if len(player.hand) < 2 and not player.skip:
            if player == AI_player:  # skip ownself
                pass
            else:
                possible_winners.append(player)

    # return bool value if there is possible winners or not
    # also return the list of possible winners for later use
    # in stop_winners
    if len(possible_winners) < 1:
        return (False, None)
    else:
        return (True, possible_winners)


def stop_winners(board, deck, player, players, possible_winner):
    """
    O(n) runtime
    """
    # TODO put meanest playable attack card on likely winning
    # most hated player Priority on using wild 4

    hate_cards = fetch_hate_cards(board, player)  # O(n)

    player.play_card(board, hate_cards[0][1])
    # figure out what do within the game from AI played card
    AI_card_logic.AI_card_played_type(
        board, deck, player, players, possible_winner)  # O(n)


def fetch_hate_cards(board, player):
    """
    Returns a list of all the cards that are hateable that are playable.
    Returns both the card itself and its index in the players hand

    O(n) runtime where n is the size of the players hand
    """
    hate_cards = []
    card_index = 0
    maxi = 0
    maxi_index = 0

    playable_indexes = card_logic.card_allowed(board, player)  # O(n)
    for card in player.hand:  # O(n)
        if card.type in ["d", "s", "p"] and card_index in playable_indexes:
            hate_cards.append((card, card_index))
        card_index += 1

    return hate_cards


def fetch_hate_priority(player, players):
    """
    Returns the highest hate value that player has set on any of the
    players in the game.

    O(n) runtime where n is the length of players
    """
    max_hate = 0
    hate_player = None

    for h_player in players:   # O(n)
        if player == h_player:
            continue
        try:
            if player.hatval[h_player] >= max_hate:
                max_hate = player.hatval[h_player]
                hate_player = h_player
        except KeyError:
            player.hatval[h_player] = 0

    if hate_player is None:  # catch if this the first time initilizing hateval
        max_hate = 0
        hate_player = list(player.hatval.keys())[0]

    return (max_hate, hate_player)


def do_nothing(deck, player):
    """
    Placeholder function of doing nothing (skipping a turn).

    O(1) runtime
    """
    print("NOTHING TO PLAY SKIPPING")  # TODO
    player.grab_card(deck)
    return
