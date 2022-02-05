from source.user_management.user import User
from source.database_management.database_operation import Database


class TestGroupUser:

    def init_test_user():
        new_test_user = User()
        new_test_user.register('Test', 'Test123!')

    def test_login(self):
        TestGroupUser.init_test_user()
        new_test_user = User()
        target = True
        result = new_test_user.login('Test', 'Test123!')
        TestGroupUser.delete_test_user()
        assert target == result

    def test_password_without_symbol_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'Test123')
        assert target == passed

    def test_password_without_number_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'Testnew!')
        assert target == passed

    def test_password_without_capital_letter_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'test123')
        assert target == passed

    def test_password_out_of_range_min_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'Test!')
        assert target == passed

    def test_password_out_of_range_min_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'Test!')
        assert target == passed

    def test_password_out_of_range_max_error(self):
        new_test_user = User()
        target = False
        passed = new_test_user.register('Test', 'Test!')
        assert target == passed

    def delete_test_user():
        new_con = Database()
        new_con.execute_one("DELETE FROM student WHERE name_user = 'Test'")
        new_con.commit()
        new_con.close()
