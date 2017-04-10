import card_logic
import AI_card_logic


def fetch_most_common_color(player):
    """
    Returns the most common color in a players hand.
    """
    color_dict = dict()
    for card in player.hand:
        try:
            color_dict[card.color] = color_dict[card.color] + 1
        except KeyError:
            color_dict[card.color] = 1
    max_color = max(color_dict, key=color_dict.get)
    if len(max_color) > 1:
        max_color = max_color[0]
    return max_color


def fetch_most_common_color_playable(board, player):
    """
    Returns the most common color in a players hand that is also playable.
    """
    color_dict = dict()

    allowed_cards = card_logic.card_allowed(board, player)
    for i in allowed_cards:
        allowed_card = player.hand[i]

        try:
            color_dict[allowed_card.color] = 0
        except KeyError:
            color_dict[allowed_card.color] = 0

    for card in player.hand:
        if card.color in color_dict.keys():
            color_dict[card.color] += 1

    max_color = max(color_dict, key=color_dict.get)

    return max_color


def fetch_most_common_type(player):
    """
    Returns the most common card type from a players hand.
    """
    type_dict = dict()
    for card in player.hand:
        try:
            type_dict[card.type] = type_dict[card.type] + 1
        except KeyError:
            type_dict[card.type] = 1
    max_type = max(type_dict, key=type_dict.get)
    if len(max_type) > 1:
        max_type = max_type[0]
    return max_type


def fetch_most_common_type_playable(board, player):
    """
    Returns the most common card type from a players hand that is also
    playable.
    """
    type_dict = dict()

    allowed_cards = card_logic.card_allowed(board, player)
    for i in allowed_cards:
        allowed_card = player.hand[i]

        try:
            type_dict[allowed_card.type] = 0
        except KeyError:
            type_dict[allowed_card.type] = 0

    for card in player.hand:
        if card.type in type_dict.keys():
            type_dict[card.type] += 1

    return max(type_dict, key=type_dict.get)


def fetch_oldest_card(board, player):
    """
    Returns the oldest playable card card's index in players hand.
    """

    card_index = 0
    maxi = 0
    maxi_index = 0
    playable_indexes = card_logic.card_allowed(board, player)
    for card in player.hand:
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
    """
    possible_winners = []

    # grab a list of possible_winners (players with
    # hands smaller than 2)
    for player in players:
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


def stop_winners(board, deck, player, possible_winner):

    # TODO put meanest playable attack card on likely winning
    # most hated player Priority on using wild 4

    # TODO selection = choosecardaifunction()
    hate_cards = fetch_hate_cards(board, player)

    play_card(board, player, hate_cards[0][1])  # TODO improve

    # figure out what do within the game from AI played card
    AI_card_logic.AI_card_played_type(
        board, deck, player, None, possible_winner)


# TODO REMOVE PROPERLY
def play_card(board, player, selected=0):
    player.play_card(board, selected)


def fetch_hate_cards(board, player):
    """
    Returns a list of all the cards that are hateable that are playable.
    Returns both the card itself and its index in the players hand
    """
    hate_cards = []
    card_index = 0
    maxi = 0
    maxi_index = 0

    playable_indexes = card_logic.card_allowed(board, player)
    for card in player.hand:
        if card.type in ["d", "s", "p"] and card_index in playable_indexes:
            hate_cards.append((card, card_index))
        card_index += 1

    return hate_cards


def fetch_hate_priority(player, players):
    """
    Returns the highest hate value that player has set on any of the
    players in the game.
    """
    max_hate = 0
    hate_player = None

    for h_player in players:
        if player == h_player:
            continue
        try:
            if player.hatval[h_player.name] >= max_hate:
                max_hate = player.hatval[h_player.name]
                hate_player = h_player
        except KeyError:
            player.hatval[h_player.name] = 0
    return (max_hate, hate_player)


def do_nothing(deck, player):
    """
    Placeholder function of doing nothing (skipping a turn).
    """
    player.grab_card(deck)
    return
