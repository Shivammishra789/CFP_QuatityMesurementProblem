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
                             [(0, 0), ( None,None),(1,12),(2,24)])
    def test_feet_to_inch(self,obj,first_length,second_length ):
        # Test case  Zero check, None check, Value check
        assert self.obj1.feet_inch(first_length) == second_length

    @pytest.mark.parametrize("first_length, second_length",
                             [(0, 0), (None, None),(3, 1),(9, 3)])
    def test_feet_to_yard(self, obj, first_length, second_length):
        assert self.obj1.feet_yard(first_length) == second_length

    def test_for_type(self, obj):
        # Test case  Type check
        assert type(self.obj1.feet_inch(1)) == int

    def test_for_comparison1(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_inch(1) != 1

    def test_for_comparison2(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_inch(1) > 1

    def test_for_comparison3(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_inch(1) < 13

    def test_for_type_feet_to_yard(self, obj):
        # Test case Type check
        assert type(self.obj1.feet_yard(1)) == float

    def test_for_comparison1_feet_to_yard(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_yard(1) != 1

    def test_for_comparison2_feet_to_yard(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_yard(1) < 1

    def test_for_comparison1_feet_to_yard(self, obj):
        # Test case Comparison check
        assert self.obj1.feet_yard(1) > 0




        
