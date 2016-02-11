__author__ = 'antonioirizar'
from unittest import TestCase
from score_image import score_image_with_commands


class TestControlCloudTrailActiveInAllRegions(TestCase):
    def test_score_image_1(self):
        image_original = [[True, True, True], [True, True, True], [True, True, True]]
        list_commands = [(1, 1, 1, 1)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 17)

    def test_score_image_2(self):
        image_original = [[True, True, True], [True, False, True], [True, True, True]]
        list_commands = [(1, 1, 1, 1), (0, 1, 1)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 16)

    def test_score_image_3(self):
        image_original = [[True, True, True], [True, False, True], [True, True, True]]
        list_commands = [(1, 1, 1, 1)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertFalse(equals)
        self.assertEqual(score, 15)

    def test_score_image_4(self):
        image_original = [[True, True, True], [True, False, True], [True, True, True]]
        list_commands = [(2, 0, 0, 2, 0), (2, 0, 1, 2, 1), (2, 0, 2, 2, 2)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertFalse(equals)
        self.assertEqual(score, 13)

    def test_score_image_5(self):
        image_original = [[True, True, True], [True, True, True], [True, True, True]]
        list_commands = [(2, 0, 0, 2, 0), (2, 0, 1, 2, 1), (2, 0, 2, 2, 2)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 15)

    def test_score_image_6(self):
        image_original = [[True, True, True], [True, True, True], [True, True, True]]
        list_commands = [(2, 2, 0, 0, 0), (2, 0, 1, 2, 1), (2, 0, 2, 2, 2)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 15)

    def test_score_image_7(self):
        image_original = [[True, True, True], [True, True, True], [True, True, True]]
        list_commands = [(2, 0, 0, 0, 2), (2, 1, 0, 1, 2), (2, 2, 0, 2, 2)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 15)

    def test_score_image_8(self):
        image_original = [[False, False, False], [True, False, False], [False, False, False]]
        list_commands = [(2, 1, 0, 1, 0)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 17)

    def test_score_image_9(self):
        image_original = [[False, False, False], [True, False, False], [False, False, False]]
        list_commands = [(1, 1, 0, 0)]
        equals, score = score_image_with_commands(image_original, list_commands)
        self.assertTrue(equals)
        self.assertEqual(score, 17)
