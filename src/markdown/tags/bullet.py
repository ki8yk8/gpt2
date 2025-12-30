import re
from dash import html

from ..factory import register_tag, BaseTag

@register_tag("bullet_points")
class Bullet(BaseTag):
	regex = r"^- (.+)"

	@classmethod
	def get_element(self, item):
		match = re.match(self.regex, item)

		if match is None:
			return None

		return html.Li(children=html.Span(children=match.groups()[0]))