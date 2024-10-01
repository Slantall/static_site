import unittest

from textnode import *
from markdown_convert import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        result = split_nodes_delimiter([node], "`", "code")

        expected =   [
        TextNode("This is text with a ", "text"),
        TextNode("code block", "code"),
        TextNode(" word", "text"),
    ]

        self.assertEqual(result, expected)


    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a *italic block* word", "text")
        result = split_nodes_delimiter([node], "*", "italic")

        expected =   [
        TextNode("This is text with a ", "text"),
        TextNode("italic block", "italic"),
        TextNode(" word", "text"),
    ]

        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a *italic block* word", "text")
        result = split_nodes_delimiter([node], "*", "italic")

        expected =   [
        TextNode("This is text with a ", "text"),
        TextNode("italic block", "italic"),
        TextNode(" word", "text"),
    ]

        self.assertEqual(result, expected)





class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded word", "bold"),
                TextNode(" and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
        self.assertListEqual(
            [
                TextNode("bold", "bold"),
                TextNode(" and ", "text"),
                TextNode("italic", "italic"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )


class TestImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)" 
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_images(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)


class TestSplitNodesImagesAndLinks(unittest.TestCase):
    def test_split_nodes_image1(self):
        text_node = TextNode("This is text with a image ![of boot dev](https://www.boot.gif) and [to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!", "text",)
        expected = "[TextNode(This is text with a image , text, None), TextNode(of boot dev, image, https://www.boot.gif), TextNode( and [to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!, text, None)]"
        self.assertEqual(expected, repr(split_nodes_image([text_node])))
    
    
    def test_split_nodes_image2(self):
        text_node = TextNode("This is text with a image ![of boot dev](https://www.boot.gif)", "text",)
        expected = "[TextNode(This is text with a image , text, None), TextNode(of boot dev, image, https://www.boot.gif)]"
        self.assertEqual(expected, repr(split_nodes_image([text_node])))

    def test_split_nodes_image3(self):
        text_node = TextNode("![of boot dev](https://www.boot.gif)", "text",)
        expected = "[TextNode(of boot dev, image, https://www.boot.gif)]"
        self.assertEqual(expected, repr(split_nodes_image([text_node])))

    def test_split_nodes_image4(self):
        self.maxDiff = None
        text_node = TextNode("This is text with a image ![of boot dev](https://www.boot.gif) and ![to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!", "text",)
        expected = "[TextNode(This is text with a image , text, None), TextNode(of boot dev, image, https://www.boot.gif), TextNode( and , text, None), TextNode(to youtube, image, https://www.youtube.com/@bootdotdev), TextNode(. Please visit us soon!, text, None)]"
        self.assertEqual(expected, repr(split_nodes_image([text_node])))



    def test_split_nodes_link1(self):
        text_node = TextNode("This is text with a link [of boot dev](https://www.boot.com) and ![to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!", "text",)
        expected = "[TextNode(This is text with a link , text, None), TextNode(of boot dev, link, https://www.boot.com), TextNode( and ![to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!, text, None)]"
        self.assertEqual(expected, repr(split_nodes_link([text_node])))
    

    def test_split_nodes_link2(self):
        text_node = TextNode("This is text with a link [of boot dev](https://www.boot.gif)", "text",)
        expected = "[TextNode(This is text with a link , text, None), TextNode(of boot dev, link, https://www.boot.gif)]"
        self.assertEqual(expected, repr(split_nodes_link([text_node])))

    def test_split_nodes_link3(self):
        text_node = TextNode("[of boot dev](https://www.boot.gif)", "text",)
        expected = "[TextNode(of boot dev, link, https://www.boot.gif)]"
        self.assertEqual(expected, repr(split_nodes_link([text_node])))

    def test_split_nodes_link4(self):
        self.maxDiff = None
        text_node = TextNode("This is text with a link [of boot dev](https://www.boot.gif) and [to youtube](https://www.youtube.com/@bootdotdev). Please visit us soon!", "text",)
        expected = "[TextNode(This is text with a link , text, None), TextNode(of boot dev, link, https://www.boot.gif), TextNode( and , text, None), TextNode(to youtube, link, https://www.youtube.com/@bootdotdev), TextNode(. Please visit us soon!, text, None)]"
        self.assertEqual(expected, repr(split_nodes_link([text_node])))







    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", "image", "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            "text",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
                TextNode(" and ", "text"),
                TextNode("another link", "link", "https://blog.boot.dev"),
                TextNode(" with text that follows", "text"),
            ],
            new_nodes,
        )



class TestSTextToTextnodes(unittest.TestCase):
    def test_split_links(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = "[TextNode(This is , text, None), TextNode(text, bold, None), TextNode( with an , text, None), TextNode(italic, italic, None), TextNode( word and a , text, None), TextNode(code block, code, None), TextNode( and an , text, None), TextNode(obi wan image, image, https://i.imgur.com/fJRm4Vk.jpeg), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]"
        self.assertEqual(repr(text_to_textnodes(text)), expected)



if __name__ == "__main__":
    unittest.main()
