from .pack_algo import PackingAlgorithm
from .geometry import Rectangle
import itertools
import collections
import operator


first_item = operator.itemgetter(0)



class MaxRects(PackingAlgorithm):

    def __init__(self, width, height, rot=True, *args, **kwargs):
        super(MaxRects, self).__init__(width, height, rot, *args, **kwargs)
   
    def _rect_fitness(self, max_rect, width, height):
        """
        Arguments:
            max_rect (Rectangle): Destination max_rect
            width (int, float): Rectangle width
            height (int, float): Rectangle height

        Returns:
            None: Rectangle couldn't be placed into max_rect
            integer, float: fitness value 
        """
        pass

    def _select_position(self, w, h): 
        """
        Find max_rect with best fitness for placing a rectangle
        of dimentsions w*h

        Arguments:
            w (int, float): Rectangle width
            h (int, float): Rectangle height

        Returns:
            (rect, max_rect)
            rect (Rectangle): Placed rectangle or None if was unable.
            max_rect (Rectangle): Maximal rectangle were rect was placed
        """
        pass

    def _generate_splits(self, m, r):
        """
        When a rectangle is placed inside a maximal rectangle, it stops being one
        and up to 4 new maximal rectangles may appear depending on the placement.
        _generate_splits calculates them.

        Arguments:
            m (Rectangle): max_rect rectangle
            r (Rectangle): rectangle placed

        Returns:
            list : list containing new maximal rectangles or an empty list
        """
        pass

    def _split(self, rect):
        """
        Split all max_rects intersecting the rectangle rect into up to
        4 new max_rects.
        
        Arguments:
            rect (Rectangle): Rectangle

        Returns:
            split (Rectangle list): List of rectangles resulting from the split
        """
        pass

    def _remove_duplicates(self):
        """
        Remove every maximal rectangle contained by another one.
        """
        pass

    def fitness(self, width, height): 
        """
        Metric used to rate how much space is wasted if a rectangle is placed.
        Returns a value greater or equal to zero, the smaller the value the more 
        'fit' is the rectangle. If the rectangle can't be placed, returns None.

        Arguments:
            width (int, float): Rectangle width
            height (int, float): Rectangle height

        Returns:
            int, float: Rectangle fitness 
            None: Rectangle can't be placed
        """
        pass

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
        pass

    def reset(self):
        pass




class MaxRectsBl(MaxRects):
    
    def _select_position(self, w, h): 
        """
        Select the position where the y coordinate of the top of the rectangle
        is lower, if there are severtal pick the one with the smallest x 
        coordinate
        """
        pass


class MaxRectsBssf(MaxRects):
    """Best Sort Side Fit minimize short leftover side"""
    def _rect_fitness(self, max_rect, width, height):
        pass
           
class MaxRectsBaf(MaxRects):
    """Best Area Fit pick maximal rectangle with smallest area
    where the rectangle can be placed"""
    def _rect_fitness(self, max_rect, width, height):
        pass


class MaxRectsBlsf(MaxRects):
    """Best Long Side Fit minimize long leftover side"""
    def _rect_fitness(self, max_rect, width, height):
        pass
