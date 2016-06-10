import unittest

from pbxproj import PBXGenericObject
from pbxproj.PBXObjects import objects


class PBXGenericObjectTest(unittest.TestCase):
    def testParseCreateAttributes(self):
        obj = {"a": "varA", "b": [1, 2, 3], "c": {"c1": "varC1"}}
        dobj = PBXGenericObject().parse(obj)
        self.assertEqual(dobj.a, "varA")
        self.assertEqual(dobj.b, [1, 2, 3])
        self.assertIsNotNone(dobj.c)

    def testParseCreateObjectOfRightTypes(self):
        obj = {"objects": {"id": {"isa": "type"}}}
        dobj = PBXGenericObject().parse(obj)

        self.assertIsInstance(dobj.objects, objects)

    def testEscapeItem(self):
        self.assertEqual(PBXGenericObject._escape("/bin/sh"), "/bin/sh")
        self.assertEqual(PBXGenericObject._escape("abcdefghijklmnopqrstuvwyz0123456789"), "abcdefghijklmnopqrstuvwyz0123456789")
        self.assertEqual(PBXGenericObject._escape("some spaces"), '"some spaces"')
        self.assertEqual(PBXGenericObject._escape("a.valid_id."), "a.valid_id.")
        self.assertEqual(PBXGenericObject._escape("a-invalid-id"), '"a-invalid-id"')
        self.assertEqual(PBXGenericObject._escape("<group>"), '"<group>"')

    def testPrintObject(self):
        obj = {"a": "varA", "b": [1, 2, 3], "c": {"c1": "varC1"}}
        dobj = PBXGenericObject().parse(obj)
        expected = '{\n\ta = varA;\n\tb = (\n\t\t1,\n\t\t2,\n\t\t3,\n\t);\n\tc = {\n\t\tc1 = varC1;\n\t};\n}'

        self.assertEqual(dobj.__repr__(), expected)

