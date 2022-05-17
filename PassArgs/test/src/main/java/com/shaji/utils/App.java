package com.shaji.utils;

import java.io.FileInputStream;
import java.io.IOException;

public class App {
	
	public static void main(String[] args) throws IOException {
		
		String filePath = args[0];
		FileInputStream fi = new FileInputStream(filePath);
		byte[] b = new byte[fi.available()];
		fi.read(b);
		String s = new String(b);
		System.out.println(s);
	}

}
