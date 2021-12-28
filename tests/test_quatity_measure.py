'''
@author: Shivam Mishra
@date: 27-12-21 10:35 AM
'''
import pytest

from quatity_measure import UnitConv


class TestQuatity:

    @pytest.fixture()
    def obj(self):
        self.obj1 = UnitConv()

    @pytest.mark.parametrize("first_length, second_length",
                             [(0, 0), ( None,None),(1,12)])
    def test_feet_to_inch(self,obj,first_length,second_length ):
        assert self.obj1.feet_inch(first_length) == second_length

    @pytest.mark.parametrize("first_length, second_length",
                             [(0, 0), (None, None),(36,12)])
    def test_feet_to_yard(self, obj, first_length, second_length):
        assert self.obj1.feet_yard(first_length) == second_length


        
