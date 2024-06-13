import os
import imagehash
from PIL import Image


def find_duplicates(*image_dirs):
    duplicates = []
    image_hashes = {}

    for image_dir in image_dirs:
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                filepath = os.path.join(image_dir, filename)
                try:
                    image = Image.open(filepath)
                    image_hash = imagehash.average_hash(image)
                    if image_hash not in image_hashes:
                        image_hashes[image_hash] = [filepath]
                    else:
                        duplicates.append((filepath, image_hashes[image_hash][0]))
                except Exception as e:
                    print(f"Ошибка при обработке изображения {filename}: {e}")

    return duplicates


def main():
    image_dir1 = './5 Flower Types Classification Dataset-1/5 Flower Types Classification Dataset/Lilly'
    image_dir2 = './5 Flower Types Classification Dataset-1/5 Flower Types Classification Dataset/Lotus'
    duplicates = find_duplicates(image_dir1, image_dir2)

    if not duplicates:
        print("Дубликатов не найдено")
    else:
        for duplicate in duplicates:
            print(f"Найден дубликат: {duplicate[0]} и {duplicate[1]}")


if __name__ == '__main__':
    main()
