import adv_test
import adv

def module():
    return D_Nefaria

class D_Nefaria(adv.Adv):
    a1 = ('s',0.25)

    def init(this):
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s3, fsc
                `fs, seq=4
                """


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

