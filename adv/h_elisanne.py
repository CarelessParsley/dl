import adv_test
from adv import *

def module():
    return H_Elisanne

class H_Elisanne(Adv):
    a1 = ('s',0.3)

    def init(this):
        this.stance = 0
        if this.condition("no s2"):
            this.conf['acl'] = """
                `s1, seq=5 and cancel
                `s3, seq=5 and cancel
                """

    def s1latency(this, e):
        Teambuff("s1_buff",0.1,15).on()

    def s1_proc(this, e):
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            Timer(this.s1latency).on(2.5)
            this.stance = 2
        elif this.stance == 2:
            Timer(this.s1latency).on(2.5)
            this.stance = 0

    def s2_proc(this, e):
        this.charge('s2',500)



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    adv_test.test(module(), conf, verbose=0)

    #module().comment = 'do not use s2'
    #conf['acl'] = """
    #    `s1, seq=5 and cancel
    #    `s3, seq=5 and cancel
    #    """
    #adv_test.test(module(), conf, verbose=0)
