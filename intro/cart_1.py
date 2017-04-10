from __future__ import print_function

import gym
env = gym.make('CartPole-v0')
for i_episode in xrange(1):
	observation = env.reset()
	for t in xrange(100):
		env.render()
		print(observation)
		# action = env.action_space.sample()
		if t < 20:
			action = 0 # left
		else:
			action = 1
		observation, reward, done, info = env.step(action)
		print("Timestep: {}".format(t))
		print("Observation, reward, done, info")
		print(observation)
		print(reward)
		print(done)
		print(info)
		# if done:
		# 	print("Episode finished after {} timesteps".format(t))
		# 	break