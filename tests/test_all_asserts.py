import unittest

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2,4,5,10])
        self.assertNotIn(5, [2,4,10])

    def test_assert_dicts(self):
        user = {"first_name": "German", "last_name": "Garcia"}
        self.assertDictEqual(
            {"first_name": "German", "last_name": "Garcia"},
            user
        )
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )