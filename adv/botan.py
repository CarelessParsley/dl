import adv_test
from adv import *
from module.bleed import Bleed

def module():
    return Botan

class Botan(Adv):
    a3 = ('prep','50%')
    def init(this):
        this.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(this, e):
        if random.random() < 0.8:
            Bleed("s1_bleed", 1.32).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=-2,mass=1)


