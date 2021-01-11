import math
from collections import defaultdict


def infinity_factory(): # tovární funkce pro vracení nekonečen
    return math.inf


class City:
    def __init__(self, name): # konstruktor
        self.name = name      # do objektu uložíme jméno města
        self.connections = [] # seznam spojení z města je zatím prázdný

    def add_connection(self, target, distance, bidi=True):
        self.connections.append((target, distance))  
        # přidáme dvojici (město, vzdálenost) do seznamu
        if bidi:  # je-li spojení obousměrné
            target.add_connection(self, distance, bidi=False) # vložíme i opačný směr

    def distance(self, target):
        # pořadník s plánem přesunu do startovního města (=self)
        waiting_list = [(self, 0)]
        # prázdná tabulka (nekonečné vzdálenosti)
        mindist = defaultdict(infinity_factory)
        while waiting_list: # dokud není pořadník prázdný
            # vyjme a vrátí první dvojici (další testovaný cíl, dosžitelná vzdálenost)
            goal, sum_distance = waiting_list.pop()
            # je-li dosažitelná vzdálenost menší než aktuální minimální
            if sum_distance < mindist[goal]:
                # nová minimální vzdálenost je rovna dosažitelné
                mindist[goal] = sum_distance
                # projdeme spojení do okolních měst (z města `goal`)
                for next_goal, next_distance in goal.connections:
                    # spočítáme dosažitelnou vzdálenost do okolních měst
                    next_sum_distance = sum_distance + next_distance
                    # je-li menší než aktuálná minimální
                    if next_sum_distance < mindist[next_goal]:
                        # pak přidáme spojení do pořadníku
                        waiting_list.append((next_goal, next_sum_distance))
        # a nakonec vrátíme minimální vzdálenost cílového města
        return mindist[target]
