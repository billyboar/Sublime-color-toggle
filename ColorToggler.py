import sublime, sublime_plugin
import time

class ColorChangerCommand(sublime_plugin.TextCommand):
    def run(self, *args):
        for arg in args:
            print (arg)
        self.change_color()
    
    def change_color(self):
        #current_hour = time.localtime().tm_hour
        settings = sublime.load_settings("Preferences.sublime-settings")
        time = settings.get("time")
        if time == "night":
            settings.set("color_scheme", "Packages/Color Scheme - Default/Mac Classic.tmTheme")
            settings.set("time", "day")
        else:
            settings.set("color_scheme", "Packages/Base16 Color Schemes/base16-colors.dark.tmTheme")
            settings.set("time", "night")
            
        #if current_hour < 20 and current_hour > 8:
            #settings.set("color_scheme", "Packages/Color Scheme - Default/Mac Classic.tmTheme")
        #else:
            #settings.set("color_scheme", "Packages/Base16 Color Schemes/base16-colors.dark.tmTheme")
        sublime.save_settings("Preferences.sublime-settings")
        #print(settings.has("time"))