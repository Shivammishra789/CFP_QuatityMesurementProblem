'''
@author: Shivam Mishra
@date: 27-12-21 10:33 AM
'''
from quatity_custom_exception import QuatityCustomException


class UnitConv:

    def feet_inch(self, length):
        '''
        Description:
            Converts the length from feet to inch
        Parameter:
            length(int): length in feet
        Return:
            length_inch(int): length in inch
        '''
        if length is None:
            return None
        elif length >= 0:
            length_inch = length * 12
            return length_inch
        else:
            raise QuatityCustomException('incorrect length')

    def feet_yard(self, length):
        '''
        Description:
            Converts the length from feet to yard
        Parameter:
            length(int): length in feet
        Return:
            length_yard(float): length in inch with 2 decimal precision
        '''
        if length is None:
            return None
        elif length >= 0:
            length_yard = length / 3
            return round(length_yard, 2)
        else:
            raise QuatityCustomException('incorrect length')












