# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))

print(hello_goodbye('Alice'))



