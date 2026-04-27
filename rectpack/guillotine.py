from .pack_algo import PackingAlgorithm
from .geometry import Rectangle
import itertools
import operator


class Guillotine(PackingAlgorithm):
    """Implementation of several variants of Guillotine packing algorithm
    
    For a more detailed explanation of the algorithm used, see:
    Jukka Jylanki - A Thousand Ways to Pack the Bin (February 27, 2010)
    """
    def __init__(self, width, height, rot=True, merge=True, *args, **kwargs):
        """
        Arguments:
            width (int, float):
            height (int, float):
            merge (bool): Optional keyword argument
        """
        self._merge = merge
        super(Guillotine, self).__init__(width, height, rot, *args, **kwargs)
        

    def _add_section(self, section):
        """Adds a new section to the free section list, but before that and if 
        section merge is enabled, tries to join the rectangle with all existing 
        sections, if successful the resulting section is again merged with the 
        remaining sections until the operation fails. The result is then 
        appended to the list.

        Arguments:
            section (Rectangle): New free section.
        """
        pass


    def _split_horizontal(self, section, width, height):
        """For an horizontal split the rectangle is placed in the lower
        left corner of the section (section's xy coordinates), the top
        most side of the rectangle and its horizontal continuation,
        marks the line of division for the split.
        +-----------------+
        |                 |
        |                 |
        |                 |
        |                 |
        +-------+---------+
        |#######|         |
        |#######|         |
        |#######|         |
        +-------+---------+
        If the rectangle width is equal to the the section width, only one
        section is created over the rectangle. If the rectangle height is
        equal to the section height, only one section to the right of the
        rectangle is created. If both width and height are equal, no sections
        are created.
        """
        pass


    def _split_vertical(self, section, width, height):
        """For a vertical split the rectangle is placed in the lower
        left corner of the section (section's xy coordinates), the
        right most side of the rectangle and its vertical continuation,
        marks the line of division for the split.
        +-------+---------+
        |       |         |
        |       |         |
        |       |         |
        |       |         |
        +-------+         |
        |#######|         |
        |#######|         |
        |#######|         |
        +-------+---------+
        If the rectangle width is equal to the the section width, only one
        section is created over the rectangle. If the rectangle height is
        equal to the section height, only one section to the right of the
        rectangle is created. If both width and height are equal, no sections
        are created.
        """
        pass
        

    def _split(self, section, width, height):
        """
        Selects the best split for a section, given a rectangle of dimmensions
        width and height, then calls _split_vertical or _split_horizontal, 
        to do the dirty work.
       
        Arguments:
            section (Rectangle): Section to split
            width (int, float): Rectangle width
            height (int, float): Rectangle height
        """
        raise NotImplementedError


    def _section_fitness(self, section, width, height):
        """The subclass for each one of the Guillotine selection methods,
        BAF, BLSF.... will override this method, this is here only
        to asure a valid value return if the worst happens.
        """
        raise NotImplementedError

    def _select_fittest_section(self, w, h):
        """Calls _section_fitness for each of the sections in free section 
        list. Returns the section with the minimal fitness value, all the rest 
        is boilerplate to make the fitness comparison, to rotatate the rectangles,
        and to take into account when _section_fitness returns None because 
        the rectangle couldn't be placed.

        Arguments:
            w (int, float): Rectangle width
            h (int, float): Rectangle height

        Returns:
            (section, was_rotated): Returns the tuple 
                section (Rectangle): Section with best fitness
                was_rotated (bool): The rectangle was rotated 
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

    def fitness(self, width, height):
        """
        In guillotine algorithm case, returns the min of the fitness of all 
        free sections, for the given dimension, both normal and rotated
        (if rotation enabled.)
        """
        pass

    def reset(self):
        pass



class GuillotineBaf(Guillotine):
    """Implements Best Area Fit (BAF) section selection criteria for 
    Guillotine algorithm.
    """
    def _section_fitness(self, section, width, height):
        pass


class GuillotineBlsf(Guillotine):
    """Implements Best Long Side Fit (BLSF) section selection criteria for 
    Guillotine algorithm.
    """
    def _section_fitness(self, section, width, height):
        pass


class GuillotineBssf(Guillotine):
    """Implements Best Short Side Fit (BSSF) section selection criteria for 
    Guillotine algorithm.
    """
    def _section_fitness(self, section, width, height):
        pass


class GuillotineSas(Guillotine):
    """Implements Short Axis Split (SAS) selection rule for Guillotine 
    algorithm.
    """
    def _split(self, section, width, height):
        pass
        


class GuillotineLas(Guillotine):
    """Implements Long Axis Split (LAS) selection rule for Guillotine 
    algorithm.
    """
    def _split(self, section, width, height):
        pass



class GuillotineSlas(Guillotine):
    """Implements Short Leftover Axis Split (SLAS) selection rule for 
    Guillotine algorithm.
    """
    def _split(self, section, width, height):
        pass
        


class GuillotineLlas(Guillotine):
    """Implements Long Leftover Axis Split (LLAS) selection rule for 
    Guillotine algorithm.
    """
    def _split(self, section, width, height):
        pass



class GuillotineMaxas(Guillotine):
    """Implements Max Area Axis Split (MAXAS) selection rule for Guillotine
    algorithm. Maximize the larger area == minimize the smaller area.
    Tries to make the rectangles more even-sized.
    """
    def _split(self, section, width, height):
        pass
        


class GuillotineMinas(Guillotine):
    """Implements Min Area Axis Split (MINAS) selection rule for Guillotine 
    algorithm. 
    """
    def _split(self, section, width, height):
        pass
       


# Guillotine algorithms GUILLOTINE-RECT-SPLIT, Selecting one
# Axis split, and one selection criteria.
class GuillotineBssfSas(GuillotineBssf, GuillotineSas):
    pass
class GuillotineBssfLas(GuillotineBssf, GuillotineLas):
    pass
class GuillotineBssfSlas(GuillotineBssf, GuillotineSlas):
    pass
class GuillotineBssfLlas(GuillotineBssf, GuillotineLlas):
    pass
class GuillotineBssfMaxas(GuillotineBssf, GuillotineMaxas):
    pass
class GuillotineBssfMinas(GuillotineBssf, GuillotineMinas):
    pass
class GuillotineBlsfSas(GuillotineBlsf, GuillotineSas):
    pass
class GuillotineBlsfLas(GuillotineBlsf, GuillotineLas):
    pass
class GuillotineBlsfSlas(GuillotineBlsf, GuillotineSlas):
    pass
class GuillotineBlsfLlas(GuillotineBlsf, GuillotineLlas):
    pass
class GuillotineBlsfMaxas(GuillotineBlsf, GuillotineMaxas):
    pass
class GuillotineBlsfMinas(GuillotineBlsf, GuillotineMinas):
    pass
class GuillotineBafSas(GuillotineBaf, GuillotineSas):
    pass
class GuillotineBafLas(GuillotineBaf, GuillotineLas):
    pass
class GuillotineBafSlas(GuillotineBaf, GuillotineSlas):
    pass
class GuillotineBafLlas(GuillotineBaf, GuillotineLlas):
    pass
class GuillotineBafMaxas(GuillotineBaf, GuillotineMaxas):
    pass
class GuillotineBafMinas(GuillotineBaf, GuillotineMinas):
    pass



