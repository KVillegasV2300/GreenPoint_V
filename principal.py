import interfaz
import busqueda
import vista


def main():
    #diccionario de las funciones de pila
    busqueda_centros = {
        "busqueda_materiales" : busqueda.busqueda_materiales,
        "busqueda_key": busqueda.busqueda_key,
        "obtener_indices": busqueda.obtener_indices
    }

    interfaz_funciones = {
        "frame_scroll" : interfaz.Frame_scroll,
        "limpiar_frame" : interfaz.limpiar_frame,
        "eliminar_frame" : interfaz.elimnar_frame,
        "barra_busqueda" : interfaz.Barra_Busqueda,
        "mostrar_centro" : interfaz.mostrar_centro,
        "ocultar_frame" : interfaz.Barra_mostrar
    }

    vista.interfaz_principal(busqueda_centros, interfaz_funciones)


main()