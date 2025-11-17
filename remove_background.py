#!/usr/bin/env python3
"""
Script para remover el fondo de Vivi.jpeg usando rembg
Requiere: pip install rembg[new]
"""

import os
from pathlib import Path

def remove_background():
    """Remueve el fondo de Vivi.jpeg usando rembg"""
    try:
        from rembg import remove
        from PIL import Image
    except ImportError:
        print("❌ Error: rembg no está instalado")
        print("📦 Instala con: pip install rembg[new] pillow")
        return False
    
    input_path = Path(__file__).parent / "Vivi.jpeg"
    output_path = Path(__file__).parent / "Vivi_no_bg.png"
    
    if not input_path.exists():
        print(f"❌ Error: No se encontró {input_path}")
        return False
    
    print(f"🔄 Procesando {input_path}...")
    
    try:
        # Leer imagen
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        
        # Remover fondo
        print("🎨 Removiendo fondo...")
        output_data = remove(input_data)
        
        # Guardar resultado
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
        
        print(f"✅ Fondo removido exitosamente!")
        print(f"📁 Archivo guardado en: {output_path}")
        print(f"💡 Ahora puedes usar 'Vivi_no_bg.png' en la página")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al procesar imagen: {e}")
        return False

if __name__ == "__main__":
    remove_background()

