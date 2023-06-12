# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
BLOODYWATERS_LYRICS = "Meet the man in the maskMeet the man in the mask All those days and all that stays and I don't keep itI won't be here for it All those days and all that stays andI don't keep it thoughI won't be here for itYes Lord, huh Hail Mary's in the sky Bossed up, let's get buried alive Head on the throne 'cause that's where I reside (reside)Ways of the world that we won't survive Something's in the water (water)My nigga we lawless (lawless)Please move with cautionWho set the fairway? (Fairway)Damn right I need all this (all this)Yeah, Jack, I need all this, eyy Hittas acquitted with fingerprints on the GlockScreamin' we gon' make it like two-thirds of The LOXYeah yeah, yeah yeah Blah blah, he comes, blah blah Blood on my hands I'ma need hot agua You gon' meet your maker I won't say it in Patois Hope I strike a nerve like a pack of matches You might wanna bypass, this smoke ain't gas trick A prince-turned-pauper trying to do like kings do Sweating in chess games try move like kings moveYou should slow your roll before you drown in the moat He tried to channel balance but never found the remoteKillers on the prowl still juggin' off a lickStealing, with a double for his Common politics, everlasting mayhem Draw to stick you for your figures, that's how they hang man So what's your game plan, if you got one?You aimin' at passengers with a shotgun? (Woah)The aftermath is you in the scopeIt's warfare, is war fair? (No)You understand? It's probably better you don'tJust keep a dock on standby, charter a boatShip set sailing, planes departThe big picture's in motion, are you playing your part?Before the lights get dark and the curtains get closedAre you playing your role?As told by an organized criminalAnd general, get off my genitals, I got your generalHail Mary's in the skyBossed up, let's get buried aliveHead on the throne 'cause that's where I reside (reside)Ways of the world that we won't survive Something's in the water (the water)My nigga we lawless (lawless)Please move with cautionWho set the fairway? (Fairway)Damn right I need all this (all this)Yeah, Jack, I need all thisI had to be about 9 when I first had seen itLow lows pulled up outside of the Ralph'sAfter a car show at Dominguez They had a disagreement, they had to air outJust another day in Del Amo Fo' sho man down, mandoThank God I never had to knock your partner offOr be an another casualty of war, AmenThere's 4 footprints in the sand where I walk I never claimed to be a saint at all Four Russians trippin' with hollow tips And a Kalashnikov, ain't that y'all No, Soulo hoe, kept it clean Riding dirty, jury would have gave me thirty Herbie love buggin' out, hit the target blindfolded Electoral college devoted To hit the score, to write the score, that's not a metaphor Raging against the machinery, taping up the scenery You gotta keep the piece, to keep the peace Got dough, squad up and mopped the block up for a cleaning fee I don't need you to change I don't need you to change yourself (get, get away) But I've got get away (get, get away) But I've got get away from it all Be as free as you can Be as free as you can away from me I tried to be a saint like everybody else"
BIRTHDAY = ' Happy Birthday to You Happy Birthday to You Happy Birthday Dear (name) Happy Birthday to You. From good friends and true, From old friends and new, May good luck go with you, And happiness too. Alternative ending: How old are you? How old are you? How old, How old How old are you? '
TWINKLE = 'Twinkle, twinkle, little star, How I wonder what you are. Up above the world so high, Like a diamond in the sky. When the blazing sun is gone, When he nothing shines upon, Then you show your little light, Twinkle, twinkle, all the night. Then the traveller in the dark, Thanks you for your tiny spark, He could not see which way to go, If you did not twinkle so. In the dark blue sky you keep, And often through my curtains peep, For you never shut your eye, ‘Till the sun is in the sky. As your bright and tiny spark, Lights the traveller in the dark. Though I know not what you are, Twinkle, twinkle, little star. Twinkle, twinkle, little star. How I wonder what you are. Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star. How I wonder what you are. How I wonder what you are.'

# DATA - mantras
SO_HUM = 'So Hum, or Soham, is a Sanskrit mantra meaning "I am that," with "that" being the universe. According to Markoe Schieffelin, working with this mantra helps one to identify with the oneness of the universe.'
GIRA = 'It was a kind of sado-masochism. I would take the things that were painful to me and elevate them and, through the mantra of music, make them into a release..'
FOGUS = 'The apprentice avoids all use of Java classes. The journeyman embraces Java classes. The master knows which classes to embrace and which to avoid.'

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding


    # STEP 0 - TODO
## defining our data structures
    class Node: # NOT given to students
        # TODO
        letter: str
        freq: int
        l: any
        r: any

        
        def __init__(self, letter: str, freq: int, l: any, r: any ):
            self.letter = letter
            self.freq = freq
            self.l = l
            self.r = r
            

    ## defining operations
    ### recursively traverses the huffman tree to record the codes
    def retrieve_codes(v: Node, path: str=''):
        # coding
        if v.letter != None: # if 'TODO': # TODO
            coding[v.letter] = path # TODO
        else:
            retrieve_codes(v.l, path + '0') # TODO
            retrieve_codes(v.r, path + '1') # TODO

    # STEP 1
    ## counting the frequencies - TODO

    for letter in message:
        if letter not in freq.keys():
            freq[letter]=1
        else:
            freq[letter]+=1

    # STEP 2
    ## initialize the nodes - TODO
    nodes = list()
    #nodes.append(Node(0, 'a'))
    for letter, count in freq.items():
        single_node: Node = Node(letter,count,None, None)
        nodes.append(single_node)

    # STEP 3 - TODO
    ## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
        ## sort based on weight
        nodes.sort(key=lambda x: x.freq, reverse=True)

        ## get the first min
        min_a: Node = nodes.pop()

        ## get the second min
        min_b: Node = nodes.pop()

        ## combine the two
        combined: Node = Node(None, min_a.freq+ min_b.freq, min_a, min_b)
        ## put the combined nodes back in the list of nodes
        nodes.append(combined)

    # STEP 4
    ## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    print(coding)
    result: str = str() # TODO (hint coding[letter] -> code)
    for letter in message:
        total = coding[letter]
        result += total

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Diei Analyzing Huffman')

MAX_N: int = int(170 * 3 / 2)

# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = BLOODYWATERS_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', color = 'red', label = 'Bloody Waters')
plt.legend()
## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = BIRTHDAY[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', label = 'Happy Birthday')
plt.legend()
## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = TWINKLE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', label = "Twinkle Twinkle Little Star")
plt.legend()

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = FOGUS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', label = "Fogus")
plt.legend()

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = SO_HUM[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', label = 'So Hum')
plt.legend()

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = GIRA[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(ratios, '-.', label = 'GIRA')
plt.legend()

plt.show()