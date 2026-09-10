from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        #sorted(card_counts) automatically extracts just the unique cards ([1, 2, 3, 4, 5])
        #and sorts them, which sets up the perfect ordered loop for our greedy "start with the
        #smallest card" logic.

        if len(hand)%groupSize!=0:
            return False

        card_count = Counter(hand)

        for card in sorted(card_count):

            needed = card_count[card]

            if needed>0:

                for i in range(card,card+groupSize):

                    if card_count[i]<needed:
                        return False
                    card_count[i]-=needed

        return True