

def travel_Main_Decision_Tree(Dec_Tree):
    '''
    TODO: SHOULD READ QUESTIUON THEN PROCEED LEFT OR RIGHT
    '''
    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)

    if left_tree is False:  # catchi if Dec_Tree is actually a Leaf
        # TODO do leaf instruction
        read_Dec_leaf_instruction(right_tree)
        return
    else:
        question = Dec_Tree.question

        (left_yes, right_yes) = read_Dec_tree_question(question):

    if left_yes:
        travel_Main_Decision_Tree(left_tree)
    elif right_yes:
        travel_Main_Decision_Tree(right_tree)
    else:
        print("ERROR: didn't choose path")


def read_Dec_tree(Dec_Tree):

    try:  # check if Dec_Tree is actually is
        leaf_val = Dec_Tree.value
        return (False, leaf_val)  # return special case

    except TypeError:  # Dec_Tree is not a Leaf
        (left_tree, right_tree) = Dec_Tree.get_offshoots()
        return (left_tree, right_tree)


def read_Dec_tree_question(question):
    left_yes = False
    right_yes = False

    if question == "Is there an apparent winner?":
        (winnners_bool, winners_list) = check_possible_winner(
            board, player, players)
        if winnners_bool:
            return (True, False)
        else:
            return (False, True)

    elif question == "Can stop them winning it?":
        (winnners_bool, winners_list) = check_possible_winner(
            board, player, players)
        playable_cards = card_logic.card_allowed(board, player)

        for hand_index in playable_cards:
            possible_card = player.hand[hand_index]

            if card.type in ["p", "s", "r", "d"]:
                return (True, False)

        return (False, True)

    elif question == "Does oldest card play priority beat my hate play priority?":
        old_val = fetch_oldest_card(player)
        (hate_val, hate_player) = fetch_hate_priority(players)
        if hate_val < oldval:
            return (True, False)
        else:
            return (True, False)

    elif question == "Do I have playable cards?":
        playable_cards = card_logic.card_allowed(board, player)
        if len(playable_cards) > 0:
            return (True, False)
        else:
            return (False, True)

    elif question == "Do I multiple playable cards?":
        playable_cards = card_logic.card_allowed(board, player)
            if len(playable_cards) > 1:
                return (True, False)
            else:
                return (False, True)

    elif question == "1":
        pass

    elif question == "1":
        pass

    return (left_yes, right_yes)


def read_Dec_leaf_instruction(leaf_val):
    # TODO INCLUDE BOARD AND PLAYER
    if leaf_val == "Goto stop funct":
        stop_winners(board, player, possible_winners)
        pass

    elif leaf_val == "Play old card":
        pass

    elif leaf_val == "Play hate card":
        pass

    elif leaf_val == "Play a card":
        playable_cards = card_logic.card_allowed(board, player)
        player.play_card(board, playable_cards[0])
        pass

    elif leaf_val == "Go back up this tree":  # goes all back to the start and goes right
        (branch_left, branch_right) = player.Main_Dec.Dec_Tree.get_offshoots()
        travel_Main_Decision_Tree(branch_right)

    elif leaf_val == "1":
        pass

    elif leaf_val == "Do nothing":
        do_nothing()
        pass

#########################################################


def fetch_oldest_card(player):
    """
    Returns the oldest playable card card's index in players hand
    """

    card_index = 0
    playable_cards = card_logic.card_allowed(board, player)
    for card in player.hand:
        if card.old_val > maxi and not card.color == "w" and card_index in playable_cards:
            maxi = card.old_val
            maxi_index = card_index
        card_index += 1

    return maxi_index


def check_possible_winner(board, AI_player, players):
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
        if len(player.hand) < 2:
            if player == AI_player: # skip ownself
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


def stop_winners(board, player, possible_winners):
    # TODO
    (max_hate, hate_player) = fetch_hate_priority(possible_winners)

    # TODO put meanest playable attack card on likely winning
    # most hated player Priority on using wild 4

    # TODO selection = choosecardaifunction()


    play_card(board, player, selection)


def play_card(board, player, selected=0):
    player.play_card(board, selected)


def fetch_hate_priority(player, players):
    """
    Returns the highest hate value that player has set on any of the
    players in the game.
    """

    max_hate = 0

    for h_player in players:
        if player.hatval[h_player.name] > max_hate:
            max_hate = player.hatval[h_player.name]
            hate_player = h_player

    return (max_hate, hate_player)


def do_nothing():
    """
    Placeholder function of doing nothing (skipping a turn)
    """
    return

#########################################################
