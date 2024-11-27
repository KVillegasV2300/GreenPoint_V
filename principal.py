import interfaz
import busqueda
import vista


def main():
    #diccionario de las funciones de pila
    busqueda_centros = {
        "barra_busqueda" : busqueda.Barra_Busqueda,
    }

    interfaz_funciones = {
        "frame_scroll" : interfaz.Frame_scroll,
        "limpiar_frame" : interfaz.limpiar_frame
    }

    vista.interfaz_principal(busqueda_centros, interfaz_funciones)


main()