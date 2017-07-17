from joblib import Parallel, delayed
import multiprocessing
from Twitter_Bot_Split import botsplit
week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


# what are your inputs, and what operation do you want to
# perform on each input. For example...
#inputs = range(10)


num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(botsplit)(i) for i in week)
