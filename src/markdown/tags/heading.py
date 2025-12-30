import re
from dash import html

from ..factory import register_tag, BaseTag

@register_tag("heading")
class Heading(BaseTag):
	regex = "^(#+)? (.+)?"

	@classmethod
	def get_element(self, item):
		match = re.match(self.regex, item)

		# if different element donot proceed
		if not match:
			return None
		
		group = match.groups()

		match group[0]:
			case "#":
				return html.H1(children=group[1])
			case "##":
				return html.H2(children=group[1])
			case "###":
				return html.H3(children=group[1])
			case "####":
				return html.H4(children=group[1])
			case "#####":
				return html.H5(children=group[1])
			case "######":
				return html.H6(children=group[2])
			case _:
				# if greater than H6 than return P with all the hashtags
				return html.P(children=item)

if __name__ == "__main__":
	print(Heading.get_element("# Heading 1"))
	print(Heading.get_element("### Heading 2"))