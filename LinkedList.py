#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:03:12 2019

@author: jimmy
"""
from collections import Iterable
# 初始化节点
class Node(object):
    def __init__(self,val,p=None):
        self.data = val
        self.next = p


class LinkedList(object):
    def __init__(self):
        # 初始化LinkedList类别，head节点为None
        self.head = None

    def __getitem__(self, key):
        # 链表是否为空
        if self.is_empty():
            raise ValueError('The LinkedList is empty.')


        elif key <0  or key > self.getlength():
            raise ValueError(f'The key must be 0-{self.getlength()}, while get the wrong key {key}.')
            

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            raise ValueError('The LinkedList is empty.')

        elif key <0  or key > self.getlength():
            raise ValueError(f'The key must be 0-{self.getlength()}, while get the wrong key {key}.')

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):
        if not isinstance(data,Iterable):
            raise TypeError('The data must be iterable.')
        
        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            raise ValueError('The LinkedList is empty.')
        
        j = 0
        p = self.head

        while p.next!= None and j < index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:
            raise IndexError('Index out of range.')

    def insert(self,index,item):

        if self.is_empty() or index < 0 or index > self.getlength():
            raise IndexError('Index out of range.')

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=None and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            raise ValueError('The LinkedList is empty.')

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=None and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            raise ValueError('The LinkedList is empty.')

        p = self.head
        i = 0
        while p.next!=None and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


l = LinkedList()
l.initlist([1,2,3,4,5])
print(l.getitem(4))
l.append(6)
print(l.getitem(5))

l.insert(4,40)
print(l.getitem(3))
print(l.getitem(4))
print(l.getitem(5))

l.delete(5)
print(l.getitem(5))

l.index(5)