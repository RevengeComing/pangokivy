from pythonforandroid.toolchain import Recipe, current_directory, shprint
from os.path import exists, join
import sh


class FribidiRecipe(Recipe):
    version = '1.0.5'
    url = 'https://github.com/fribidi/fribidi/releases/download/v{version}/fribidi-{version}.tar.bz2'

    def should_build(self, arch):
        if exists(join(self.get_build_dir(arch.arch), 'lib', '.libs', 'libfribidi.so')):
            return False
        return True

    def build_arch(self, arch):
        with current_directory(self.get_build_dir(arch.arch)):
            configure = sh.Command(
                './configure', self.get_build_dir(arch.arch))
            shprint(configure)
            shprint(sh.make, '-j5')
            shprint(sh.cp, '-L', join('lib', '.libs',
                                      'libfribidi.so'), self.ctx.libs_dir)


recipe = FribidiRecipe()
