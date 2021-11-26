class Numeric:
    """
    Class for the fun_with_py.
    Attributes
    ----------
    __author__ = "HSD, Hemant S D"
    __email__ = "ashuhemantsingh@gmail.com"
    __status__ = "planning"


    Private:
        None
        
    Methods
    -------
    Private:
        None
    Public:
        reverse : returns reverse of numbers 
        isMultipleOf : returns true if given number is multiple of it 
         
    """
    def __init__(self, number):
        """
        Creates a new instance of 
        Parameters
        ----------
        number : integer
            takes integer  
        """
        self.___value = number
        if type(self.__value) == int or type(self.__value) == float:
            pass
        else:
            print("Please input a numeric value not string this might cause error")


    def reverse(self):
        """
        return reverse integer
        """
        val = str(self.__value)
        val = val[::-1]
        return int(val)

    def isMultipleOf(self, num):
        """
        return true if it is divisible by given number
        """
        val = self.__value
        if val%num == 0:
            return True
        else:
            return False
