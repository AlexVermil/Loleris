autod = {
    "auto1" : {
        "nimi" : "Ford Mustang",
        "aasta" : 2009
    }
    "auto2" : {
        "nimi" : "Rimac Concept_Two",
        "aasta" : 2020
    }
    "auto3" : {
        "nimi" : "Koenigsegg One:1",
        "aasta" : 2014    
}
int(input("Sisestage auto aasta: "))

if input(2009):
    print(autod.get("aasta"))