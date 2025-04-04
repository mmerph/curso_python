class Sport:
    '''Clase para representar un deporte
    '''
    def __init__(self, name: str, players: int, league: str):
        """Constructor de sport"""
        self.name = name
        if isinstance(players, int): #verificamos que players sea un entero
            self.players = players
        else: 
            self.players= int(players)
        self.league = league

    def __str__(self)-> str:
        """Representación en string del sport"""
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)-> str:
        """Representación en string de sport"""
        return f"Sport(name = '{self.name}', players = {self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        """Convertir Sport ro json"""
        return{"name":self.name, "players":self.players, "league":self.league}
    
if __name__== "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    print( )
    nfl = Sport("Football", 11, "NFL")
    lmp = Sport("Baseball", "9", "LMP")
    mlb= Sport("Baseball", 9, "MBL")
    lmx = Sport("Soccer", 11, "Liga Mx")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s] 

    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes: 
            file.write(repr(d)+"\n")
    sport_list=[]
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())

    #Escribiremos el archivo en formato JSON 
    import json 
    archivo_json = "deportes.json"
    #Convertir todos los deportes a formato JSON
    sports_json = [sport.to_json() for sport in sport_list]
    #Escribe la lista entera como un solo arreglo JSON
    with open(archivo_json, "w") as file:
        json.dump(sports_json, file, indent = 4)

    #Leemos el archivo JSON
    sport_list_json = []
    with open(archivo_json, "r") as file:
        sport_list_json = json.load(file)
    print(sport_list_json)
