"""
Alumno: Nava Villagrana Brian Ulises
No. Control: 19211692
Practica: Hola Mundo
"""

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Configuración de la pantalla OLED y pines I2C
pix_res_x = 128
pix_res_y = 64
scl_pin = 27
sda_pin = 26

def init_i2c(scl_pin, sda_pin):
    # Inicializa el dispositivo I2C
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
    return i2c_dev

def display_text(oled, text, x, y):
    # Limpia la pantalla
    oled.fill(0)
    # Muestra el texto en la posición (x, y)
    oled.text(text, x, y)
    oled.show()

def main():
    i2c_dev = init_i2c(scl_pin, sda_pin)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    
    text_to_display = "Hola, mundo!"
    x_position = 20  # Posición en el eje X
    y_position = 30  # Posición en el eje Y
    
    display_text(oled, text_to_display, x_position, y_position)

if __name__ == '__main__':
    main()
