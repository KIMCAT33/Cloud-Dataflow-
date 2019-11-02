{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "train.py",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KIMCAT33/ML-Pipeline/blob/master/train.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hu8y0fljcs1c",
        "colab_type": "code",
        "outputId": "d1cc44ab-422a-4f14-f4e0-234f3c4eccac",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        }
      },
      "source": [
        "from google.colab import auth\n",
        "auth.authenticate_user()\n",
        "print('Authenticated')"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Authenticated\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K0ebYfTDcx8p",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "project_id = 'pipeliner'\n",
        "\n",
        "from google.cloud import bigquery\n",
        "\n",
        "client = bigquery.Client(project=project_id)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9lNjLpnIa9gS",
        "colab_type": "code",
        "outputId": "c5333f55-0729-4179-e850-c564b9950426",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        }
      },
      "source": [
        "query = \"\"\"\n",
        "SELECT\n",
        "    weight_pounds,\n",
        "    is_male,\n",
        "    mother_age,\n",
        "    plurality,\n",
        "    gestation_weeks\n",
        "FROM\n",
        "    publicdata.samples.natality\n",
        "WHERE year > 2000\n",
        "\"\"\"\n",
        "\n",
        "df = client.query(query + \"LIMIT 10000\").to_dataframe()\n",
        "df.head()"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>weight_pounds</th>\n",
              "      <th>is_male</th>\n",
              "      <th>mother_age</th>\n",
              "      <th>plurality</th>\n",
              "      <th>gestation_weeks</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.131954</td>\n",
              "      <td>True</td>\n",
              "      <td>22</td>\n",
              "      <td>1</td>\n",
              "      <td>41.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7.980734</td>\n",
              "      <td>False</td>\n",
              "      <td>28</td>\n",
              "      <td>1</td>\n",
              "      <td>44.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>8.675190</td>\n",
              "      <td>False</td>\n",
              "      <td>33</td>\n",
              "      <td>1</td>\n",
              "      <td>41.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5.346210</td>\n",
              "      <td>True</td>\n",
              "      <td>25</td>\n",
              "      <td>1</td>\n",
              "      <td>35.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>6.999677</td>\n",
              "      <td>False</td>\n",
              "      <td>29</td>\n",
              "      <td>1</td>\n",
              "      <td>39.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   weight_pounds  is_male  mother_age  plurality  gestation_weeks\n",
              "0       7.131954     True          22          1             41.0\n",
              "1       7.980734    False          28          1             44.0\n",
              "2       8.675190    False          33          1             41.0\n",
              "3       5.346210     True          25          1             35.0\n",
              "4       6.999677    False          29          1             39.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C1BFX99kbCVH",
        "colab_type": "code",
        "outputId": "6fd1865f-03db-4b18-dafe-a31564abc205",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 149
        }
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "import seaborn as sns\n",
        "from keras import models\n",
        "from keras import layers\n",
        "\n",
        "columns = ['is_male', 'mother_age', 'plurality', 'gestation_weeks']\n",
        "df.dropna(how=\"any\", inplace=True)\n",
        "\n",
        "x=df[columns]\n",
        "y = df['weight_pounds']\n",
        "\n",
        "x.loc[x[\"is_male\"] == True, \"is_male\"] = 1\n",
        "x.loc[x[\"is_male\"] == False, \"is_male\"] = 0\n"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/indexing.py:494: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  self.obj[item] = s\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f5wKQUTPdehW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M5EM8NAAdiI7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def build_model():\n",
        "    model = models.Sequential()\n",
        "    model.add(layers.Dense(64, activation='relu',\n",
        "                           input_shape=(train_x.shape[1],)))\n",
        "    model.add(layers.Dense(64, activation='relu'))\n",
        "    model.add(layers.Dense(1))\n",
        "    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])\n",
        "    return model"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1Vv2SzDDdkAm",
        "colab_type": "code",
        "outputId": "ff849208-6e40-46a1-8a69-9d7f2ee443ce",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "k = 4\n",
        "num_val_samples = len(train_x) // k\n",
        "num_epochs = 20\n",
        "all_mae_histories = []\n",
        "for i in range(k):\n",
        "    print('처리중인 폴드 #', i)\n",
        "    # 검증 데이터 준비: k번째 분할\n",
        "    val_data = train_x[i * num_val_samples: (i + 1) * num_val_samples]\n",
        "    val_targets = train_y[i * num_val_samples: (i + 1) * num_val_samples]\n",
        "\n",
        "    # 훈련 데이터 준비: 다른 분할 전체\n",
        "    partial_train_data = np.concatenate(\n",
        "        [train_x[:i * num_val_samples],\n",
        "         train_x[(i + 1) * num_val_samples:]],\n",
        "        axis=0)\n",
        "    partial_train_targets = np.concatenate(\n",
        "        [train_y[:i * num_val_samples],\n",
        "         train_y[(i + 1) * num_val_samples:]],\n",
        "        axis=0)\n",
        "\n",
        "    # 케라스 모델 구성(컴파일 포함)\n",
        "    model = build_model()\n",
        "    # 모델 훈련(verbose=0 이므로 훈련 과정이 출력되지 않습니다)\n",
        "    history = model.fit(partial_train_data, partial_train_targets,\n",
        "                        validation_data=(val_data, val_targets),\n",
        "                        epochs=num_epochs, batch_size=1, verbose=1)\n",
        "    mae_history = history.history['val_mean_absolute_error']\n",
        "    all_mae_histories.append(mae_history)"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "처리중인 폴드 # 0\n",
            "Train on 5921 samples, validate on 1973 samples\n",
            "Epoch 1/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.4793 - mean_absolute_error: 0.9439 - val_loss: 1.2450 - val_mean_absolute_error: 0.8754\n",
            "Epoch 2/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.3300 - mean_absolute_error: 0.9040 - val_loss: 1.7217 - val_mean_absolute_error: 1.0522\n",
            "Epoch 3/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2905 - mean_absolute_error: 0.8863 - val_loss: 1.3409 - val_mean_absolute_error: 0.9107\n",
            "Epoch 4/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2742 - mean_absolute_error: 0.8824 - val_loss: 1.3247 - val_mean_absolute_error: 0.9105\n",
            "Epoch 5/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2572 - mean_absolute_error: 0.8769 - val_loss: 1.8037 - val_mean_absolute_error: 1.0795\n",
            "Epoch 6/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2575 - mean_absolute_error: 0.8793 - val_loss: 1.3258 - val_mean_absolute_error: 0.9044\n",
            "Epoch 7/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2467 - mean_absolute_error: 0.8713 - val_loss: 1.1641 - val_mean_absolute_error: 0.8462\n",
            "Epoch 8/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2403 - mean_absolute_error: 0.8738 - val_loss: 1.2378 - val_mean_absolute_error: 0.8715\n",
            "Epoch 9/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2417 - mean_absolute_error: 0.8691 - val_loss: 1.1732 - val_mean_absolute_error: 0.8510\n",
            "Epoch 10/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2426 - mean_absolute_error: 0.8721 - val_loss: 1.3498 - val_mean_absolute_error: 0.9130\n",
            "Epoch 11/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2235 - mean_absolute_error: 0.8655 - val_loss: 1.2393 - val_mean_absolute_error: 0.8769\n",
            "Epoch 12/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2374 - mean_absolute_error: 0.8663 - val_loss: 1.1383 - val_mean_absolute_error: 0.8367\n",
            "Epoch 13/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2271 - mean_absolute_error: 0.8671 - val_loss: 1.1750 - val_mean_absolute_error: 0.8518\n",
            "Epoch 14/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2298 - mean_absolute_error: 0.8647 - val_loss: 1.1803 - val_mean_absolute_error: 0.8499\n",
            "Epoch 15/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2217 - mean_absolute_error: 0.8615 - val_loss: 1.1403 - val_mean_absolute_error: 0.8361\n",
            "Epoch 16/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2176 - mean_absolute_error: 0.8573 - val_loss: 1.1949 - val_mean_absolute_error: 0.8554\n",
            "Epoch 17/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2288 - mean_absolute_error: 0.8622 - val_loss: 1.1424 - val_mean_absolute_error: 0.8373\n",
            "Epoch 18/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2126 - mean_absolute_error: 0.8606 - val_loss: 1.2300 - val_mean_absolute_error: 0.8685\n",
            "Epoch 19/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2219 - mean_absolute_error: 0.8626 - val_loss: 1.1494 - val_mean_absolute_error: 0.8407\n",
            "Epoch 20/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2192 - mean_absolute_error: 0.8617 - val_loss: 1.2137 - val_mean_absolute_error: 0.8670\n",
            "처리중인 폴드 # 1\n",
            "Train on 5921 samples, validate on 1973 samples\n",
            "Epoch 1/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.8901 - mean_absolute_error: 0.9925 - val_loss: 1.2481 - val_mean_absolute_error: 0.8788\n",
            "Epoch 2/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.3017 - mean_absolute_error: 0.8888 - val_loss: 1.5191 - val_mean_absolute_error: 0.9928\n",
            "Epoch 3/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2662 - mean_absolute_error: 0.8800 - val_loss: 1.1936 - val_mean_absolute_error: 0.8649\n",
            "Epoch 4/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2584 - mean_absolute_error: 0.8722 - val_loss: 1.1674 - val_mean_absolute_error: 0.8544\n",
            "Epoch 5/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2434 - mean_absolute_error: 0.8669 - val_loss: 1.2834 - val_mean_absolute_error: 0.9001\n",
            "Epoch 6/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2246 - mean_absolute_error: 0.8634 - val_loss: 1.1625 - val_mean_absolute_error: 0.8530\n",
            "Epoch 7/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2345 - mean_absolute_error: 0.8645 - val_loss: 1.1684 - val_mean_absolute_error: 0.8558\n",
            "Epoch 8/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2249 - mean_absolute_error: 0.8639 - val_loss: 1.1607 - val_mean_absolute_error: 0.8523\n",
            "Epoch 9/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2153 - mean_absolute_error: 0.8563 - val_loss: 1.1787 - val_mean_absolute_error: 0.8595\n",
            "Epoch 10/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2168 - mean_absolute_error: 0.8588 - val_loss: 1.1647 - val_mean_absolute_error: 0.8543\n",
            "Epoch 11/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2074 - mean_absolute_error: 0.8561 - val_loss: 1.9532 - val_mean_absolute_error: 1.1260\n",
            "Epoch 12/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2104 - mean_absolute_error: 0.8568 - val_loss: 1.1741 - val_mean_absolute_error: 0.8579\n",
            "Epoch 13/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2066 - mean_absolute_error: 0.8557 - val_loss: 1.1549 - val_mean_absolute_error: 0.8512\n",
            "Epoch 14/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2001 - mean_absolute_error: 0.8563 - val_loss: 1.1555 - val_mean_absolute_error: 0.8522\n",
            "Epoch 15/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.1979 - mean_absolute_error: 0.8554 - val_loss: 1.2575 - val_mean_absolute_error: 0.8911\n",
            "Epoch 16/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2001 - mean_absolute_error: 0.8510 - val_loss: 1.1592 - val_mean_absolute_error: 0.8520\n",
            "Epoch 17/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2045 - mean_absolute_error: 0.8561 - val_loss: 1.1551 - val_mean_absolute_error: 0.8509\n",
            "Epoch 18/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.1992 - mean_absolute_error: 0.8546 - val_loss: 1.1529 - val_mean_absolute_error: 0.8504\n",
            "Epoch 19/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2109 - mean_absolute_error: 0.8562 - val_loss: 1.1918 - val_mean_absolute_error: 0.8660\n",
            "Epoch 20/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.1994 - mean_absolute_error: 0.8587 - val_loss: 1.2893 - val_mean_absolute_error: 0.9039\n",
            "처리중인 폴드 # 2\n",
            "Train on 5921 samples, validate on 1973 samples\n",
            "Epoch 1/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.5197 - mean_absolute_error: 0.9631 - val_loss: 1.6259 - val_mean_absolute_error: 1.0077\n",
            "Epoch 2/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.3013 - mean_absolute_error: 0.8991 - val_loss: 1.5044 - val_mean_absolute_error: 0.9614\n",
            "Epoch 3/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2654 - mean_absolute_error: 0.8843 - val_loss: 1.6058 - val_mean_absolute_error: 0.9989\n",
            "Epoch 4/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2530 - mean_absolute_error: 0.8794 - val_loss: 1.2914 - val_mean_absolute_error: 0.8798\n",
            "Epoch 5/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2453 - mean_absolute_error: 0.8752 - val_loss: 1.3457 - val_mean_absolute_error: 0.9079\n",
            "Epoch 6/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2406 - mean_absolute_error: 0.8737 - val_loss: 1.5571 - val_mean_absolute_error: 0.9928\n",
            "Epoch 7/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2262 - mean_absolute_error: 0.8690 - val_loss: 1.1569 - val_mean_absolute_error: 0.8287\n",
            "Epoch 8/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2260 - mean_absolute_error: 0.8731 - val_loss: 1.2040 - val_mean_absolute_error: 0.8483\n",
            "Epoch 9/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2187 - mean_absolute_error: 0.8691 - val_loss: 1.2385 - val_mean_absolute_error: 0.8649\n",
            "Epoch 10/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2224 - mean_absolute_error: 0.8657 - val_loss: 1.1849 - val_mean_absolute_error: 0.8436\n",
            "Epoch 11/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2107 - mean_absolute_error: 0.8630 - val_loss: 1.1627 - val_mean_absolute_error: 0.8359\n",
            "Epoch 12/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2090 - mean_absolute_error: 0.8660 - val_loss: 1.2483 - val_mean_absolute_error: 0.8657\n",
            "Epoch 13/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2178 - mean_absolute_error: 0.8671 - val_loss: 1.2188 - val_mean_absolute_error: 0.8580\n",
            "Epoch 14/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2216 - mean_absolute_error: 0.8681 - val_loss: 1.4624 - val_mean_absolute_error: 0.9574\n",
            "Epoch 15/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.1982 - mean_absolute_error: 0.8563 - val_loss: 1.2127 - val_mean_absolute_error: 0.8508\n",
            "Epoch 16/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2088 - mean_absolute_error: 0.8631 - val_loss: 1.7693 - val_mean_absolute_error: 1.0693\n",
            "Epoch 17/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2022 - mean_absolute_error: 0.8625 - val_loss: 1.1626 - val_mean_absolute_error: 0.8335\n",
            "Epoch 18/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2046 - mean_absolute_error: 0.8616 - val_loss: 1.1649 - val_mean_absolute_error: 0.8333\n",
            "Epoch 19/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2066 - mean_absolute_error: 0.8624 - val_loss: 1.3014 - val_mean_absolute_error: 0.8854\n",
            "Epoch 20/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2018 - mean_absolute_error: 0.8621 - val_loss: 1.2196 - val_mean_absolute_error: 0.8580\n",
            "처리중인 폴드 # 3\n",
            "Train on 5921 samples, validate on 1973 samples\n",
            "Epoch 1/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.4525 - mean_absolute_error: 0.9513 - val_loss: 1.1341 - val_mean_absolute_error: 0.8268\n",
            "Epoch 2/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.3036 - mean_absolute_error: 0.8944 - val_loss: 1.1274 - val_mean_absolute_error: 0.8242\n",
            "Epoch 3/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2700 - mean_absolute_error: 0.8873 - val_loss: 1.1156 - val_mean_absolute_error: 0.8188\n",
            "Epoch 4/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2634 - mean_absolute_error: 0.8817 - val_loss: 1.2015 - val_mean_absolute_error: 0.8466\n",
            "Epoch 5/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2571 - mean_absolute_error: 0.8786 - val_loss: 1.1034 - val_mean_absolute_error: 0.8147\n",
            "Epoch 6/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2389 - mean_absolute_error: 0.8741 - val_loss: 1.1889 - val_mean_absolute_error: 0.8426\n",
            "Epoch 7/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2460 - mean_absolute_error: 0.8748 - val_loss: 1.0981 - val_mean_absolute_error: 0.8116\n",
            "Epoch 8/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2305 - mean_absolute_error: 0.8717 - val_loss: 1.1303 - val_mean_absolute_error: 0.8206\n",
            "Epoch 9/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2399 - mean_absolute_error: 0.8728 - val_loss: 1.1751 - val_mean_absolute_error: 0.8361\n",
            "Epoch 10/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2311 - mean_absolute_error: 0.8669 - val_loss: 1.1487 - val_mean_absolute_error: 0.8364\n",
            "Epoch 11/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2339 - mean_absolute_error: 0.8722 - val_loss: 1.1213 - val_mean_absolute_error: 0.8259\n",
            "Epoch 12/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2357 - mean_absolute_error: 0.8729 - val_loss: 1.2792 - val_mean_absolute_error: 0.8905\n",
            "Epoch 13/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2283 - mean_absolute_error: 0.8730 - val_loss: 1.1269 - val_mean_absolute_error: 0.8277\n",
            "Epoch 14/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2343 - mean_absolute_error: 0.8696 - val_loss: 1.1808 - val_mean_absolute_error: 0.8373\n",
            "Epoch 15/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2217 - mean_absolute_error: 0.8696 - val_loss: 1.1369 - val_mean_absolute_error: 0.8314\n",
            "Epoch 16/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2232 - mean_absolute_error: 0.8634 - val_loss: 1.2645 - val_mean_absolute_error: 0.8870\n",
            "Epoch 17/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2220 - mean_absolute_error: 0.8683 - val_loss: 1.2148 - val_mean_absolute_error: 0.8658\n",
            "Epoch 18/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2257 - mean_absolute_error: 0.8664 - val_loss: 1.0993 - val_mean_absolute_error: 0.8133\n",
            "Epoch 19/20\n",
            "5921/5921 [==============================] - 24s 4ms/step - loss: 1.2140 - mean_absolute_error: 0.8665 - val_loss: 1.1379 - val_mean_absolute_error: 0.8327\n",
            "Epoch 20/20\n",
            "5921/5921 [==============================] - 23s 4ms/step - loss: 1.2226 - mean_absolute_error: 0.8692 - val_loss: 1.2242 - val_mean_absolute_error: 0.8675\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cZ9aTLygdl3y",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "model.save_weights('./natality.h5', overwrite=True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OWwEc-d8hIJa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}