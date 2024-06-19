import os
import imagehash
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter


def find_duplicates_by_hash(*image_dirs: str) -> dict:
    '''
    Function to find duplicates by hash of images in directories
    :param image_dirs: directories with images
    :return: dictionary of duplicates with hash as keys and list of file paths as values
    '''
    image_hashes = {}

    for image_dir in image_dirs:
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                filepath = os.path.join(image_dir, filename)
                try:
                    with Image.open(filepath) as img:
                        hash = imagehash.average_hash(img)
                        if hash in image_hashes:
                            image_hashes[hash].append(filepath)
                        else:
                            image_hashes[hash] = [filepath]
                except Exception as e:
                    print(f"Error processing file {filepath}: {e}")

    return image_hashes


def visualize_duplicates(duplicates: dict):
    '''
    Function to visualize duplicates
    :param duplicates: dictionary of duplicates with hash as keys and list of file paths as values
    '''
    for hash, paths in duplicates.items():
        original = paths[0]
        duplicates = paths[1:]

        num_images = len(paths)
        fig, axes = plt.subplots(1, num_images, figsize=(5 * num_images, 5))

        axes[0].imshow(Image.open(original))
        axes[0].set_title(f'Original:\n{os.path.basename(original)}')
        axes[0].axis('off')

        for i, dup_path in enumerate(duplicates):
            axes[i + 1].imshow(Image.open(dup_path))
            axes[i + 1].set_title(f'Duplicate:\n{os.path.basename(dup_path)}')
            axes[i + 1].axis('off')

        plt.show()


def visualize_duplicate_stats(duplicates: dict):
    '''
    Function to visualize duplicate statistics
    :param duplicates: dictionary of duplicates with hash as keys and list of file paths as values
    '''
    num_duplicates = [len(paths) - 1 for paths in duplicates.values()]
    duplicate_counts = Counter(num_duplicates)

    plt.figure(figsize=(10, 5))
    plt.bar(duplicate_counts.keys(), duplicate_counts.values())
    plt.xlabel('Number of Duplicates')
    plt.ylabel('Number of Images')
    plt.title('Number of Images with Specific Number of Duplicates')
    plt.xticks(range(max(duplicate_counts.keys()) + 1))
    plt.show()


def save_duplicates_to_file(duplicates: dict, file_path: str):
    '''
    Function to save duplicates to a file
    :param duplicates: dictionary of duplicates with hash as keys and list of file paths as values
    :param file_path: path to the file where results will be saved
    '''
    with open(file_path, 'w') as file:
        for hash, paths in duplicates.items():
            original = paths[0]
            file.write(f'Original image: {original}\n')
            file.write(f'Number of duplicates: {len(paths) - 1}\n')
            for path in paths[1:]:
                file.write(f' - Duplicate: {path}\n')
            file.write('\n')


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


if __name__ == '__main__':
    main()
