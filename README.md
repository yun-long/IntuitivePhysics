# IntuitivePhysics
To learn the intuitive physics from videos by using Deep Learning Neural Networks


## GANs Structure
<img src="https://github.com/yun-long/IntuitivePhysics/tree/master/Tutorials/figures/my_Structure.jpg" width="50%" />

## Generator
<img src="https://github.com/yun-long/IntuitivePhysics/tree/master/Tutorials/figures/my_Generator.jpg" width="50%" />

## Discriminator
<img src="https://github.com/yun-long/IntuitivePhysics/tree/master/Tutorials/figures/my_Discriminator.jpg" width="50%" />


## Usage
1. Clone or download this repository.
2. Prepare your data:
    - Preprocess your video data so that they are directories of frame sequences as structured below. (Neither the names nor the image extensions matter, only the structure):
    ```
    - Train
        - Video 1
            - frame ...
        - Video ...
        - Video N
            - frame ...
    - Test
        - Video 1
            - frame1.png
            - frame2.png
            - frame ...
            - frameN.png
        - Video ...
        - Video N


    ```
3. Process training data:
    - The network trains on random 32x32 pixel crops of the input images, filtered to make sure that most clips have some movement in them. To process your input data into this form, run the script `python process_data` from the `Code/` directory with the following options:
    ```
    -n/--num_clips= <# clips to process for training> (Default = 5000000)
    -t/--train_dir= <Directory of full training frames>
    -c/--clips_dir= <Save directory for processed clips>
                    (I suggest making this a hidden dir so the filesystem doesn't freeze
                    with so many files. DON'T `ls` THIS DIRECTORY!)
    -o/--overwrite  (Overwrites the previous data in clips_dir)
    -H/--help       (prints usage)
    ```
    - This can take a few hours to complete, depending on the number of clips you want.

4. Train/Test:
    - If you want to plug-and-play with the Ms. Pac-Man dataset, you can [download my trained models here](https://drive.google.com/open?id=0Byf787GZQ7KvR2JvMUNIZnFlbm8). Load them using the `-l` option. (e.g. `python avg_runner.py -l ./Models/Adversarial/model.ckpt-500000`).
    - Train and test your network by running `python avg_runner.py` from the `Code/` directory with the following options:
    ```
    -l/--load_path=    <Relative/path/to/saved/model>
    -t/--test_dir=     <Directory of test images>
    -r--recursions=    <# recursive predictions to make on test>
    -a/--adversarial=  <{t/f}> (Whether to use adversarial training. Default=True)
    -n/--name=         <Subdirectory of ../Data/Save/*/ in which to save output of this run>
    -O/--overwrite     (Overwrites all previous data for the model with this save name)
    -T/--test_only     (Only runs a test step -- no training)
    -H/--help          (Prints usage)
    --stats_freq=      <How often to print loss/train error stats, in # steps>
    --summary_freq=    <How often to save loss/error summaries, in # steps>
    --img_save_freq=   <How often to save generated images, in # steps>
    --test_freq=       <How often to test the model on test data, in # steps>
    --model_save_freq= <How often to save the model, in # steps>
    ```

## Single Pendulum 

1. My data:
    ```
        - Train(135 videos)
            - Video 0
                - frame 000.png (300 x 300)
                - frame ...
                - frame 049.png
            - Video ...
            - Video 135
        - Test(15 videos)
            - Video 1
                - frame 000.png
                - frame ...
                - frame 049.png
            - Video ...
            - Video 15
        - num_clips = 100,000
        - Training Steps = 20,000
    ```
2. Training Results:
    
