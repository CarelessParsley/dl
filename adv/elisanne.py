import adv_test
from adv import *
from slot.a import *

def module():
    return Elisanne

class Elisanne(Adv):
    comment = 'do not use fs & RR+15%buff_time'
    a1 = ('bt',0.25)

    conf = {
            'slots.a': RR() + Bellathorna()
            }



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)


