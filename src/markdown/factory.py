import re

_TAGS_REGISTER = {}

# exposes decorator to create and register the tags
def register_tag(name):
	def inner(func):
		_TAGS_REGISTER[name] = func

	return inner

class BaseTag:
	def __init__(self):
		pass
	
	@classmethod
	def get_element(self, item):
		pass

	@classmethod
	def is_match(self, item):
		return bool(re.match(self.regex, item))

if __name__ == "__main__":
	# defining a tag class
	@register_tag("heading")
	class HeadingTag(BaseTag):
		regex = "# .+"

	print(_TAGS_REGISTER)
	print(_TAGS_REGISTER["heading"].is_match("# hello"))
	print(_TAGS_REGISTER["heading"].is_match("hi"))