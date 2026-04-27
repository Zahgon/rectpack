from .maxrects import MaxRectsBssf

import operator
import itertools
import collections

import decimal

# Float to Decimal helper
def float2dec(ft, decimal_digits):
    """
    Convert float (or int) to Decimal (rounding up) with the
    requested number of decimal digits.

    Arguments:
        ft (float, int): Number to convert
        decimal (int): Number of digits after decimal point

    Return:
        Decimal: Number converted to decima
    """
    pass


# Sorting algos for rectangle lists
SORT_AREA  = lambda rectlist: sorted(rectlist, reverse=True, 
        key=lambda r: r[0]*r[1]) # Sort by area

SORT_PERI  = lambda rectlist: sorted(rectlist, reverse=True, 
        key=lambda r: r[0]+r[1]) # Sort by perimeter

SORT_DIFF  = lambda rectlist: sorted(rectlist, reverse=True, 
        key=lambda r: abs(r[0]-r[1])) # Sort by Diff

SORT_SSIDE = lambda rectlist: sorted(rectlist, reverse=True, 
        key=lambda r: (min(r[0], r[1]), max(r[0], r[1]))) # Sort by short side

SORT_LSIDE = lambda rectlist: sorted(rectlist, reverse=True, 
        key=lambda r: (max(r[0], r[1]), min(r[0], r[1]))) # Sort by long side

SORT_RATIO = lambda rectlist: sorted(rectlist, reverse=True,
        key=lambda r: r[0]/r[1]) # Sort by side ratio

SORT_NONE = lambda rectlist: list(rectlist) # Unsorted



class BinFactory(object):

    def __init__(self, width, height, count, pack_algo, *args, **kwargs):
        self._width = width
        self._height = height
        self._count = count
        
        self._pack_algo = pack_algo
        self._algo_kwargs = kwargs
        self._algo_args = args
        self._ref_bin = None # Reference bin used to calculate fitness
        
        self._bid = kwargs.get("bid", None)

    def _create_bin(self):
        pass

    def is_empty(self):
        pass

    def fitness(self, width, height):
        pass

    def fits_inside(self, width, height):
        # Determine if rectangle widthxheight will fit into empty bin
        pass

    def new_bin(self):
        pass

    def __eq__(self, other):
        return self._width*self._height == other._width*other._height

    def __lt__(self, other):
        return self._width*self._height < other._width*other._height

    def __str__(self):
        return "Bin: {} {} {}".format(self._width, self._height, self._count)



class PackerBNFMixin(object):
    """
    BNF (Bin Next Fit): Only one open bin at a time.  If the rectangle
    doesn't fit, close the current bin and go to the next.
    """

    def add_rect(self, width, height, rid=None):
        pass


class PackerBFFMixin(object):
    """
    BFF (Bin First Fit): Pack rectangle in first bin it fits
    """
 
    def add_rect(self, width, height, rid=None):
        # see if this rect will fit in any of the open bins
        pass


class PackerBBFMixin(object):
    """
    BBF (Bin Best Fit): Pack rectangle in bin that gives best fitness
    """

    # only create this getter once
    first_item = operator.itemgetter(0)

    def add_rect(self, width, height, rid=None):
 
        # Try packing into open bins
        pass



class PackerOnline(object):
    """
    Rectangles are packed as soon are they are added
    """

    def __init__(self, pack_algo=MaxRectsBssf, rotation=True):
        """
        Arguments:
            pack_algo (PackingAlgorithm): What packing algo to use
            rotation (bool): Enable/Disable rectangle rotation
        """
        self._rotation = rotation
        self._pack_algo = pack_algo
        self.reset()

    def __iter__(self):
        return itertools.chain(self._closed_bins, self._open_bins)

    def __len__(self):
        return len(self._closed_bins)+len(self._open_bins)
    
    def __getitem__(self, key):
        """
        Return bin in selected position. (excluding empty bins)
        """
        if not isinstance(key, int):
            raise TypeError("Indices must be integers")

        size = len(self)  # avoid recalulations

        if key < 0:
            key += size

        if not 0 <= key < size:
            raise IndexError("Index out of range")
        
        if key < len(self._closed_bins):
            return self._closed_bins[key]
        else:
            return self._open_bins[key-len(self._closed_bins)]

    def _new_open_bin(self, width=None, height=None, rid=None):
        """
        Extract the next empty bin and append it to open bins

        Returns:
            PackingAlgorithm: Initialized empty packing bin.
            None: No bin big enough for the rectangle was found
        """
        pass

    def add_bin(self, width, height, count=1, **kwargs):
        # accept the same parameters as PackingAlgorithm objects
        pass

    def rect_list(self):
        pass

    def bin_list(self):
        """
        Return a list of the dimmensions of the bins in use, that is closed
        or open containing at least one rectangle
        """
        pass

    def validate_packing(self):
        pass

    def reset(self): 
        # Bins fully packed and closed.
        pass


