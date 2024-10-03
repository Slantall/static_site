import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_repr_nothing(self):
        node = HTMLNode()
        string = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), string)

    def test_repr_tag(self):
        node = HTMLNode("b")
        string = "HTMLNode(b, None, None, None)"
        self.assertEqual(repr(node), string)

    def test_repr_value(self):
        node = HTMLNode(None, "no idea what value looks like")
        string = "HTMLNode(None, no idea what value looks like, None, None)"
        self.assertEqual(repr(node), string)

    def test_props_to_html(self):
        test_prop = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, test_prop)
        string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), string)


    def test_LeafNode_to_html1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        string = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), string)


    def test_LeafNode_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), string)




    def test_ParentNode_to_html1(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
        )
        string = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), string)


    def test_ParentNode_to_html2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
        ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        string = '<p><b>Bold text</b><p><i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), string)





    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()