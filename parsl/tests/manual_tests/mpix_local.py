from libsubmit.providers import LocalProvider
from libsubmit.channels import LocalChannel

from parsl.config import Config
from parsl.executors.mpix import MPIExecutor

config = Config(
    executors=[
        MPIExecutor(
            label="local_ipp",
            jobs_q_url="tcp://127.0.0.1:50005",
            results_q_url="tcp://127.0.0.1:50006",
            provider=LocalProvider(
                channel=LocalChannel(),
                init_blocks=0,
                max_blocks=0,
            )
        )
    ],
    strategy=None,
)