class Packer(PackerOnline):
    """
    Rectangles aren't packed untils pack() is called
    """

    def __init__(self, pack_algo=MaxRectsBssf, sort_algo=SORT_NONE, 
            rotation=True):
        """
        """
        super(Packer, self).__init__(pack_algo=pack_algo, rotation=rotation)
        
        self._sort_algo = sort_algo

        # User provided bins and Rectangles
        self._avail_bins = collections.deque()
        self._avail_rect = collections.deque()

        # Aux vars used during packing
        self._sorted_rect = []

    def add_bin(self, width, height, count=1, **kwargs):
        pass

    def add_rect(self, width, height, rid=None):
        pass

    def _is_everything_ready(self):
        pass

    def pack(self):

        pass


 
class PackerBNF(Packer, PackerBNFMixin):
    """
    BNF (Bin Next Fit): Only one open bin, if rectangle doesn't fit
    go to next bin and close current one.
    """
    pass

class PackerBFF(Packer, PackerBFFMixin):
    """
    BFF (Bin First Fit): Pack rectangle in first bin it fits
    """
    pass
    
class PackerBBF(Packer, PackerBBFMixin):
    """
    BBF (Bin Best Fit): Pack rectangle in bin that gives best fitness
    """
    pass 

class PackerOnlineBNF(PackerOnline, PackerBNFMixin):
    """
    BNF Bin Next Fit Online variant
    """
    pass 

class PackerOnlineBFF(PackerOnline, PackerBFFMixin):
    """ 
    BFF Bin First Fit Online variant
    """
    pass

class PackerOnlineBBF(PackerOnline, PackerBBFMixin):
    """ 
    BBF Bin Best Fit Online variant
    """
    pass


class PackerGlobal(Packer, PackerBNFMixin):
    """ 
    GLOBAL: For each bin pack the rectangle with the best fitness.
    """
    first_item = operator.itemgetter(0)
    
    def __init__(self, pack_algo=MaxRectsBssf, rotation=True):
        """
        """
        super(PackerGlobal, self).__init__(pack_algo=pack_algo,
            sort_algo=SORT_NONE, rotation=rotation)

    def _find_best_fit(self, pbin):
        """
        Return best fitness rectangle from rectangles packing _sorted_rect list

        Arguments:
            pbin (PackingAlgorithm): Packing bin

        Returns:
            key of the rectangle with best fitness
        """
        pass


    def _new_open_bin(self, remaining_rect):
        """
        Extract the next bin where at least one of the rectangles in
        rem

        Arguments:
            remaining_rect (dict): rectangles not placed yet

        Returns:
            PackingAlgorithm: Initialized empty packing bin.
            None: No bin big enough for the rectangle was found
        """
        pass

    def pack(self):
       
        pass





# Packer factory
class Enum(tuple): 
    __getattr__ = tuple.index

PackingMode = Enum(["Online", "Offline"])
PackingBin = Enum(["BNF", "BFF", "BBF", "Global"])


def newPacker(mode=PackingMode.Offline, 
         bin_algo=PackingBin.BBF, 
        pack_algo=MaxRectsBssf,
        sort_algo=SORT_AREA, 
        rotation=True):
    """
    Packer factory helper function

    Arguments:
        mode (PackingMode): Packing mode
            Online: Rectangles are packed as soon are they are added
            Offline: Rectangles aren't packed untils pack() is called
        bin_algo (PackingBin): Bin selection heuristic
        pack_algo (PackingAlgorithm): Algorithm used
        rotation (boolean): Enable or disable rectangle rotation. 

    Returns:
        Packer: Initialized packer instance.
    """
    pass


