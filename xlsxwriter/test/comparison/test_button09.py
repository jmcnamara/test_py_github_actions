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

        self.set_filename('button09.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename)

        worksheet1 = workbook.add_worksheet()
        worksheet2 = workbook.add_worksheet()

        worksheet1.write_comment('A1', 'Foo')

        worksheet2.insert_button('C2', {})

        worksheet1.set_comments_author('John')

        workbook.close()

        self.assertExcelEqual()
