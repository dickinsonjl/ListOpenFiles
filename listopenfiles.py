import sublime,sublime_plugin,os
from os.path import relpath

class ListOpenFilesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        views = window.views()

        fileNames = ''
        for view in views:
            if view and view.file_name():
                # fileNames += os.path.basename(view.file_name())+'\n'
                fileNames += self.getRelativePathOfFile(view.file_name())+'\n'

        window.new_file().insert(edit, 0, "List of open files:\n\n"+fileNames)

    def getRelativePathOfFile(self, filename):
        if len(filename) > 0:
            try :
                thePath = (
                    min(
                        (
                            relpath(filename, folder).replace("\\", "/")
                            for folder in sublime.active_window().folders()
                        ),
                        key=len,
                    )
                )
            except :
                thePath = filename
            return thePath
