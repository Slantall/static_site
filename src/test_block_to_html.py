import unittest

from block_to_html import *

class TestBlockToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """### This *is the best* lesson **ever**!

```it has code blocks
that span multiple lines```

*random* text

>a quote 
>or two

1. A list
2. that is ordered.

* other lists

more ranodm text
oops typo, **not** going to fix that 

"""
        self.assertEqual(repr(markdown_to_html_node(markdown)), "ParentNode(div, [ParentNode(h3, [LeafNode(None, This , None), LeafNode(i, is the best, None), LeafNode(None,  lesson , None), LeafNode(b, ever, None), LeafNode(None, !, None)], None), ParentNode(code, [LeafNode(None, it has code blocks\nthat span multiple lines, None)], None), ParentNode(p, [LeafNode(i, random, None), LeafNode(None,  text, None)], None), ParentNode(blockquote, [LeafNode(None, a quote or two, None)], None), ParentNode(ol, [ParentNode(li, [LeafNode(None, A list, None)], None), ParentNode(li, [LeafNode(None, that is ordered., None)], None)], None), ParentNode(ul, [ParentNode(li, [LeafNode(None, other lists, None)], None)], None), ParentNode(p, [LeafNode(None, more ranodm text\noops typo, , None), LeafNode(b, not, None), LeafNode(None,  going to fix that, None)], None)], None)")










if __name__ == "__main__":
    unittest.main()