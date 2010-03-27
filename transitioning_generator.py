#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import xml.etree.cElementTree as ElementTree

if __name__ == '__main__':
    curdir = os.path.dirname(os.path.abspath(__file__))
    itens = os.listdir(curdir)
    root = ElementTree.Element('background')
    time_info = ElementTree.SubElement(root, 'starttime')
    year = ElementTree.SubElement(time_info, 'year')
    year.text = '2010'
    month = ElementTree.SubElement(time_info, 'month')
    month.text = '01'
    day = ElementTree.SubElement(time_info, 'day')
    day.text = '01'
    hour = ElementTree.SubElement(time_info, 'hour')
    hour.text = '00'
    minute = ElementTree.SubElement(time_info, 'minute')
    minute.text = '00'
    second = ElementTree.SubElement(time_info, 'second')
    images = [item for item in itens if item.lower().endswith('jpg')]
    image_count = len(images)
    cur_index = 0
    while cur_index < image_count:
        static = ElementTree.SubElement(root, 'static')
        duration = ElementTree.SubElement(static, 'duration')
        duration.text = '895.0'
        image_file = ElementTree.SubElement(static, 'file')
        image_file.text = os.path.join(curdir, images[cur_index])
        transiction = ElementTree.SubElement(root, 'transiction')
        transiction_duration = ElementTree.SubElement(transiction, 'duration')
        transiction_duration.text = '5.0'
        from_file = ElementTree.SubElement(transiction, 'from')
        from_file.text = os.path.join(curdir, images[cur_index])
        to_file = ElementTree.SubElement(transiction, 'to')
        if (cur_index + 1 == image_count):
            to_file.text = os.path.join(curdir, images[0])
        else:
            to_file.text = os.path.join(curdir, images[cur_index + 1])
        cur_index += 1
    bg_file = open('bg_file.xml', 'w')
    ElementTree.ElementTree(root).write(bg_file)
    bg_file.close()

