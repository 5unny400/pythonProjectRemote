"""
@FileName：test2
@Description：
@Author：shenxinyuan
@Time：2025/1/17
"""


def match_args(args):
    match args:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')

args = ['gcc', 'hello.c', 'world.c']
match_args(args)

args = ['clean']
match_args(args)

args = ['gcc']
match_args(args)