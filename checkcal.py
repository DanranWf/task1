# from busi.calculator import CalTool
import pytest
import yaml

from busi.calculator import CalTool

# data-processing
with open('data/data.yml') as f:
    mydata = yaml.safe_load(f)
    adddata=mydata['add']
    minusdata=mydata['minus']
    multidata = mydata['multi']
    divdata = mydata['div']


class TestCal:     #==========class fist capital should be lowercase!

    def setup_class(self):
        pass

    def setup(self):
        self.cal = CalTool()
        # print('counting is beginning\n')

    @pytest.mark.parametrize('a,b,result',adddata)
    @pytest.mark.run(order=-4)
    def test_add(self,a,b,result):                         #=========== args not be sended in test!
        assert self.cal.add(a,b) ==result

    @pytest.mark.parametrize("a,b,result",minusdata)
    @pytest.mark.run(order=-3)
    @pytest.mark.dependency(depends=["test_add"])
    def test_minus(self,a,b,result):
        assert self.cal.minus(a,b)==result

    @pytest.mark.parametrize('a,b,result',multidata)
    @pytest.mark.run(order=-2)
    def test_multi(self,a,b,result):
        assert self.cal.multi(a,b)==result

    @pytest.mark.parametrize('a,b,result', divdata)
    @pytest.mark.run(order=-1)
    @pytest.mark.dependency(depends=["test_multi"])
    def test_divd(self,a,b,result):
        assert self.cal.divd(a,b)==result


    def test_env(self,cmdoption):
        print(cmdoption)
        ip, port = cmdoption['ip'], cmdoption['port']
        url = "https://{}:{}".format(ip, port)
        print(url)



    def teardown(self):
        pass
        # print('counting is ending')

