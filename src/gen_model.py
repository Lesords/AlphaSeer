from stable_baselines3 import DQN
from stable_baselines3.common import logger
from logon_new import AlphaSeer

#初始化AlphaSeer环境
env = AlphaSeer()

#设置AI玩家agent
agent = DQN('MlpPolicy', env, verbose=0,tensorboard_log='logs')

print("start learning")
#对战场次定为50万次
agent.learn(total_timesteps=500000, log_interval=100,tb_log_name='DQN')

print("start saving the model")
#保存模型
agent.save("model/DQN_Seer")

print("All over")
