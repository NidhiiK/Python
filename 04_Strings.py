course_a = 'Python for "Beginners"'
# output: Python for "Beginners"

course_b = "Pythons's Course for Beginners"
# output: Pythons's Course for Beginners

course_c = '''
Hi Nidhi,

Here is our first email to you.


Thank you,
The support team'''

print(course_a)
print(course_b)
print(course_c)

# In python negative index in arrays also exist. Eg: course_a[-1] = s and course_a[-2] = r.
# Negative indexing starts from backward.

print(course_a[0:3])
print(course_a[0:])
print(course_a[1:])
print(course_a[:5])  #[0:5]
print(course_a[:])

name = 'Jennifer'
print(name[1:-1])  #ennife
