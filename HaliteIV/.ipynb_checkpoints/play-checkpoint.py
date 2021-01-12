from kaggle_environments import make
env = make("halite", debug=True)
env.run(["agent.py", "random", "random", "random"])
env.render(mode="ipython", width=800, height=600)
