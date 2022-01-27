class Run:
    def __init__(self, run):
        self.seed: int = None
        self.config: dict = None
        self.measures: dict = None

        self.final_test_acc: float = None
        self.final_train_acc: float = None