import pandas as pd
import matplotlib.pyplot as plt

def vis_bar(dataframe, titletext):
    # 시각화
    plt.figure(figsize=(9, 4))

    # 각 바를 따로 그리고 레전드 레이블 설정
    for i, (value, count) in enumerate(zip(dataframe[dataframe.columns[0]], dataframe[dataframe.columns[-1]])):
        alpha = 0.2 + 0.8 * (count / max(dataframe[dataframe.columns[-1]]))  # 투명도 설정
        plt.bar(value, count, color="black", label=value, alpha=alpha)

    # 바 위에 숫자 표시
    for i, (value, count) in enumerate(zip(dataframe[dataframe.columns[0]], dataframe[dataframe.columns[-1]])):
        height = count
        plt.annotate('{}'.format(int(height)),  # 정수로 변환하여 표시
                    xy=(i, height),
                    xytext=(0, 3),  # 텍스트 위치 설정
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.title(titletext)
    plt.gca().axes.xaxis.set_visible(False) #x 라벨 범위 없애기
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.ylabel('빈도', rotation=0, ha='right')  # y 축 라벨을 수평으로 설정
    plt.xticks(rotation=0)  # x 축 레이블을 회전하지 않고 평행하게 표시
    plt.legend()  # 레전드 표시

    # y 축 눈금을 5의 배수 단위로 설정
    plt.yticks(range(0, max(dataframe[dataframe.columns[-1]]) + 1, 5))

    # 레전드 설정
    legend = plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.show()
    return plt

def vis_bar_subplot(dataframe):
    # 그래프 크기 및 서브플롯 생성
    fig, axs = plt.subplots(2, 1, figsize=(15, 10))

    # 색상 맵 설정
    cmap = plt.colormaps.get_cmap('Blues')
    normalize1 = mpl.colors.Normalize(vmin=min(frequency1_1['1순위']), vmax=max(frequency1_1['1순위']))
    normalize2 = mpl.colors.Normalize(vmin=min(frequency1_2['2순위']), vmax=max(frequency1_2['2순위']))

    # 1순위 그래프 그리기

    for i, (value, count) in enumerate(zip(frequency1_1['값'], frequency1_1['1순위'])):
        axs[0].bar(value, count, color=cmap(normalize1(count)), label=value)
        axs[0].annotate('{}'.format(int(count)),
                        xy=(i, count),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
    axs[0].set_title("귀하가 강원세계산림엑스포에 참여하는 참여동기는 무엇입니까? - 1순위")
    axs[0].set_xlabel('값')
    axs[0].set_ylabel('빈도') # , rotation=0
    axs[0].xaxis.set_visible(False)
    axs[0].spines['top'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    axs[0].legend()

    # 2순위 그래프 그리기
    for i, (value, count) in enumerate(zip(frequency1_2['값'], frequency1_2['2순위'])):
        axs[1].bar(value, count, color=cmap(normalize2(count)), label=value)
        axs[1].annotate('{}'.format(int(count)),
                        xy=(i, count),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
    axs[1].set_title("귀하가 강원세계산림엑스포에 참여하는 참여동기는 무엇입니까? - 2순위")
    axs[1].set_xlabel('값')
    axs[1].set_ylabel('빈도') # , rotation=0
    axs[1].axes.xaxis.set_visible(False)
    axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    axs[1].xaxis.set_tick_params(rotation=0)
    axs[1].legend()

    # y 축 눈금을 5의 배수 단위로 설정
    axs[0].set_yticks(range(0, max(frequency1_1['1순위']) + 1, 5))
    axs[1].set_yticks(range(0, max(frequency1_2['2순위']) + 1, 5))
    # 레전드 설정
    axs[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
    axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.subplots_adjust(left=0.3, bottom=0.3, right=0.9, top=0.9, wspace=0.2, hspace=0.4)

    plt.show()