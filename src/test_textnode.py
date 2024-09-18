import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_none_specified(self):
        node = TextNode("This is another text node", "bold", None)
        node2 = TextNode("This is another text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is another text node", "bold", "www.google.com")
        node2 = TextNode("This is another text node", "bold", "www.google.com")
        self.assertEqual(node, node2)

    def test_repr_no_url(self):
        node = TextNode("This is a text node", "bold")
        string = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), string)

    def test_repr_none_specified(self):
        node = TextNode("This is another text node", "bold", None)
        string = "TextNode(This is another text node, bold, None)"
        self.assertEqual(repr(node), string)

    def test_repr_with_url(self):
        node = TextNode("This is another text node", "bold", "www.google.com")
        string = "TextNode(This is another text node, bold, www.google.com)"
        self.assertEqual(repr(node), string)

    def test_non_eq_text(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is another text node", "bold", "www.google.com")
        self.assertNotEqual(node, node2)

    def test_non_eq_missing_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_non_eq_text_type(self):
        node = TextNode("This is a text node", "italic", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()