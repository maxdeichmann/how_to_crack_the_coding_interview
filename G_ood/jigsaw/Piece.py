class Piece(objeect):

    def __init__(self, edge_top, edge_bottom, edge_right, edge_left):
        super().__init__()

        self.edge_type = {
            "top": edge_top,
            "bottom": edge_bottom,
            "left": edge_left,
            "right": edge_right
        }

        



        