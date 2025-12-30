_TAGS_REGISTER = {}

# exposes decorator to create and register the tags
def register_tag(name):
	def inner(func):
		_TAGS_REGISTER[name] = func

	return inner

class Tag:
	def __init__(self):
		pass

	def get_element(self, item):
		pass

	def is_match(self, item):
		pass

if __name__ == "__main__":
	# defining a tag class
	@register_tag("heading")
	class HeadingTag(Tag):
		regex = "hello"

		@classmethod
		def is_match(self, item):
			return item == self.regex

	print(_TAGS_REGISTER)
	print(_TAGS_REGISTER["heading"].is_match("hello"))
	print(_TAGS_REGISTER["heading"].is_match("hi"))