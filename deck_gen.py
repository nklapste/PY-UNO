import game_classes
from random import shuffle


def generate_cards():
    '''
    generate 1 set of all uno cards
    '''
    cards = []
    # predefined cards substrings
    colors = ["blue_", "red_", "green_", "yellow_"]
    colors_name = ["b", "r", "g", "y"]
    card_type = ["picker", "skip", "reverse", "0",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # make predefined cards
    for i in range(len(colors)):
        for ct in card_type:
            filename_str = "small_cards/" + colors[i] + ct + ".png"
            name_str = colors_name[i] + "_" + ct
            cards.append(game_classes.Card(name_str, filename_str, None))
    # make four wild pick 4
    cards.append(game_classes.Card(
        "w_d1", "small_cards/wild_pick_four.png", None))
    cards.append(game_classes.Card(
        "w_d2", "small_cards/wild_pick_four.png", None))
    cards.append(game_classes.Card(
        "w_d3", "small_cards/wild_pick_four.png", None))
    cards.append(game_classes.Card(
        "w_d4", "small_cards/wild_pick_four.png", None))
    # make four wild color
    cards.append(game_classes.Card(
        "w_c1", "small_cards/wild_color_changer.png", None))
    cards.append(game_classes.Card(
        "w_c2", "small_cards/wild_color_changer.png", None))
    cards.append(game_classes.Card(
        "w_c3", "small_cards/wild_color_changer.png", None))
    cards.append(game_classes.Card(
        "w_c4", "small_cards/wild_color_changer.png", None))

    return cards


def card_shuffler(cards):
    '''
    shufles a list of cards "randomly"
    '''
    print("\n\nSHUFFLING CARDLIST...", end="   ")
    shuffle(cards)
    print("DONE\n\n")
    print("SHUFFLED CARDLIST:\n")
    return cards


def build_deck(deckname, card_list):
    '''
    builds an uno game class deck from a list of uno game cards
    '''
    deckout = game_classes.Deck(deckname, card_list)
    print("deck generated named: ", end="")
    print(deckname)
    return deckout


def gen_rand_deck(deckname, size):
    '''
    generate random uno deck with assigned size (how many copies of one deck is
    included) and with name specified as input deckname
    '''
    cards = []
    for i in range(size):
        cards = card_shuffler(generate_cards()) + cards
        cards = card_shuffler(cards)

    return build_deck(deckname, cards)
