import unittest
import NoteLearner

class NoteLearnerTestCase(unittest.TestCase):
    """Base class for all NoteLearner tests."""

    def assertSomething(self):
        pass

class NoteLearnerTest(NoteLearnerTestCase):
    def setUp(self):
        # Get things for NoteLearner here

    def test_get_notes_and_durs(self):
        n = NoteLearner()
        n.get_notes_and_durs(some_song_data, tempo)
        self.assertSomething()
    
    def test_train_model(self):
        pass
