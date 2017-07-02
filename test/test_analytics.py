import unittest
from twstock import analytics


class AnalyticsTest(unittest.TestCase):
    def setUp(self):
        self.legacy = analytics.LegacyAnalytics()
        self.ng = analytics.Analytics()

    def test_continuous(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        legacy_result = self.legacy.cal_continue(data)
        ng_result = self.ng.continuous(data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, 6)

        data = [1, 2, 3, 4, 1, 2]
        legacy_result = self.legacy.cal_continue(data)
        ng_result = self.ng.continuous(data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, 1)

        data = [1, 2, 3, 4, 1, 2, 3, 4, 5]
        legacy_result = self.legacy.cal_continue(data)
        ng_result = self.ng.continuous(data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, 4)

        data = [5, 4, 3, 2, 1]
        legacy_result = self.legacy.cal_continue(data)
        ng_result = self.ng.continuous(data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, -4)

        data = [5, 4, 3, 2, 1, 5, 4, 3]
        legacy_result = self.legacy.cal_continue(data)
        ng_result = self.ng.continuous(data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, -2)

    def test_moving_average(self):
        data = [50, 60, 70, 75]

        # Legacy moving_average will affect data argument's data
        ng_result = self.ng.moving_average(2, data)
        legacy_result = self.legacy.moving_average(2, data)
        self.assertEqual(ng_result, legacy_result)
        self.assertEqual(ng_result, [55.0, 65.0, 72.5])

    def test_ma_bias_ratio(self):
        data = [50, 60, 70, 75, 80, 88, 102, 105, 106]
        self.ng.price = data
        legacy_result = self.legacy.ma_bias_ratio(3, 6, data)
        ng_result = self.ng.ma_bias_ratio(3, 6)
        self.assertEqual(ng_result, legacy_result)

        data = [75, 72, 77, 85, 100, 65, 60, 55, 52, 45]
        self.ng.price = data
        legacy_result = self.legacy.ma_bias_ratio(3, 6, data)
        ng_result = self.ng.ma_bias_ratio(3, 6)
        self.assertEqual(ng_result, legacy_result)

    def test_ma_bias_ratio_pivot(self):
        data = [50, 60, 70, 75, 80, 88, 102, 105, 106]
        legacy_result = self.legacy.ma_bias_ratio_point(data, 5, False)
        ng_result = self.ng.ma_bias_ratio_pivot(data, 5, False)
        self.assertEqual(legacy_result, ng_result)

        data = [75, 72, 77, 85, 100, 65, 60, 55, 52, 45]
        legacy_result = self.legacy.ma_bias_ratio_point(data, 5, False)
        ng_result = self.ng.ma_bias_ratio_pivot(data, 5, False)
        self.assertEqual(legacy_result, ng_result)

