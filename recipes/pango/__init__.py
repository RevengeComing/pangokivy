from pythonforandroid.toolchain import Recipe, current_directory, shprint
from os.path import exists, join
import sh


class PangoRecipe(Recipe):
    version = '1.42.4'
    url = 'http://ftp.gnome.org/pub/gnome/sources/pango/1.42/pango-{version}.tar.xz'

    depends = ['harfbuzz', 'fontconfig2', 'freetype', 'fribidi']

    def should_build(self, arch):
        if exists(join(self.get_build_dir(arch.arch), 'pango', '.libs', 'libpango-1.0.so')):
            return False
        return True

    def build_arch(self, arch):
        with current_directory(self.get_build_dir(arch.arch)):
            configure = sh.Command('./configure')
            shprint(configure)
            shprint(sh.make)

            shprint(sh.cp, '-L', join('pango', '.libs',
                                      'libpango-1.0.so'), self.ctx.libs_dir)
            shprint(sh.cp, '-L', join('pango', '.libs',
                                      'libpangoft2-1.0.so'), self.ctx.libs_dir)
            shprint(sh.cp, '-L', join('pango', '.libs',
                                      'libpangoxft-1.0.so'), self.ctx.libs_dir)


recipe = PangoRecipe()
