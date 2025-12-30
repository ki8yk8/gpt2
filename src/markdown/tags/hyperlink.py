import re
from dash import html

from ..factory import register_tag, BaseTag

@register_tag("hyperlink")
class Hyperlink(BaseTag):
	regex = r"^\[(.+?)\]\((.+?)\)"

	@classmethod
	def get_element(self, item):
		match = re.match(self.regex, item)

		if not match:
			return None
		
		group = match.groups()
		return html.A(children=group[0], href=group[1])