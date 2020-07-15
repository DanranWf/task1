import pytest
# from busi.calculator import CalTool
import yaml


@pytest.fixture(scope="session",autouse=True)    # for data sharing
def setup():
    print('fixture counting is beginning\n')   #======
    yield None
    print('\nfixture counting is ending')    #========= eauals to teardown

@pytest.fixture(scope='session',autouse=True)
def teardown():
    print('111fixture counting is ending')   #========= equals to setup

@pytest.fixture(scope='session')
def opendata():
    pass

# self-defined  data-args
# def pytest_generate_tests(metafunc:"Metafunc"):
#     if "lwjparam" in metafunc.fixturenames:
#         metafunc.parametrize("lwjparam",metafunc.module.mydata,   #=======data source following module
#                              ids=metafunc.module.myid,
#                              scope='function')

def pytest_addoption(parser):
    envs=parser.getgroup('practice')
    envs.addoption('--envdata',default='test',dest='envdata',help='this is just a explanation')

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv=request.config.getoption('--envdata',default='test')

    with open('env/data.yml') as f:
        mydata=yaml.safe_load(f)

        if myenv=='test':
           return mydata[1]
        elif myenv=='dev':
            return mydata[0]
        elif myenv=='st':
            return mydata[2]

