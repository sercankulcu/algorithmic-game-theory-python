# Algorithmic Game Theory in Python

Python code examples for the undergraduate **Algorithmic Game Theory (Algoritmik Oyun Kuramı)** course at Giresun University. Each `BolumNN` folder holds chapter NN of the course and contains the code shown on that chapter's slides as small runnable programs. Function and variable names follow the slides, and every program runs the worked example from the lecture notes, so its output can be compared directly with the slides and the notes. The expected output is at the end of each file.

Course page, slides, lecture notes and the course book: <https://sercankulcu.github.io/teaching/algorithmic-game-theory/>

## Chapters

| Folder | Chapter | Programs |
|---|---|---|
| `Bolum00` | Preparation | Argmax over actions with a loop; expected value of a lottery |
| `Bolum01` | Decision Theory | Decision criteria under uncertainty (maximin, maximax, Laplace, Savage), sequential Bayesian updating, solving a decision tree by recursion |
| `Bolum02` | Games and Representations | Minimax and alpha-beta on small trees, depth-limited alpha-beta with best-move selection on tic-tac-toe, level-k thinking and iterated elimination in Guess 2/3 of the Average, backward labelling in Don't Say 21, the Nim XOR move, backward induction (subgame perfect equilibrium) on a game tree |
| `Bolum03` | Nash Equilibrium | Pure Nash equilibria by best-response marking, iterated elimination of strictly dominated strategies, the 2×2 mixed equilibrium by indifference, 2×n maximin mixed strategy, support enumeration with nashpy |
| `Bolum04` | Mechanism Design | The VCG mechanism (public project and single item = Vickrey), Gale–Shapley deferred acceptance, Top Trading Cycles |
| `Bolum05` | Auctions | Best bid shading in first-price auctions, reserve price revenue and optimal reserve, double auction with midpoint pricing, McAfee mechanism |
| `Bolum06` | Online Platforms | Participation dynamics on a two-sided platform, GSP vs VCG payments in sponsored search, profitable-deviation check for GSP bids |
| `Bolum07` | Social Choice and Voting | Borda count, instant-runoff voting, Kemeny ranking by brute force |
| `Bolum08` | Network Design and Routing | Wardrop equilibrium on two parallel roads by bisection, Braess paradox edge removal, player cost in a network formation game (BFS) |
| `Bolum09` | Price of Anarchy | Price of anarchy of the nonlinear Pigou network, Nash check for load balancing, brute-force PoA/PoS for load balancing |
| `Bolum10` | Multi-Agent Systems | Contract net task allocation vs. brute-force optimal assignment, Shapley value, Shapley–Shubik power index |
| `Bolum11` | Algorithmic Fairness and Ethics | Group fairness metrics (selection rate, TPR, FPR, PPV), randomized equal opportunity, cut-and-choose by bisection, feedback loop in predictive policing |
| `Bolum12` | Behavioral and Collective Decisions | Prospect theory bet value, conditional cooperation decay in a public goods game, costly punishment, information cascades, Condorcet jury theorem |
| `Bolum13` | Learning and Adaptation | Fictitious play, Hedge (multiplicative weights), ε-greedy and UCB1 bandits, tabular Q-learning, repeated prisoner's dilemma matches |
| `Bolum14` | Future Directions | Algorithmic collusion under trigger strategies, automated mechanism design for two buyer types, learning a reserve price from data, exponential mechanism, AMM sandwich attack, greedy winner determination in combinatorial auctions |

## Running the examples

Requires **Python 3.8 or later**. Every file is a standalone program that uses only the standard library and runs its example with no keyboard input; programs that use randomness fix the seed used in the lecture notes, so their output is reproducible. The one exception is `Bolum03/yaklasik_denge_araclar.py`, which needs the `nashpy` package:

```bash
pip install -r requirements.txt
```

To run a program:

```bash
cd Bolum03
python saf_nash.py
```

Comments, docstrings and identifiers are in Turkish, as on the slides. Where a slide's code uses something it does not define (a missing `import`, or the tic-tac-toe game used by the depth-limited search in `Bolum02/laboratuvar_arama.py`), the file adds the smallest piece needed and says so in a comment.

## Automatic check

`ci/run_examples.py` runs every program in the `BolumNN` folders (with the packages in `requirements.txt`) and compares its output with the expected output at the end of the file. GitHub Actions runs it on every push. A program whose output changes from run to run (timings, random numbers, thread order, the network) says so above its expected output and only has to run. To run the check locally:

```bash
python ci/run_examples.py            # every chapter
python ci/run_examples.py Bolum03    # one chapter
```
