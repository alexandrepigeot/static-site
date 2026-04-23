import unittest

from extract import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):
	def test_markdown_images(self):
		self.assertEqual(
			[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
			extract_markdown_images(
				"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
			)
		)

	def test_markdown_links(self):
		self.assertEqual(
			[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
			extract_markdown_links(
				"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
			)
		)