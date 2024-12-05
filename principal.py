import interfaz
import busqueda
import vista
import Centros
import Cuentas


def main():
    #diccionario de las funciones
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

    administrar_centros = {
        "editar_centro" : Centros.editar_centro,
        "eliminar_centro" : Centros.eliminar_centro,
        "crear_centro": Centros.crear_centro,
        "agregar_centro" : Centros.agregar_centro
    }

    administrar_cuentas = {
        "registrar_cuenta" : Cuentas.registrar_cuenta,
        "iniciar_sesion" : Cuentas.iniciar_sesion,
        "obtener_tipo" : Cuentas.obtener_tipo,
        "obtener_clave" : Cuentas.obtener_clave
    }

    vista.interfaz_principal(busqueda_centros, interfaz_funciones, administrar_centros, administrar_cuentas)


main()