from collections import namedtuple


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        CN = namedtuple('CN', ['real', 'img'])

        def parse_cn(cn):
            real, img = cn.split("+")

            real = int(real)
            try:
                img = int(img[:-1])
            except ValueError:
                img = 0

            return CN(real=real, img=img)

        a, b = parse_cn(a),  parse_cn(b)
        result = CN(
            real=(a.real * b.real - (a.img * b.img)),
            img=(a.real * b.img + a.img * b.real)
        )

        return "%d+%di" % (result.real, result.img)
