# coding=utf-8
import unittest
import splitfile


class SplitFileTest(unittest.TestCase):

    def setUp(self):
        self.test_input = 'test_input.txt'
        self.separator = splitfile.FileSeparator(self.test_input)
        
    def test_get_text_block(self):
        '''splits file into text blocks'''

        first_text_block = \
            ('1 Wlazł kotek na płotek i mruga; Wlazł kotek na płotek i mruga; Wlazł kotek na płotek i mruga\n'
                '2 Ładna to piosenka niedługa; Ładna to piosenka niedługa; Ładna to piosenka niedługa\n'
                '3 Niedługa niekrótka ale starczy; Niedługa niekrótka ale starczy; Niedługa niekrótka ale starczy\n')
        result = self.separator.next_text_block()
        self.assertEqual(result, first_text_block)


if __name__ == '__main__':
    unittest.main()
