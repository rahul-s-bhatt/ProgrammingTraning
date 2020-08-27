// http://codeforces.com/contest/112/problem/A

import java.util.*;
import java.lang.*;
import java.io.*;


public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String s1 = sc.next();
		String s2 = sc.next();
		
		s1=s1.toLowerCase();
		s2=s2.toLowerCase();
		
		int n=s1.compareTo(s2);
		
		if(n==0) System.out.print("0");
		else if(n>0) System.out.print("1");
		else System.out.print("-1");
	}
}