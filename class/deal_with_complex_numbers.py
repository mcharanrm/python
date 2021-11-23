import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        complex_add = complex(self.real, self.imaginary) \
                        + complex(no.real, no.imaginary)
        return Complex(complex_add.real, complex_add.imag)
        
        
    def __sub__(self, no):
        complex_sub = complex(self.real, self.imaginary) \
                        - complex(no.real, no.imaginary)
        
        return Complex(complex_sub.real, complex_sub.imag)
        
    
    def __mul__(self, no):
        complex_mul = complex(self.real, self.imaginary) \
                        * complex(no.real, no.imaginary)
        
        return Complex(complex_mul.real, complex_mul.imag)
    
    def __truediv__(self, no):
        complex_div = complex(self.real, self.imaginary) \
                        / complex(no.real, no.imaginary)
        
        return Complex(complex_div.real, complex_div.imag)
        

    def mod(self):
        self.mod_real = abs(complex(self.real, self.imaginary))
        self.mod_imaginary = 0
        return Complex(self.mod_real, self.mod_imaginary)

    def __str__(self):
        
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
