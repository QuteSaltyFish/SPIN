from utils import TrainOptions
from train import Trainer
import warnings

if __name__ == '__main__':

    warnings.filterwarnings("ignore")
    options = TrainOptions().parse_args()
    trainer = Trainer(options)
    trainer.train()
