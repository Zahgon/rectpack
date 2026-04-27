from .geometry import Rectangle


class PackingAlgorithm(object):
    """PackingAlgorithm base class"""

    def __init__(self, width, height, rot=True, bid=None, *args, **kwargs):
        """
        Initialize packing algorithm

        Arguments:
            width (int, float): Packing surface width
            height (int, float): Packing surface height
            rot (bool): Rectangle rotation enabled or disabled
            bid (string|int|...): Packing surface identification
        """
        self.width = width
        self.height = height
        self.rot = rot
        self.rectangles = []
        self.bid = bid
        self._surface = Rectangle(0, 0, width, height)
        self.reset()

    def __len__(self):
        return len(self.rectangles)

    def __iter__(self):
        return iter(self.rectangles)

    def _fits_surface(self, width, height):
        """
        Test surface is big enough to place a rectangle

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height

        Returns:
            boolean: True if it could be placed, False otherwise
        """
        pass
    
    def __getitem__(self, key):
        """
        Return rectangle in selected position.
        """
        return self.rectangles[key]

    def used_area(self):
        """
        Total area of rectangles placed

        Returns:
            int, float: Area
        """
        pass

    def fitness(self, width, height, rot = False):
        """
        Metric used to rate how much space is wasted if a rectangle is placed.
        Returns a value greater or equal to zero, the smaller the value the more 
        'fit' is the rectangle. If the rectangle can't be placed, returns None.

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height
            rot (bool): Enable rectangle rotation

        Returns:
            int, float: Rectangle fitness 
            None: Rectangle can't be placed
        """
        raise NotImplementedError
        
    def add_rect(self, width, height, rid=None):
        """
        Add rectangle of widthxheight dimensions.

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height
            rid: Optional rectangle user id

        Returns:
            Rectangle: Rectangle with placemente coordinates
            None: If the rectangle couldn be placed.
        """
        raise NotImplementedError

    def rect_list(self):
        """
        Returns a list with all rectangles placed into the surface.
        
        Returns:
            List: Format [(x, y, width, height, rid), ...]
        """
        pass

    def validate_packing(self):
        """
        Check for collisions between rectangles, also check all are placed
        inside surface.
        """
        pass

    def is_empty(self):
        # Returns true if there is no rectangles placed.
        pass

    def reset(self):
        pass



