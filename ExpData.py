import matplotlib.pyplot as plt



       E1= Expense.objects.filter(Category="Essential")
       E2= Expense.objects.filter(Category="Non-Essential")
       E1.include(sum('Amount'))
       E2.include(sum('Amount'))

Essential,NonEssential= 22630, 31690
fig, ax = plt.subplots()
ax.pie((Essential,NonEssential), labels=('Essential', 'Non-Essential'), autopct='%1.1f%%')
plt.show()