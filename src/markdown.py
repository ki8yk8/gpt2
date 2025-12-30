import re

elements = {
	"heading": {
		"regex": r"^#+ .+",   # starts with # and then have space followed by at least one character
		"element": None,
	},
	"bullets": {
		"regex": r"/- *+/",
		"element": None,
	},
	"others": {
		"element": None,
	}
}

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
