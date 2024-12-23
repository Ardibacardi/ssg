import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode("h1", "this text", props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(type(node.props_to_html()), str)

    def test2(self):
        node = HTMLNode("h1", "this text", props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test3(self):
        node = HTMLNode("h1", "this text", props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(repr(node), f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})")

class TestLeafNode(unittest.TestCase):
    def test_single_tag_with_text(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_tag_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_raw_text_without_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_value_error_when_value_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "").to_html()

class TestParentNode(unittest.TestCase):
    def test_tag_with_children(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_tag_with_children_and_attributes(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    {"href": "https://www.google.com"}
)
        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_value_error_when_tag_is_none(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")]).to_html()
    
    def test_value_error_when_children_is_none(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()
    
    def test_value_error_when_children_is_empty_list(self):
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()



