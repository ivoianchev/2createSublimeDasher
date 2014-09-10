import sublime, sublime_plugin, re

class DasherToggleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        for region in regions:
            region = view.word(region)
            replace_string = ""
            new_line = ""
            substr = view.substr(region)
            newline_split = re.split("\n", substr)
            
            for line in newline_split:
                # check if we have dash - remove dash and titlecase
                if line.find("-") != -1:
                    new_line = line.replace('-', ' ')
                    new_line = self.title_case(new_line);
                # add dash
                else:
                    new_line = line.replace(' ', '-')
                    new_line = new_line.lower()


                if replace_string != "":
                    replace_string += "\n"
                replace_string += new_line

            view.replace(edit, region, replace_string)

    def title_case(self, string):
        split_str = re.split(" ", string)
        out = []
        for word in split_str:
            out.append(word.capitalize())
        return " ".join(out)