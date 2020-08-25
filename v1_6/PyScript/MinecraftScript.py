#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import csv


def pyramid_script(start_point, width, materials):
    start_x, h, start_y = start_point
    end_x, h, end_y = start_x + width, h, start_y + width
    print("fill %d %d %d %d %d %d %s" % (start_x, h-1, start_y, end_x, h-1, end_y, materials))
    while end_x > start_x and end_y > start_y:
        print("fill %d %d %d %d %d %d %s" % (start_x, h, start_y, end_x, h, end_y, materials))
        print("fill %d %d %d %d %d %d air" % (start_x+1, h, start_y+1, end_x-1, h, end_y-1))
        start_x += 1
        end_x -= 1
        start_y += 1
        end_y -= 1
        h += 1
    print("fill %d %d %d %d %d %d %s" % (start_x, h, start_y, end_x, h, end_y, materials))


def pyramid_script2(width, materials):
    start_x, h, start_y = (0, 0, 0)
    end_x, h, end_y = start_x + width, h, start_y + width
    print("fill ~%d ~%d ~%d ~%d ~%d ~%d sealantern" % (start_x, h-1, start_y, end_x, h-1, end_y))
    while end_x > start_x and end_y > start_y:
        print("fill ~%d ~%d ~%d ~%d ~%d ~%d %s" % (start_x, h, start_y, end_x, h, end_y, materials))
        print("fill ~%d ~%d ~%d ~%d ~%d ~%d air" % (start_x+1, h, start_y+1, end_x-1, h, end_y-1))
        start_x += 1
        end_x -= 1
        start_y += 1
        end_y -= 1
        h += 1
    print("fill ~%d ~%d ~%d ~%d ~%d ~%d %s" % (start_x, h, start_y, end_x, h, end_y, materials))


def random_sand_script(width, hight):
    start_x, h, start_y = (0, 0, 0)
    for h in range(0, hight):
        random_x_p = random.randint(-width, 0)
        random_z_p = random.randint(-width, 0)
        random_x_p2 = random.randint(0, width)
        random_z_p2 = random.randint(0, width)
        print("fill ~%d ~%d ~%d ~%d ~%d ~%d sandstone" % (random_x_p, h, random_z_p, random_x_p2, h, random_z_p2))


def house_script(target_point):
    target_x, h, target_y = target_point
    print("/clone %d %d %d %d %d %d %d %d %d" % (-113, 72, 155, -99, 163, 136, target_x, h, target_y))


def city_house_script(target_point):
    # 一次只能操作的方块数量，不能超过32768
    target_x, h, target_y = target_point
    # 生成第一个房间
    end_x = target_x + 20
    end_y = target_y + 15
    end_h = h + 5
    print("/fill %d %d %d %d %d %d stonebrick" % (target_x, h, target_y, end_x, end_h, end_y))
    print("/fill %d %d %d %d %d %d air" % (target_x+1, h+1, target_y+1, end_x-1, end_h-1, end_y-1))
    # 生成门
    print("/fill %d %d %d %d %d %d air" % (target_x+9, h+1, target_y, target_x+10, h+2, target_y))
    print("/fill %d %d %d %d %d %d wooden_door" % (target_x+9, h+1, target_y+1, target_x+10, h+1, target_y+1))


def flat_block_script(width, length, materials):
    start_x, h, start_y = (0, 0, 0)
    end_x, h, end_y = start_x + width, h, start_y + length
    print("fill ~%d ~%d ~%d ~%d ~%d ~%d %s" % (start_x, h, start_y, end_x, h, end_y, materials))


def vertical_block_x_script(length, height, materials):
    start_x, h, start_y = (0, 0, 0)
    end_x, end_h, end_y = start_x + length, h+height, start_y
    print("fill ~%d ~%d ~%d ~%d ~%d ~%d %s" % (start_x, h, start_y, end_x, end_h, end_y, materials))


def vertical_block_y_script(length, height, materials):
    start_x, h, start_y = (0, 0, 0)
    end_x, end_h, end_y = start_x, h+height, start_y + length
    print("fill ~%d ~%d ~%d ~%d ~%d ~%d %s" % (start_x, h, start_y, end_x, end_h, end_y, materials))


def hai_script(width):
    flat_block_script(width, width, "stonebrick")
    print("fill ~ ~ ~ ~%d ~%d ~%d %s" % (width, 10, 0, "stonebrick"))
    print("fill ~ ~ ~ ~%d ~%d ~%d %s" % (0, 10, width, "stonebrick"))
    print("fill ~%d ~ ~ ~%d ~%d ~%d %s" % (width, width, 10, width, "stonebrick"))
    print("fill ~ ~ ~%d ~%d ~%d ~%d %s" % (width, width, 10, width, "stonebrick"))
    print("fill ~1 ~1 ~1 ~%d ~%d ~%d %s" % (width-1, 3, width-1, "water"))
    print("fill ~1 ~4 ~1 ~%d ~%d ~%d %s" % (width - 1, 6, width - 1, "water"))


def diyu_script():
    print("fill ~ 30 ~ ~100 30 ~100 obsidian")
    print("fill ~ 3 ~ ~100 3 ~100 obsidian")
    print("fill ~ 30 ~ ~ 3 ~100 obsidian")
    print("fill ~ 30 ~ ~ 3 ~100 obsidian")
    print("fill ~100 30 ~ ~100 3 ~100 obsidian")
    print("fill ~ 3 ~ ~100 30 ~ obsidian")
    print("fill ~ 3 ~100 ~100 30 ~100 obsidian")


def yuan_script():
    with open('E:/111.csv', encoding='gbk') as f:
        reader = csv.reader(f)
        header = next(reader)
        # print(header)
        for row in reader:
            print("fill ~%s ~ ~%s ~%s ~ ~%s stone" % (row[0], row[1], row[0], row[2]))


if __name__ == '__main__':
    # diyu_script()
    # pyramid_script2(80, "gold_block")
    # house_script((-113, 72, 108))
    # city_house_script((-188, 116, 451))
    # random_sand_script(100, 100)
    # flat_block_script(20, 10, "stonebrick")
    # vertical_block_x_script(20, 10, "stonebrick")
    # hai_script(100)
    yuan_script()
