import interfaz
import busqueda
import vista


def main():
    #diccionario de las funciones de pila
    busqueda_centros = {
        "barra_busqueda" : busqueda.Barra_Busqueda,
        "mostrar_centro" : busqueda.mostrar_centro,
        "busqueda_key": busqueda.busqueda_key
    }

    interfaz_funciones = {
        "frame_scroll" : interfaz.Frame_scroll,
        "limpiar_frame" : interfaz.limpiar_frame,
        "eliminar_frame" : interfaz.elimnar_frame
    }

    vista.interfaz_principal(busqueda_centros, interfaz_funciones)


main()