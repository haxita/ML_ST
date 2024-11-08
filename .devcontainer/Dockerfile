# 使用官方的 Miniconda 作为基础镜像
FROM continuumio/miniconda3

# 设置工作目录
WORKDIR /workspace

# 复制环境文件
COPY environment.yml .

# 创建 Conda 环境
RUN conda env create -f environment.yml

# 激活环境
SHELL ["conda", "run", "-n", "ml_st", "/bin/bash", "-c"]

# 安装必要的工具
RUN conda install -c conda-forge jupyterlab

# 设置默认命令
CMD ["conda", "run", "--no-capture-output", "-n", "ml_st", "bash"]
