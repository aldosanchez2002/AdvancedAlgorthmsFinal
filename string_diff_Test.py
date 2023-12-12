#Test file for string_diff.py
# Aldo Sanchez - 12/11/2023
# UTEP CS5350 Advanced Algorithms - Code for Final Exam
from string_diff import generate_edit_list, apply_edit_list, edit_list_cheaper

# Testcases from the exam
examTestcases_input = [ ("Hello", "Hello"),
                        ("Hello", "Hola"),
                        ("Do you want to marry me, Christina?", "I wish you merry Christmas!"),
                        ("Hello, Hello! How are you?", "Hello! How are you?"),
                        ("",""),
                        ("","A"),
                        ("Happy Holidays!","!Felices Fiestas!"),
                       ]
for index,testcase in enumerate(examTestcases_input):
    response = generate_edit_list(testcase[0], testcase[1])
    print(testcase,response)
    print(f"\t{testcase} {len(response)}\n\t\t", "\n\t\t ".join([str(edit) for edit in response]))


# AI genereated test set
# I maunally traced trough 10 examples
# I could not come up with a shorter solution than the one in the output so i assume it to be true

testcases_input = [
    ("Italy", "Pizza"),
    ("France", "EiffelTower"),
    ("India", "TajMahal"),
    ("Brazil", "Carnival"),
    ("UnitedStates", "Hollywood"),
    ("China", "GreatWall"),
    ("Australia", "SydneyOperaHouse"),
    ("Canada", "MapleSyrup"),
    ("Egypt", "Pyramids"),
    ("Mexico", "Tacos"),
    ("Greece", "Acropolis"),
    ("SouthAfrica", "Safari"),
    ("Russia", "Kremlin"),
    ("Spain", "FlamencoDance"),
    ("Germany", "Oktoberfest"),
    ("UnitedKingdom", "Shakespeare"),
    ("SouthKorea", "Kpop"),
    ("Argentina", "Tango"),
    ("Sweden", "ABBA"),
    ("Netherlands", "Tulips"),
    ("Thailand", "PadThai"),
    ("Switzerland", "SwissWatches"),
    ("Portugal", "PortWine"),
    ("Iran", "Persepolis"),
    ("NewZealand", "KiwiFruit"),
    ("Iceland", "NorthernLights"),
    ("Morocco", "SaharaDesert"),
    ("Peru", "MachuPicchu"),
    ("Cuba", "Cigars"),
    ("Kenya", "MaasaiMara"),
    ("Norway", "NorthernFjords"),
    ("Chile", "EasterIsland"),
    ("Indonesia", "Borobudur"),
    ("Turkey", "HagiaSophia"),
    ("Vietnam", "Pho"),
    ("Denmark", "LEGO"),
    ("India", "Bollywood"),
    ("Jamaica", "ReggaeMusic"),
    ("Poland", "Pierogi"),
    ("SaudiArabia", "Petra"),
    ("Maldives", "WhiteSandBeaches"),
    ("Austria", "ViennaPhilharmonic"),
    ("Ireland", "GuinnessBeer"),
    ("Malaysia", "PetronasTowers"),
    ("CzechRepublic", "PragueCastle"),
    ("Hungary", "Goulash"),
    ("Mongolia", "GobiDesert"),
    ("Finland", "NorthernLights"),
    ("Madagascar", "BaobabTrees")
]
testcases_output = [3, 3, 3, 2, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 4, 3, 2, 2, 2, 5, 2, 4, 4, 6, 4, 2, 3, 2, 2, 3, 4, 2, 2, 2, 3, 5, 3, 2, 2, 4, 3, 5, 4, 6, 6, 4, 7]

for index,testcase in enumerate(testcases_input):
    response = generate_edit_list(testcase[0], testcase[1])
    assert len(response) == testcases_output[index], f"Testcase {testcase} failed. Expected {testcases_output[index]} but got {len(response)}"
    print(f"\t{testcase}"," "*(30-len(testcase[0])-len(testcase[1])),f"{len(response)}\n\t\t", "\n\t\t ".join([str(edit) for edit in response]))
print("ALL TESTCASES PASSED")



# I believe there is a bug in the exam testcases
edit_list_aldo = generate_edit_list("Do you want to marry me, Christina?", "I wish you merry Christmas!")
edit_list_exam = [('d', 0, 2), ('d', 5, 8), ('d', 6, 1), ('d', 10, 4), ('d', 16, 2), ('d', 17, 1), ('i', 17, 's!'), ('i', 16, 'm'), ('i', 6, 'e'),('i',1,'wish '), ('i',0,'I')]
compared = edit_list_cheaper(edit_list_aldo, edit_list_exam)
print(compared)

print("Aldo\nDo you want to marry me, Christina? Edit Length", len(edit_list_aldo), "\n",apply_edit_list("Do you want to marry me, Christina?", edit_list_aldo))
print("Exam\nDo you want to marry me, Christina? Edit Length", len(edit_list_exam), "\n",apply_edit_list("Do you want to marry me, Christina?", edit_list_exam))