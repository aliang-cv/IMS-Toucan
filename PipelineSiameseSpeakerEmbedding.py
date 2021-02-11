import random

import torch
import torchviz

from SpeakerEmbedding.SiameseSpeakerEmbedding import SiameseSpeakerEmbedding


def featurize_corpus(path_to_corpus):
    # load pair of text and speech
    # apply collect_features()
    # store features in Dataset dict
    # repeat for all pairs
    # Dump dict to file
    pass


def train_loop(net, train_dataset, eval_dataset, epochs, batchsize):
    optimizer = None
    scheduler = None
    batch_counter = 0
    net.train()
    net.to_device("cuda")
    for _ in range(epochs):
        index_list = random.sample(range(len(train_dataset)), len(train_dataset))
        for index in index_list:
            net(train_dataset[index]).backward()
            batch_counter += 1
            print("Iteration {}".format(batch_counter))
            if batch_counter % batchsize == 0:
                print("Updating weights")
                optimizer.step()
                optimizer.zero_gradient()
                with torch.no_grad():
                    pass
                    net.eval()
                    # calculate loss on eval_dataset
                    # save model if eval_loss in 5 best
                    net.train()
    pass


"""
# 2. LR Scheduler step
            for scheduler in schedulers:
                if isinstance(scheduler, AbsValEpochStepScheduler):
                    scheduler.step(reporter.get_value(*val_scheduler_criterion))
                elif isinstance(scheduler, AbsEpochStepScheduler):
                    scheduler.step()



# 4. Save/Update the checkpoint
                torch.save(
                    {
                        "model": model.state_dict(),
                        "reporter": reporter.state_dict(),
                        "optimizers": [o.state_dict() for o in optimizers],
                        "schedulers": [
                            s.state_dict() if s is not None else None
                            for s in schedulers
                        ],
                        "scaler": scaler.state_dict() if scaler is not None else None,
                    },
                    output_dir / "checkpoint.pth",
                )
"""


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def show_model(model):
    print(model)
    print("\n\nNumber of Parameters: {}".format(count_parameters(model)))


if __name__ == '__main__':
    sse = SiameseSpeakerEmbedding()

    # show_model(sse)

    out = sse(torch.rand((1, 1, 512, 2721)), torch.rand((1, 1, 512, 1233)), torch.Tensor([-1]))

    torchviz.make_dot(out.mean(), dict(sse.named_parameters())).render("speaker_emb_graph", format="png")
