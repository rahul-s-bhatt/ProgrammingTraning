import xml.etree.ElementTree as ET

contents = []
while True:
	line = input()
	if line == "</expr>":
	    contents.append(line)
	    break
	else:
		contents.append(line)

contents = list(filter(None, contents))

s = ''.join(contents)

root = ET.fromstring(s)

# compute = s.find('sum|div|prod|sub')

for child in root:
	c = child.tag
	if c == "sum":
		s = 0
		for compute in child.findall('.//elem'):
			s += int(compute.text)
		print(s)
	if c == "div":
		d = 0
		l = child.findall('.//elem')
		d += int(l[0].text) // int(l[1].text)
		print(d)
	if c == "sub":
		sub = 0
		l = child.findall('.//elem')
		l1 = int(l[0].text)
		for compute in child.findall('.//elem'):
			sub += int(compute.text)
		print(sub - l1)
	if c == "prod":
		p = 1
		for compute in child.findall('.//elem'):
			p *= int(compute.text)
		print(p)

"""

XML parse plus series computation

Evaluate an expression given in XML format. 
Keys will be Expr- contains the entire expression. 

Elem – contains the digit, sum, 

Prod- contains two or more keys whose evaluation needs
to be summed or multiplied respectively.

Sub will contain 2 keys or more, where the second key 
onwards will have to be subtracted from the first one. 

Div- will contain 2 keys in which first key will need
to be divided by second.

S i/p
<expr>

<sum>
<elem>4</elem>
<elem>6</elem>
</sum>

<div>
<elem>6</elem>
<elem>3</elem>
</div>

<sub>
<elem>10</elem>
<elem>3</elem>
<elem>3</elem>
</sub>

<prod>
<elem>2</elem>
<elem>3</elem>
<elem>5</elem>
</prod>

</expr>
"""