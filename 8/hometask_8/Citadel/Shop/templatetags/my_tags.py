from django import template

register = template.Library()


def mytag(string):
    new_string = ''
    print('mytag')
    for i in range(len(string)):
        new_string += string[i].upper() if i % 2 else string[i].lower()
    return new_string

register.filter('mytag', mytag)

if __name__ == '__main__':
    print(mytag('!!!!!!!!!!!!!!!!!!!!!!!'))
