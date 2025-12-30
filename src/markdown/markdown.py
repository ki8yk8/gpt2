from dash import html

from .factory import get_register_tags

def markdown_to_dash(markdown):
	# each element is one of H1, H2, or Paragraph
	elements = markdown.split("\n")
	
	# removing the whitespaces
	elements = [e.strip() for e in elements]
	elements = [e for e in elements if len(e) > 0]

	# stores the dash elements
	dash_list = []
	temp_bullet_list = []
	tags = get_register_tags()
	for e in elements:
		# see if any tag is matched or not
		for name, tag in tags.items():
			if tag.is_match(e):
				if name == "bullet_points":
					temp_bullet_list.append(tag.get_element(e))
				else:
					if not len(temp_bullet_list) == 0:
						dash_list.append(html.Ul(children=[*temp_bullet_list]))
						temp_bullet_list.clear()

					dash_list.append(tag.get_element(e))
				break
		else:
			# if none of tag matches than it is simply a paragraph
			dash_list.append(html.P(children=e))

	return html.Section(children=dash_list)

if __name__ == "__main__":
	example_markdown = """
		# This is a heading
		This is a paragraph 1
		This is a paragraph 2
		## This is Heading 2
		This is a paragraph
	"""
	print(markdown_to_dash(example_markdown))
