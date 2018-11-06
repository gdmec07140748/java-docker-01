package com.xingen.classdemo;

public class Client {

    public static void main(String[] args) {
      createClassInstance();
    }

       /**
     * 创建Class类实例对象的三种方式
     */
    private static void createClassInstance() {
        ClassTest1.createClassInstance1();
        ClassTest1.createClassInstance2();
        ClassTest1.createClassInstance3();

    }
}