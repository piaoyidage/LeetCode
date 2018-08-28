/**
 * @author piaoyidage
 * @version 创建时间：2015-3-25 下午9:02:29
 *
 */	

	public boolean isMatch(String s, String p)
	{
		 // 参考C语言的实现方式
		 // 首先末尾追加#作为结束标志
		if (!s.contains(#))
		{
			s += #;
		}
		if (!p.contains(#))
		{
			p += #;
		}
		
		if (p.equals(#))
		{
			return s.equals(#);
		}
		
		 // 下一个字符不是‘’：匹配当前字符
		if (p.charAt(1) != '')
		{
			String subS = s.substring(1);
			String subP = p.substring(1);
			boolean b1 = (p.charAt(0) == s.charAt(0));
			boolean b2 = ((p.charAt(0) == '.') && !s.equals(#));
			boolean b3 = isMatch(subS, subP);
			return (b1  b2) && b3;
		}
		 // 下一个字符是‘’
		while((p.charAt(0) == s.charAt(0))  ((p.charAt(0) == '.') && !s.equals(#)))
		{
			if (isMatch(s, p.substring(2)))
			{
				return true;
			}
			s = s.substring(1);
		}
		return isMatch(s, p.substring(2));
	}
	