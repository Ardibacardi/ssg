import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is an image", TextType.IMAGE, "image.com")
        node2 = TextNode("This is an image", TextType.IMAGE, "image.com")
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is an image", TextType.IMAGE, "image.com")
        node2 = TextNode("This is an image", TextType.IMAGE)
        self.assertNotEqual(node, node2)

class Test_text_node_to_html_node(unittest.TestCase):
    def test_bold_text(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_code_text(self):
        text_node = TextNode("Code text", TextType.CODE)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<code>Code text</code>")

    def test_image_text(self):
        text_node = TextNode("Image text", TextType.IMAGE, "image.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), '<img src="image.com" alt="Image text"/>')

    def test_italic_text(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_link_text(self):
        text_node = TextNode("Link text", TextType.LINK, "link.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), '<a href="link.com">Link text</a>')

    def test_normal_text(self):
        text_node = TextNode("Normal text", TextType.TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "Normal text")

    def test_value_error_when_text_type_is_invalid(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid text", "invalid"))

    def test_value_error_when_text_type_is_none(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid text", None))

if __name__ == "__main__":
    unittest.main()