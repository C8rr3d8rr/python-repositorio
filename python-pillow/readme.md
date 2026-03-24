
# ============================
# Libreria de Pillow
# ============================
# pip install pil

From PIL import Image, ImageChops, ImageEnhance, ImageOps
def main():
    image = Image.open("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Invertir colores.
    new_image = ImageChops.invert(image)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Escala de grises.
    new_image = ImageOps.grayscale(image)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Resaltar luces.
    new_image = ImageEnhance.Brightness(image).enhance(2)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Contraste.
    new_image = ImageEnhance.Contrast(image).enhance(4)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Espejo.
    new_image = ImageOps.mirror(image)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Cambiar tamaño.
    new_image = image.resize((320, 240))
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")

    # Diminuir nitidez.
    new_image = ImageEnhance.Sharpness(image).enhance(-4)
    new_image.save("/content/drive/MyDrive/Colab Notebooks/Pruebas/Bob.png")
if __name__ == "__main__":
    main()
