#a function named martyr_count that takes in a martyr's name as an argument and returns the group (Catholic or Anglican) to which the martyr belongs.
def martyr_count():
    martyr_name = input("Please enter the martyr's name: ")

    catholic_martyrs = ['Achileo Kiwanuka','Adolphus Ludigo','Mukasa','Ambrosius','Kibuuka',
    'Anatoli', 'Kiriggwajjo','Andrew Kaggwa','Antanansio ','Bazzekuketta','Bruno ',
    'Sserunkuuma','Charles Lwanga','Denis ','Ssebuggwawo ','Wasswa','Gonzaga Gonza','Gyavira Musoke','Yowana Mukiibi',
    'Yusufu Lugalama','Zakayo Lubega','James', 'Buuzaabalyaawo','John Maria ',
    'Muzeeyi','Joseph Mukasa','Kizito','Lukka ','Baanabakintu','Matiya Mulumba','Mbaga Tuzinde',
    'Mugagga Lubowa','Mukasa ','Kiriwawanvu','Nowa Mawaggali','Ponsiano ','Ngondwe']
    anglican_martyrs = ['Aaron Lubega','Apollo Kivebulaya','Eria Sebukyala','Fredrick Kizza','George Kizza','James Hannington',
    'Janani Luwum','Joseph ','Balikuddembe','Kizito','Mark Kakumba','Matia Mulumba','Nuhu Mbegu','Robert ',
    'Munyagayirwa','Samwiri Mukasa','Yefusa Namayanja','Yohana Mukasa','Yosefu Lugalama','Yowana Kitaka','Yowana Maria ','Mukasa']

    if martyr_name in catholic_martyrs:
        return 'Catholic'
    elif martyr_name in anglican_martyrs:
        return 'Anglican'
    else:
        return 'Unknown'
    
group = martyr_count()
print("The martyr belongs to the", group, "group.")
    
    
#group of Kizito
    
#martyr_name = "Kizito"
#group = martyr_count(martyr_name)
#print(f"The martyr named '{martyr_name}' belongs to the {group} group.")    