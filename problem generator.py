import random
import math

def problem():
	form = ["треугольник", "квадрат", "прямоугольник"]
	quest = ["площадь", "периметр"]
	
	prob_f = random.choice(form)
	prob_q = random.choice(quest)
	
	a=""
	b=""
	c=""
	
	if prob_f == "треугольник":
		a=random.randint(1, 30)
		b=random.randint(1, 40)
		c=random.randint(1, 50)
		text=f"Вам дан {prob_f}, со сторонами {a}, {b}, {c}. Найдите {prob_q} фигуры."
		p2=a+b+c
		p=p2/2
		sq=int(eval(f"{p}*({p}-{a})*({p}-{b})*({p}-{c})"))
		print(text)
		if sq<1:
			print("Ответ: такого треугольника не существует")
		else:
			sqrt=math.sqrt(sq)
			if prob_q == "площадь":
				print(f"Ответ: {sqrt}")
			elif prob_q == "периметр":
				print(f"Ответ: {p2}")
	
	if prob_f == "квадрат":
		a=random.randint(1, 50)
		text=f"Вам дан {prob_f}, со стороной {a}. Найдите {prob_q} фигуры."
		p2=a*4
		sq=a**2
		print(text)
		if prob_q == "площадь":
			print(f"Ответ: {sq}")
		elif prob_q == "периметр":
			print(f"Ответ: {p2}")
	
	if prob_f == "прямоугольник":
		a=random.randint(1, 40)
		b=random.randint(1, 50)
		text=f"Вам дан {prob_f}, со сторонами {a}, {b}. Найдите {prob_q} фигуры."
		p2=2*a+2*b
		sq=a*b
		print(text)
		if prob_q == "площадь":
			print(f"Ответ: {sq}")
		elif prob_q == "периметр":
			print(f"Ответ: {p2}")

for i in range(10):
	problem()
	print("\n\n")