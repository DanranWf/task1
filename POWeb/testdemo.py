from index import Index


class TestLogin:
    def setup(self):
        # Index().goto_register()
        self.index=Index()
    def test_register(self):
        result=self.index.goto_register().register()
        assert result

    def test_login(self):
        self.index.goto_login().scan()

    def test_logandregister(self):
        self.index.goto_login().goto_register().register()

        # Index().goto_register().register()
        # Index().goto_login().goto_register().register()
