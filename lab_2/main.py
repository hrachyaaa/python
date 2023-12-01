def gcd(a, b):
  while b:
      a, b = b, a % b
  return a

class Rational:
  def __init__(self, numerator, denominator):
      self.__numerator = numerator
      if denominator != 0:
          self.__denominator = denominator
      else:
          raise ValueError("Denominator should not be 0")

  def __add__(self, other):
      denominator = self.__denominator * other.__denominator
      numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
      g = gcd(numerator, denominator)
      numerator //= g
      denominator //= g
      result = Rational(numerator, denominator)
      return result

  def __sub__(self, other):
      denominator = self.__denominator * other.__denominator
      numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
      g = gcd(numerator, denominator)
      numerator //= g
      denominator //= g
      result = Rational(numerator, denominator)
      return result

  def __mul__(self, other):
      denominator = self.__denominator * other.__denominator
      numerator = self.__numerator * other.__numerator
      g = gcd(numerator, denominator)
      numerator //= g
      denominator //= g
      result = Rational(numerator, denominator)
      return result

  def __truediv__(self, other):
      numerator = self.__numerator * other.__denominator
      denominator = self.__denominator * other.__numerator
      g = gcd(numerator, denominator)
      numerator //= g
      denominator //= g
      result = Rational(numerator, denominator)
      return result

  def __eq__(self, other):
      return self.__numerator * other.__denominator == other.__numerator * self.__denominator

  def to_float(self):
      return self.__numerator / self.__denominator

  def __str__(self):
      return f"{self.__numerator} / {self.__denominator}"

rational1 = Rational(1, 2)
rational2 = Rational(3, 4)

result_add = rational1 + rational2
print(f"Addition: {rational1} + {rational2} = {result_add}")

result_sub = rational1 - rational2
print(f"Subtraction: {rational1} - {rational2} = {result_sub}")

result_mul = rational1 * rational2
print(f"Multiplication: {rational1} * {rational2} = {result_mul}")

result_div = rational1 / rational2
print(f"Division: {rational1} / {rational2} = {result_div}")

equality_check = rational1 == Rational(2, 4)
print(f"Equality check: {rational1} == {Rational(2, 4)} is {equality_check}")

float_value = rational1.to_float()
print(f"Float value of {rational1}: {float_value}")
