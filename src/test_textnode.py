import unittest

from textnode import *
from htmlnode import *


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

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", "text")
        string = "LeafNode(None, This is a text node, None)"
        self.assertEqual(repr(text_node_to_html_node(node)), string)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", "bold")
        string = "LeafNode(b, This is a text node, None)"
        self.assertEqual(repr(text_node_to_html_node(node)), string)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", "italic")
        string = "LeafNode(i, This is a text node, None)"
        self.assertEqual(repr(text_node_to_html_node(node)), string)

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a code node", "code")
        string = "LeafNode(code, This is a code node, None)"
        self.assertEqual(repr(text_node_to_html_node(node)), string)

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a link node", "link", "www.google.com")
        string = "LeafNode(a, This is a link node, {'href': 'www.google.com'})"
        self.assertEqual(repr(text_node_to_html_node(node)), string)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", "image", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")





if __name__ == "__main__":
    unittest.main()