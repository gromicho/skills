import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

SCRIPT=Path(__file__).resolve().parents[1]/'skills/amsterdam-abs-journal-points/scripts/lookup_journal.py'
spec=importlib.util.spec_from_file_location('lookup',SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class LookupTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=Path(self.temp.name)/'fixture.xlsx'
        # Synthetic titles/grades exercise XML parsing without institutional data.
        xml='''<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>
        <row r="2"><c r="A2" t="inlineStr"><is><t>A</t></is></c><c r="B2" t="inlineStr"><is><t>Computers &amp; Operations Research</t></is></c></row>
        <row r="3"><c r="A3" t="inlineStr"><is><t>A</t></is></c><c r="B3" t="inlineStr"><is><t>Journal on Computing</t></is></c></row>
        </sheetData></worksheet>'''
        with zipfile.ZipFile(self.path,'w') as archive:archive.writestr('xl/worksheets/sheet1.xml',xml)
    def tearDown(self):self.temp.cleanup()
    def test_ampersand_and_source_row(self):
        row=module.lookup('Computers and Operations Research',self.path)['matches'][0]
        self.assertEqual((row['category'],row['points'],row['cells']),('A',100,'A2:B2'))
    def test_alias(self):
        self.assertEqual(module.lookup('INFORMS Journal on Computing',self.path)['matches'][0]['journal'],'Journal on Computing')
    def test_missing_is_unresolved(self):
        result=module.lookup('Unknown journal',self.path)
        self.assertEqual(result['matches'],[])
        self.assertEqual(result['status'],'no_match_points_not_established')
    def test_empty_query_rejected(self):
        with self.assertRaises(ValueError):module.lookup(' ',self.path)
    def test_no_bundled_workbook(self):
        with self.assertRaises(ValueError):module.lookup('Journal')

if __name__=='__main__':unittest.main()
