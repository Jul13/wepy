# ==============================================================================
# author          : Amine Kamoun
# date            : 28/03/17
# ==============================================================================
import os
import unittest
import wepy.util.excel as xl


class TestExcel(unittest.TestCase):
    def test_open_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = current_dir + '/rebalance 2017-03-06 10-32-27-example.xlsx'
        worksheet_names = xl.read_worksheets_names(file_path)
        self.assertEqual(
            list(['Summary', 'Prices', 'Proxy Prices', 'FX rates', 'Money Volumes', 'Returns', 'Volumes']),
            worksheet_names)

    def test_get_data_feature(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = current_dir + '/rebalance 2017-03-06 10-32-27-example.xlsx'
        wb = xl.get_workbook(file_path=file_path)
        feature_from_file = xl.worksheet_to_feature(wb, "Returns", 1)
        self.assertTupleEqual(feature_from_file.shape, (506, 76))




if __name__ == '__main__':
    unittest.main()
