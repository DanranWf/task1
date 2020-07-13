from busi.calculator import CalTool
import pytest


class TestCal:     #==========class fist capital should be lowercase!


    def setup(self):
        self.cal = CalTool()
        print('counting is beginning\n')

    def test_add(self):      #=========== args not be sended in test!
        self.cal = CalTool()
        assert self.cal.add(1,2) == 3
        assert self.cal.add(3,5)==8

    @pytest.mark.parametrize("a,b",[(1,2),(3,5),(8,8)])
    # @pytest.mark.parametrize(a, b, result, ['2,2,4', '3,1,4', '5,9,14'])
    def test_minus(self,a,b):
        print(a-b)
        assert self.cal.minus(a,b)==a-b

    def test_multi(self):
        assert self.cal.multi(1,2)==2
        assert self.cal.multi(3, 5) == 15

    def test_divd(self):
        assert self.cal.divd(1,2)==0.5
        assert self.cal.divd(3, 5) == 0.6

    def teardown(self):
        self.cal = CalTool()
        print('counting is ending')

