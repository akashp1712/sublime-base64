import sublime
import sublime_plugin
import base64

class EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            randomized_text = base64.b64encode(bytes(region_text.strip(), encoding='utf-8')).decode("utf-8")
            self.view.replace(edit, region, str(randomized_text))


class DecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            randomized_text = base64.b64decode(bytes(region_text.strip(), encoding='utf-8')).decode("utf-8")
            self.view.replace(edit, region, str(randomized_text))
