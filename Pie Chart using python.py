import matplotlib.pyplot as plt
    
Partition = 'Restuaratns', 'Travelling', 'Shopping', 'Micallaneous'
sizes = [250, 100, 300, 200]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)         
ax1.axis('equal')
plt.show()