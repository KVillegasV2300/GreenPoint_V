# Lista de materiales reciclables
materiales_reciclables = [
    "Escombros", "Desechos vegetales", "Aceites y grasas", "Plásticos", "Papel", "Cartón",
    "Vidrio", "Metales", "Electrónicos", "Cascajo", "Aceites usados"
]

centros =[] #Arreglo de centro donde estaran 

# Datos de los centros de reciclaje (temporal)
centros_reciclaje = [
    {
        "nombre": "Planta de Reciclaje CIREC Miguel Hidalgo",
        "direccion": "Calle 5 de mayo #150, Col. San Lorenzo Tlaltenango",
        "materiales": ["Escombros", "Desechos vegetales", "Aceites y grasas"],
        "precios":[2,2,4],
        "horarios": "Lunes a viernes: 8:00 am - 6:00 pm",
        "link": "https://maps.app.goo.gl/9hYGHAfP6suBogjm7",
        "key" : "1234"
    },
    {
        "nombre": "Centro de Acopio de Residuos Reciclables (CAMH)",
        "direccion": "Alcaldía Miguel Hidalgo, CDMX",
        "materiales": ["Plásticos", "Papel", "Cartón", "Vidrio", "Metales", "Electrónicos"],
        "precios":[5,3,4,3,9,9],
        "horarios": "Lunes a sábado: 9:00 am - 5:00 pm",
        "link": "https://maps.app.goo.gl/tiqugsXU9aGtLm2d9", 
        "key" : "1234"
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "materiales": ["Cascajo", "Residuos vegetales", "Aceites usados"],
        "precios":[2,3,4],
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "link": "https://maps.app.goo.gl/YAnK9pS8ohp5YUC46",
        "key" : "1908"
    },
    {
        "nombre": "Centro de Reciclaje Avenida Juárez",
        "direccion": "Avenida Juárez, Miguel Hidalgo",
        "materiales": ["Aceites y grasas", "Plásticos", "Papel", "Cartón"],
        "precios":[3,3,9],
        "horarios": "Lunes a viernes: 7:00 am - 4:00 pm",
        "link": "https://maps.app.goo.gl/C1YjxMGiC8iMZ4GWA",
        "key" : "3456"
    }
]

#meter todo en un array :) (temporal)
for i in centros_reciclaje:
        centros.append(i)
        print(i['nombre'])
