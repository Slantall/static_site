import unittest
from markdown_blocks import *


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        blocks = """# This is a heading   

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

   * This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertListEqual(markdown_to_blocks(blocks), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])



class TestBlockTypeClassifications(unittest.TestCase):
    def test_block_type_heading1(self):
        block = "## a heading block."
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_type_heading2(self):
        block = "# a heading block."
        self.assertEqual(block_to_block_type(block), "heading")


    def test_block_type_not_heading2(self):
        block = "#not a heading block."
        self.assertNotEqual(block_to_block_type(block), "heading")

    def test_block_type_code(self):
        block = "```a code block.```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_type_not_code(self):
        block = "``not code block.``"
        self.assertNotEqual(block_to_block_type(block), "code")

    def test_block_type_quote1(self):
        block = ">a quote block.```"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_type_quote2(self):
        block = """>a quote block.
>more quotes"""
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_type_not_quote(self):
        block = "<not quote block."
        self.assertNotEqual(block_to_block_type(block), "quote")

    def test_block_type_unordered_list1(self):
        block = "* unordered list block."
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_type_unordered_list2(self):
        block = """* unordered list block.
* with more lines
- and mixed symbols"""
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_type_not_unordered_list(self):
        block = """* unordered list block.
*with more lines
- and mixed symbols
* but one is missing a space"""
        self.assertNotEqual(block_to_block_type(block), "unordered_list")


    def test_block_type_ordered_list1(self):
        block = """1. ordered list block.
2. with more lines
3. and same symbols"""
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_block_type_not_ordered_list(self):
        block = """1. ordered list block.
2. with more lines
4. but a missing number."""
        self.assertNotEqual(block_to_block_type(block), "ordered_list")

    def test_block_type_paragraph(self):
        block = """1 ordered list block.
2. with more lines
3. and same symbols(actually a paragraph due to 1 missing a .)"""
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_type_not_paragraph(self):
        block = """1. ordered list block.
2. with more lines
3. but with the correct numbers."""
        self.assertNotEqual(block_to_block_type(block), "paragraph")









if __name__ == "__main__":
    unittest.main()
