import unittest
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.request import ProxyHandler, Request, build_opener


class _AccountControlParser(HTMLParser):
    """Finds <a> or <button> controls whose visible text contains 'account'."""

    def __init__(self):
        super().__init__()
        self._tag_stack = []
        self._text_stack = []
        self.found_account_control = False

    def handle_starttag(self, tag, attrs):
        if tag in {"a", "button"}:
            self._tag_stack.append(tag)
            self._text_stack.append([])
        elif self._tag_stack:
            # Keep collecting nested text within the current <a>/<button>.
            self._tag_stack.append(tag)

    def handle_data(self, data):
        if self._text_stack:
            self._text_stack[-1].append(data)

    def handle_endtag(self, tag):
        if not self._tag_stack:
            return

        if tag == self._tag_stack[-1]:
            self._tag_stack.pop()

        # Close tracked <a>/<button> elements and evaluate their combined text.
        if tag in {"a", "button"} and self._text_stack:
            text = " ".join(self._text_stack.pop()).strip().lower()
            if "account" in text:
                self.found_account_control = True


class TestOrthazoneAccountButton(unittest.TestCase):
    def test_account_button_exists(self):
        request = Request(
            "https://orthazone.com",
            headers={"User-Agent": "Mozilla/5.0"},
        )

        # Use a no-proxy opener first to avoid environment proxy tunneling issues.
        opener = build_opener(ProxyHandler({}))
        try:
            with opener.open(request, timeout=20) as response:
                html = response.read().decode("utf-8", errors="ignore")
        except URLError as exc:
            self.skipTest(f"Network unavailable for https://orthazone.com: {exc}")

        parser = _AccountControlParser()
        parser.feed(html)

        self.assertTrue(
            parser.found_account_control,
            msg='Expected to find an "Account" button/link on https://orthazone.com',
        )


if __name__ == "__main__":
    unittest.main()
