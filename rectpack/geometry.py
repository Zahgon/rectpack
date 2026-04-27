from math import sqrt



class Point(object):

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __repr__(self):
        return "P({}, {})".format(self.x, self.y)

    def distance(self, point):
        """
        Calculate distance to another point
        """
        pass

    def distance_squared(self, point):
        pass


class Segment(object):
    
    __slots__ = ('start', 'end')

    def __init__(self, start, end):
        """
        Arguments:
            start (Point): Segment start point
            end (Point): Segment end point
        """
        assert(isinstance(start, Point) and isinstance(end, Point))
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            None
        return self.start==other.start and self.end==other.end

    def __repr__(self):
        return "S({}, {})".format(self.start, self.end)
    
    @property
    def length_squared(self):
        """Faster than length and useful for some comparisons"""
        pass

    @property
    def length(self):
        pass

    @property
    def top(self):
        pass
    
    @property
    def bottom(self):
        pass

    @property
    def right(self):
        pass

    @property
    def left(self):
        pass


class HSegment(Segment):
    """Horizontal Segment""" 

    def __init__(self, start, length):
        """
        Create an Horizontal segment given its left most end point and its
        length.

        Arguments:
            - start (Point): Starting Point
            - length (number): segment length
        """
        assert(isinstance(start, Point) and not isinstance(length, Point))
        super(HSegment, self).__init__(start, Point(start.x+length, start.y))

    @property
    def length(self):
        pass


class VSegment(Segment):
    """Vertical Segment"""

    def __init__(self, start, length):
        """
        Create a Vertical segment given its bottom most end point and its
        length.
        
        Arguments:
            - start (Point): Starting Point
            - length (number): segment length
        """
        assert(isinstance(start, Point) and not isinstance(length, Point))
        super(VSegment, self).__init__(start, Point(start.x, start.y+length))

    @property
    def length(self):
        pass
    


class Rectangle(object):
    """Basic rectangle primitive class.
    x, y-> Lower right corner coordinates
    width - 
    height - 
    """
    __slots__ = ('width', 'height', 'x', 'y', 'rid')

    def __init__(self, x, y, width, height, rid = None):
        """
        Args:
            x (int, float):
            y (int, float):
            width (int, float):
            height (int, float):
            rid (int):
        """
        assert(height >=0 and width >=0)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rid = rid

    @property
    def bottom(self):
        """
        Rectangle bottom edge y coordinate
        """
        pass

    @property
    def top(self):
        """
        Rectangle top edge y coordiante
        """
        pass

    @property
    def left(self):
        """
        Rectangle left ednge x coordinate
        """
        pass

    @property
    def right(self):
        """
        Rectangle right edge x coordinate
        """
        pass

    @property
    def corner_top_l(self):
        pass

    @property
    def corner_top_r(self):
        pass

    @property
    def corner_bot_r(self):
        pass

    @property
    def corner_bot_l(self):
        pass

    def __lt__(self, other):
        """
        Compare rectangles by area (used for sorting)
        """
        return self.area() < other.area()
    
    def __eq__(self, other):
        """
        Equal rectangles have same area.
        """
        if not isinstance(other, self.__class__):
            return False

        return (self.width == other.width and \
                self.height == other.height and \
                self.x == other.x and \
                self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y, self.width, self.height))

    def __iter__(self):
        """
        Iterate through rectangle corners
        """
        yield self.corner_top_l
        yield self.corner_top_r
        yield self.corner_bot_r
        yield self.corner_bot_l

    def __repr__(self):
        return "R({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)

    def area(self):
        """
        Rectangle area
        """
        pass

    def move(self, x, y):
        """
        Move Rectangle to x,y coordinates

        Arguments:
            x (int, float): X coordinate
            y (int, float): Y coordinate
        """
        pass

    def contains(self, rect):
        """
        Tests if another rectangle is contained by this one

        Arguments:
            rect (Rectangle): The other rectangle

        Returns:
            bool: True if it is container, False otherwise
        """
        pass

    def intersects(self, rect, edges=False):
        """
        Detect intersections between this and another Rectangle.

        Parameters:
            rect (Rectangle): The other rectangle.
            edges (bool): True to consider rectangles touching by their
                edges or corners to be intersecting.
                (Should have been named include_touching)

        Returns:
            bool: True if the rectangles intersect, False otherwise
        """
        pass

    def intersection(self, rect, edges=False):
        """
        Returns the rectangle resulting of the intersection between this and another 
        rectangle. If the rectangles are only touching by their edges, and the 
        argument 'edges' is True the rectangle returned will have an area of 0.
        Returns None if there is no intersection.
        
        Arguments:
             rect (Rectangle): The other rectangle.
             edges (bool): If True Rectangles touching by their edges are 
                considered to be intersection. In this case a rectangle of 
                0 height or/and width will be returned.

        Returns:
            Rectangle: Intersection.
            None: There was no intersection.
        """
        pass

    def join(self, other):
        """
        Try to join a rectangle to this one, if the result is also a rectangle 
        and the operation is successful and this rectangle is modified to the union.

        Arguments:
            other (Rectangle): Rectangle to join

        Returns:
            bool: True when successfully joined, False otherwise
        """
        pass

