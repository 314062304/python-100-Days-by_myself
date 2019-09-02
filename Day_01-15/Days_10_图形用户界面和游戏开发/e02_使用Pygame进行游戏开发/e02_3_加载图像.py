#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()

    # 初始化用于显示的窗口与并设置窗口大小
    screen = pygame.display.set_mode((800, 600))

    # 设置当前窗口标题
    pygame.display.set_caption('大球吃小球')

    # 设置窗口背景色（颜色是由红绿蓝三原色构成的元组）
    screen.fill((255, 255, 255))

    # 通过执行的文件名加载图像
    ball_image = pygame.image.load('../ball.png')

    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))
    # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
    pygame.display.flip()

    running = True
    # 开启一个事件循环处理发生的事情
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()