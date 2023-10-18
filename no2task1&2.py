catholic_martyrs = ['Achileo Kiwanuka','Adolphus Ludigo','Mukasa','Ambrosius','Kibuuka',
'Anatoli', 'Kiriggwajjo','Andrew Kaggwa','Antanansio ','Bazzekuketta','Bruno ',
'Sserunkuuma','Charles Lwanga','Denis ','Ssebuggwawo ','Wasswa','Gonzaga Gonza','Gyavira Musoke','Yowana Mukiibi',
'Yusufu Lugalama','Zakayo Lubega','James', 'Buuzaabalyaawo','John Maria ',
'Muzeeyi','Joseph Mukasa','Kizito','Lukka ','Baanabakintu','Matiya Mulumba','Mbaga Tuzinde',
'Mugagga Lubowa','Mukasa ','Kiriwawanvu','Nowa Mawaggali','Ponsiano ','Ngondwe']
anglican_martyrs = ['Aaron Lubega','Apollo Kivebulaya','Eria Sebukyala','Fredrick Kizza','George Kizza','James Hannington',
'Janani Luwum','Joseph ','Balikuddembe','Kizito','Mark Kakumba','Matia Mulumba','Nuhu Mbegu','Robert ',
'Munyagayirwa','Samwiri Mukasa','Yefusa Namayanja','Yohana Mukasa','Yosefu Lugalama','Yowana Kitaka','Yowana Maria ','Mukasa']

print("catholic_martyrs:", catholic_martyrs)
print("anglican_martyrs:", anglican_martyrs)

#task2
#block of code that Identifies and removes any duplicate names present in both lists.

# Convert the lists to sets
set1 = set(catholic_martyrs)
set2 = set(anglican_martyrs)

# Find the common elements
common_names = set1.intersection(set2)

# Remove the common names from both lists
catholic_martyrs = list(set1 - common_names)
anglican_martyrs = list(set2 - common_names)

print("catholic_martyrs without duplicates:",catholic_martyrs )
print("anglican_martyrs without duplicates:", anglican_martyrs )


