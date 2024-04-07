# 印刷したいデザインのリストを作成する
unprinted_designs = ['iphone','ロボットのペンダント','12面体']
completed_models = []

# リストがなくなるまでデザインを3D印刷する
# 各デザインは印刷後に completed_models に移動する

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"3D印刷中:{current_design}")
    completed_models.append(current_design)

# 3D印刷が完了したモデルを印刷する
print("\n以下のモデルが3D印刷されました。")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs,completed_models):
    """
    リストからなくなるまでデザインを3D印刷する
    各デザインは印刷後に completed_model に移動する
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"3D印刷中:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """3D印刷されたすべてのモデルの情報を出力する"""
    print("\n以下のデザインが3D印刷されました")
    for completed_model in completed_models:
        print(completed_model)

