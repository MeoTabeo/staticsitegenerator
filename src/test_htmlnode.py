import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node1 = HTMLNode("p", "Text inside", None, {"href": "https://www.heise.de"})
        ret_str = node1.props_to_html()
        self.assertEqual(ret_str, ' href="https://www.heise.de"')

    def test_values(self):
        node = HTMLNode("div", "I wish I could read",)
        self.assertEqual(node.tag,"div",)
        self.assertEqual(node.value,"I wish I could read",)
        self.assertEqual(node.children,None,)
        self.assertEqual(node.props,None,)

    def test_repr(self):
        node = HTMLNode("p","What a strange world",None,{"class": "primary"},)
        self.assertEqual(node.__repr__(),"HTMLNode(p, What a strange world, None, {'class': 'primary'})",)


if __name__ == "__main__":
    unittest.main()