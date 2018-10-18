from pythonforandroid.toolchain import Recipe, current_directory, shprint
from os.path import exists, join
import sh


class FontConfigRecipe(Recipe):
    version = '2.10.0'
    url = 'https://www.freedesktop.org/software/fontconfig/release/fontconfig-{version}.tar.bz2'

    def should_build(self, arch):
        if exists(join(self.get_build_dir(arch.arch), 'src', '.libs', 'libfontconfig.so')):
            return False
        return True

    def build_arch(self, arch):
        with current_directory(self.get_build_dir(arch.arch)):
            configure = sh.Command('./configure')
            shprint(configure)
            shprint(sh.make)

            shprint(sh.cp, '-L', join('src', '.libs',
                                      'libfontconfig.so'), self.ctx.libs_dir)


recipe = FontConfigRecipe()
