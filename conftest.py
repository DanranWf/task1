import pytest
# from busi.calculator import CalTool


@pytest.fixture(scope="session")    # for data sharing
def setup(self):
    # self.cal = CalTool()
    print('fixture counting is beginning\n')   #======


def teardown(self):
    # self.cal = CalTool()
    print('fixture counting is ending')     #=========