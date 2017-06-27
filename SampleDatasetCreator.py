import os
import glob
import random
import os.path
from shutil import copyfile
import typing
from termcolor import colored

'''
Creates a sample dataset by randomly copying a subset of the
images into the specified samples directory
'''
def copy_random_images(directory: str, to_dir: str, sample_size: float=0.20) -> None:
    dirs = [d for d in os.listdir(directory) if os.path.isdir(
        os.path.join(directory, d))]

    for d in dirs:
        files = glob.glob("{0}/{1}/{2}".format(directory, d,'*.jpg'))
        sample = random.sample(files, k=int(len(files) * sample_size))
        print(colored('{1}: {0} '.format(len(sample), d),  'blue'))
        copy_files(sample, to_dir + "/" + d + "/")


def copy_files(files: str , to_dir: str) -> None:
    os.makedirs(os.path.dirname(to_dir), exist_ok=True)
    for file in files:
        copyfile(file, to_dir +  os.path.basename(file))
        print(colored('coppied ' + file, "green"))
        
def mkdirs(path: str) -> None:
    [os.mkdir('{}/c{}'.format(path, i)) for i in range(10)]
               
def mv_valid(path: str) -> None:
    for i in range(10):
        d = 'c{}'.format(i)
        g = glob('{}/{}/*.jpg'.format(path, d))
        shuf = np.random.permutation(g)
        for i in range(200):
            os.rename(shuf[i], shuf[i].replace('train', 'valid'))
            

def main():
    copy_random_images(directory='./imgs/train/', to_dir='./sample/train/')


#Example usage
if __name__ == "__main__":
    main()
    print ("Done")
