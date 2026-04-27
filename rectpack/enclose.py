import heapq # heapq.heappush, heapq.heappop
from .packer import newPacker, PackingMode, PackingBin, SORT_LSIDE
from .skyline import SkylineBlWm



class Enclose(object):

    def __init__(self, rectangles=[], max_width=None, max_height=None, rotation=True):
        """
        Arguments:
            rectangles (list): Rectangle to be enveloped
                [(width1, height1), (width2, height2), ...]
            max_width (number|None): Enveloping rectangle max allowed width.
            max_height (number|None): Enveloping rectangle max allowed height.
            rotation (boolean): Enable/Disable rectangle rotation.
        """
        # Enclosing rectangle max width
        self._max_width = max_width

        # Encloseing rectangle max height
        self._max_height = max_height

        # Enable or disable rectangle rotation
        self._rotation = rotation

        # Default packing algorithm
        self._pack_algo = SkylineBlWm
        
        # rectangles to enclose [(width, height), (width, height, ...)]
        self._rectangles = []
        for r in rectangles:
            self.add_rect(*r)

    def _container_candidates(self):
        """Generate container candidate list 
        
        Returns:
            tuple list: [(width1, height1), (width2, height2), ...] 
        """
        pass
   
    def _refine_candidate(self, width, height):
        """
        Use bottom-left packing algorithm to find a lower height for the 
        container.

        Arguments:
            width
            height

        Returns:
            tuple (width, height, PackingAlgorithm):
        """
        pass

    def generate(self):
    
        # Generate initial containers
        pass

    def add_rect(self, width, height):
        """
        Add anoter rectangle to be enclosed

        Arguments:
            width (number): Rectangle width
            height (number): Rectangle height
        """
        pass


