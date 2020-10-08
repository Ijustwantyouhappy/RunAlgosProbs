# -*- coding: utf-8 -*-
# @Time     : 2020/9/5 23:29
# @Author   : Run 
# @File     : hanota.py
# @Software : PyCharm


"""
References:
    1. [leetcode > 面试题 08.06. 汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci/)
"""


def hanota(n: int):
    """
    总共ABC3根柱子，初始时n个盘子放在柱子A上，从上到下越来越大，将其全部移动到柱子C
    注意：在整个移动的过程中，不能出现同一根柱子上大盘子放在小盘子之上的情况。
    :param n:
    :return:
    """
    stacks = [
        list(range(n, 0, -1)),
        [],
        []
    ]
    posts = 'ABC'

    def _play(x, y, n):
        # ABC3根柱子编号依次为0，1，2
        # 将上面n个盘子从柱子x移至柱子y
        if n == 1:
            print(f"[action] {posts[x]} -> {posts[y]}: {stacks[x][-1]}")
            stacks[y].append(stacks[x].pop())  # 通过栈实现
            print(f"[status] A: {stacks[0][::-1]}, B: {stacks[1][::-1]}, C: {stacks[2][::-1]}")
        else:
            z = 3 - x - y
            _play(x, z, n - 1)
            _play(x, y, 1)
            _play(z, y, n - 1)

    _play(0, 2, n)


if __name__ == "__main__":
    hanota(3)
    print()
    hanota(4)