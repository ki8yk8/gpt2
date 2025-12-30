import re
from dash import html

from ..factory import register_tag, BaseTag

@register_tag("paragraph_with_hyperlink")
class ParagraphWithHyperLink(BaseTag):
	hyperlink_at_last = r"(.+)(\[.+\]\(.+\))(.*)"
	hyperlink_at_first = r"(.*)(\[.+\]\(.+\))(.+)"
	hyperlink_regex = r"(\[.*\])(\(.*\))"
	regex = f"{hyperlink_at_last}|{hyperlink_at_first}"

	@classmethod
	def get_element(self, item):
		match = re.match(self.regex, item)

		if not match:
			return None

		dash_html = []

		groups = match.groups()
		for g in groups:
			if g is None or len(g) == 0:
				continue
			elif re.match(self.hyperlink_regex, g.strip()):
				(text, link) = re.match(self.hyperlink_regex, g.strip()).groups()
				text, link = text[1:-1], link[1:-1]
				dash_html.append(html.A(children=[text], href=link))
			else:
				dash_html.append(html.Span(children=g))
		
		return html.P(children=dash_html)