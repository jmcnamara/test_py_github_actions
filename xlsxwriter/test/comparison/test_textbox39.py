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

        self.set_filename('textbox39.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with textbox(s)."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.insert_textbox('E9', 'This is some text',
                                 {'url': 'https://github.com/jmcnamara'})

        worksheet.insert_textbox('E19', 'This is some text',
                                 {'url': 'https://github.com/jmcnamara'})

        workbook.close()

        self.assertExcelEqual()
