###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2021, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparison_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('chart_chartarea05.xlsx')

    def test_create_file(self):
        """Test XlsxWriter chartarea properties."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()
        chart = workbook.add_chart({'type': 'pie'})

        data = [
            [2, 4, 6],
            [60, 30, 10],
        ]

        worksheet.write_column('A1', data[0])
        worksheet.write_column('B1', data[1])

        chart.add_series({
            'categories': '=Sheet1!$A$1:$A$3',
            'values': '=Sheet1!$B$1:$B$3',
        })

        chart.set_chartarea({
            'border': {'color': '#FFFF00', 'dash_type': 'long_dash'},
            'fill': {'color': '#92D050'}
        })

        chart.set_plotarea({
            'border': {'dash_type': 'square_dot'},
            'fill': {'color': '#FF0000'}
        })

        worksheet.insert_chart('E9', chart)

        workbook.close()

        self.assertExcelEqual()
