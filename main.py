from motor_logico import MotorRutasIA

def ejecutar_sistema():
    # 1. Iniciamos el motor apuntando al archivo de rutas en el cual se encuentran todas las rutas del sistema de transporte.
    try:
        sistema = MotorRutasIA('rutas.csv')
    except Exception as e:
        print(f"❌ Error crítico al iniciar: {e}")
        return
    
    print("\n" + "="*50)
    print("   SISTEMA EXPERTO DE RUTAS - TRANS-IArthur Ibero")
    print("="*50)
    
    while True:
        print("\n(Escribe 'salir' para terminar)")
        origen = input("📍Ingresa tu estacion de Origen: ").strip()
        if origen.lower() == 'salir': 
            break
            
        destino = input("🏁 Ingresa tu estacion de destino: ").strip()
        if destino.lower() == 'salir': 
            break

        # 2. Llamamos al motor lógico
        resultado = sistema.buscar_mejor_ruta(origen, destino)

        # 3. Manejo de errores de entrada
        if resultado == "ERROR_NOMBRE":
            print("\n⚠️ ERROR: Una de las estaciones no se encuentra en la base de datos.")
            print("Asegúrate de usar tildes y mayúsculas (Ej: Portal Américas).")
        elif resultado is None:
            print("\n⚠️ No se encontró una ruta disponible entre esos puntos.")
        else:
            # 4. Impresión inteligente de la ruta
            print("\n🗺️  RUTA ÓPTIMA ENCONTRADA:")
            print("="*45)
            
            ruta_actual = ""
            
            for paso in resultado:
                # Solo informamos la ruta si es la primera o si cambió (trasbordo)
                if paso['ruta'] != ruta_actual:
                    ruta_actual = paso['ruta']
                    print(f"\n👉 En {paso['de']}, ahora toma la ruta: {ruta_actual}")
                    print("-" * 45)
                
                # Listamos la estación de llegada de cada tramo
                print(f"   • {paso['a']}")
            
            print("="*45)
            print("✅ ¡Has llegado a tu destino!")

if __name__ == "__main__":
    ejecutar_sistema()