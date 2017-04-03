

def travel_Main_Decision_Tree(Dec_Tree):
    '''
    TODO: SHOULD READ QUESTIUON THEN PROCEED LEFT OR RIGHT
    '''
    (left_tree, right_tree) = read_Dec_tree(Dec_Tree)

    if left_tree is False:  # catchi if Dec_Tree is actually a Leaf
        # TODO do leaf instruction
        read_Dec_leaf_instruction(right_tree)
        pass
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
    if question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    elif question == "1":
        pass

    return (left_yes, right_yes)


def read_Dec_leaf_instruction(leaf_val):
    if leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

    elif leaf_val == "1":
        pass

#########################################################


def fetch_oldest_card(player):
    # TODO might need to intergrate allowed cards
    maxi = 0
    card_index = 0
    for card in player.hand:
        if card.old_val > maxi and not card.color == "w":
            maxi = card.old_val
            maxi_index = card_index
        card_index += 1

    return maxi_index  # returns the oldest cards index in players hand


def check_possible_winner(board, player, players):
    possible_winners = []

    # grab a list of possible_winners (players with
    # hands smaller than 2)
    for player in players:
        if len(player.hand) < 2:
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
    hate_list = fetch_hate_priority(possible_winners)

    # TODO put meanest playable attack card on likely winning
    # most hated player Priority on using wild 4

    # TODO selection = choosecardaifunction()

    play_card(board, player, selection)


def play_card(board, player, selected=0):
    player.play_card(board, selected)
    pass


def fetch_hate_priority(players):
    # TODO
    for player in players:
        pass
    pass


def do_nothing():
    pass

#########################################################
