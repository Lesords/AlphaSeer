from stable_baselines3 import DQN
from logon_new import AlphaSeer

# 创建环境（请确保此处的环境配置与训练时的环境配置一致）
env = AlphaSeer()

# 加载训练好的智能盖亚
trained_model = DQN.load("model/DQN_Seer_best")

# 在环境中使用智能盖亚进行预测
obs = env.reset()  # 重置环境状态
done = False

#状态计数器
k=0
while not done:
    if k==0:
        obs=obs[0]
    action, _ = trained_model.predict(obs)  # 使用模型预测动作

    #预测模型动作
    obs, reward, done, _,info = env.step_info(action.reshape(-1)[0])  # 执行动作并获取新的状态、奖励和终止信息

    #打印模型的动作、奖励、终止信息
    print(reward,info)
    k+=1
