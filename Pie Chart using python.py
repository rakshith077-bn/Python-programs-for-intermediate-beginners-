import matplotlib.pyplot as plt

Partition = 'Eating', 'Travelling', 'Phone Bill', 'Micallaneous'
sizes = [250, 150, 100, 350]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = Partition, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('Equal')
plt.show()
