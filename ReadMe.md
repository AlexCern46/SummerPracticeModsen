# Поиск дубликатов изображений

Скрипт для поиска дубликатов изображений в указанных директориях. Использует библиотеку `imagehash` для вычисления хэшей изображений и сравнения их друг с другом.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)
- [Источники](#источники)

## Технологии
- [Python](https://www.python.org/)
- [Pillow](https://python-pillow.org/)
- [Imagehash](https://github.com/JohannesBuchner/imagehash)
- [Matplotlib](https://matplotlib.org/)

## Начало работы

### Требования
Для работы скрипта необходимо установить Python 3 и следующие библиотеки:

```sh
$ pip install pillow imagehash matplotlib
```

## Использование
Скрипт можно использовать для поиска дубликатов изображений в двух указанных директориях. Для этого запустите скрипт командой:
    
```sh
$ python main.py
```

### Пример использования
Убедитесь, что директории с изображениями указаны корректно в функции `main()`:

```python
def main():
    image_dir1 = './5 Flower Types Classification Dataset-1/5 Flower Types Classification Dataset/Lilly'
    image_dir2 = './5 Flower Types Classification Dataset-1/5 Flower Types Classification Dataset/Lotus'
    image_hashes = find_duplicates_by_hash(image_dir1, image_dir2)

    duplicates = {hash: paths for hash, paths in image_hashes.items() if len(paths) > 1}

    if not duplicates:
        print("Duplicates not found")
    else:
        visualize_duplicate_stats(duplicates)
        save_duplicates_to_file(duplicates, 'duplicates.txt')
```

## Тестирование
Для тестирования скрипта создайте директории с изображениями и запустите скрипт. Убедитесь, что скрипт корректно находит дубликаты изображений.

## Contributing
Если вы хотите помочь в разработке проекта, вы можете:

* Отправить баг-репорт или предложение по улучшению.
* Сделать форк репозитория и отправить pull request с доработками.

## To do
- [x] Добавить поддержку дополнительных форматов изображений.
- [x] Добавить возможность работы с большим количеством директорий.
- [x] Добавить обработку ошибок.
- [ ] Добавить обработку изображений при помощи SIFT.
- [x] Добавить сохранение результатов в файл.
- [ ] Добавить модульные тесты.

## Команда проекта
Черняк Александр — Разработчик

## Источники
1. [Imagehash](https://github.com/JohannesBuchner/imagehash)
2. [Pillow](https://python-pillow.org/)
3. [Matplotlib](https://matplotlib.org/)