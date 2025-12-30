import re
from dash import html

_ELEMENTS = {
	"h1": {
		"regex": r"^#+ .+",   # starts with # and then have space followed by at least one character
		"element": html.H1,
	},
	"h2": {
		"regex": r"^## .+",
		"element": html.H2,
	},
	"h3": {
		"regex": r"^### .+",
		"element": html.H3,
	},
	"h4": {
		"regex": r"^#### .+",
		"element": html.H4,
	},
	"h5": {
		"regex": r"^##### .+",
		"element": html.H5,
	},
	"h6": {
		"regex": r"^###### .+",
		"element": html.H6,
	},
	"bullets": {
		"regex": r"/- *+/",
		"element": html.Li,
	},
	"others": {
		"element": html.P,
	}
}

def detect_and_convert_to_dash(element):
	for tag in _ELEMENTS.values():
		if re.match(tag["regex"], element):
			return tag["element"](children=element)

def markdown_to_dash(markdown):
	# each element is one of H1, H2, or Paragraph
	elements = markdown.split("\n")
	
	# removing the whitespaces
	elements = [e.strip() for e  in elements]

	# stores the dash elements
	dash_list = []

	for e in elements:
		pass

if __name__ == "__main__":
	print(re.fullmatch(elements["heading"]["regex"], "# hello"))
	print(re.match(elements["heading"]["regex"], "## hello"))
	print(re.match(elements["heading"]["regex"], "#### hello"))
	print(re.match(elements["heading"]["regex"], "#hello"))

	example_markdown = """
		# This is a heading
		This is a paragraph 1
		This is a paragraph 2
		## This is Heading 2
		This is a paragraph
	"""
	print(markdown_to_dash(example_markdown))
