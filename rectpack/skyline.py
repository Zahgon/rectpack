import collections
import itertools
import operator
import heapq
import copy
from .pack_algo import PackingAlgorithm
from .geometry import Point as P
from .geometry import HSegment, Rectangle
from .waste import WasteManager


class Skyline(PackingAlgorithm):
    """ Class implementing Skyline algorithm as described by
    Jukka Jylanki - A Thousand Ways to Pack the Bin (February 27, 2010)

    _skyline:  stores all the segments at the top of the skyline.
    _waste: Handles all wasted sections.
    """

    def __init__(self, width, height, rot=True, *args, **kwargs):
        """
        _skyline is the list used to store all the skyline segments, each 
        one is a list with the format [x, y, width] where x is the x
        coordinate of the left most point of the segment, y the y coordinate
        of the segment, and width the length of the segment. The initial 
        segment is allways [0, 0, surface_width]
        
        Arguments:
            width (int, float): 
            height (int, float):
            rot (bool): Enable or disable rectangle rotation
        """
        self._waste_management = False
        self._waste = WasteManager(rot=rot)
        super(Skyline, self).__init__(width, height, rot, merge=False, *args, **kwargs)

    def _placement_points_generator(self, skyline, width):
        """Returns a generator for the x coordinates of all the placement
        points on the skyline for a given rectangle.

        WARNING: In some cases could be duplicated points, but it is faster
        to compute them twice than to remove them.
        
        Arguments:
            skyline (list): Skyline HSegment list
            width (int, float): Rectangle width

        Returns:
            generator
        """ 
        pass

    def _generate_placements(self, width, height):
        """
        Generate a list with 

        Arguments:
            skyline (list): SkylineHSegment list
            width (number):

        Returns:
            tuple (Rectangle, fitness):
                Rectangle: Rectangle in valid position
                left_skyline: Index for the skyline under the rectangle left edge.
                right_skyline: Index for the skyline under the rectangle right edte.
        """
        pass

    def _merge_skyline(self, skylineq, segment):
        """
        Arguments:
            skylineq (collections.deque):
            segment (HSegment):
        """
        pass

    def _add_skyline(self, rect):
        """
        Arguments:
            seg (Rectangle):
        """
        pass

    def _rect_fitness(self, rect, left_index, right_index):
        pass

    def _select_position(self, width, height):
        """
        Search for the placement with the bes fitness for the rectangle.

        Returns:
            tuple (Rectangle, fitness) - Rectangle placed in the fittest position
            None - Rectangle couldn't be placed
        """
        pass

    def fitness(self, width, height):
        """Search for the best fitness 
        """
        pass

    def add_rect(self, width, height, rid=None):
        """
        Add new rectangle
        """
        pass

    def reset(self):
        pass




class SkylineWMixin(Skyline):
    """Waste managment mixin"""
    def __init__(self, width, height, *args, **kwargs):
        super(SkylineWMixin, self).__init__(width, height, *args, **kwargs)
        self._waste_management = True


class SkylineMwf(Skyline):
    """Implements Min Waste fit heuristic, minimizing the area wasted under the
    rectangle.
    """
    def _rect_fitness(self, rect, left_index, right_index):
        pass

    def _rect_fitnes2s(self, rect, left_index, right_index):
        pass

class SkylineMwfl(Skyline):
    """Implements Min Waste fit with low profile heuritic, minimizing the area
    wasted below the rectangle, at the same time it tries to keep the height
    minimal.
    """ 
    def _rect_fitness(self, rect, left_index, right_index):
        pass


class SkylineBl(Skyline):
    """Implements Bottom Left heuristic, the best fit option is that which
    results in which the top side of the rectangle lies at the bottom-most 
    position.
    """
    def _rect_fitness(self, rect, left_index, right_index):
        pass




class SkylineBlWm(SkylineBl, SkylineWMixin):
    pass

class SkylineMwfWm(SkylineMwf, SkylineWMixin):
    pass

class SkylineMwflWm(SkylineMwfl, SkylineWMixin):
    pass
