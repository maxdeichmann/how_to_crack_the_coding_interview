from Piece import Piece

class Puzzle(object):

    def __init__(self, size):
        super().__init__()
        
        self.size = size
        self.solution = [][]
        self.pieces = initialise_pieces(size)
    
    def initialise_pieces(self, size):
        
        # corener pieces
        top_left = Piece("flat", "outside", "outside", "flat")
        top_right = Piece("flat", "outside", "flat", "outside")
        bottom_left = Piece("outside", "flat", "outside", "flat")
        bottom_right = Piece("outside", "flat", "outside", "flat")

        pieces = [top_left, top_right, bottom_left, bottom_right]


        




    
