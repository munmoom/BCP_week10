{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMl4n9loEpUyWzp79+xcq6C",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_week10/blob/main/1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HbF86ik4IJ8Z",
        "outputId": "b2e3648e-541b-4ea3-b780-e99c8f6210df"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "5 3\n",
            "1 2\n",
            "7 5\n",
            "3 2\n"
          ]
        }
      ],
      "source": [
        "T = int(input())\n",
        "for i in range (T):\n",
        "  N,M = map(int, input().split())\n",
        "  na = N - M\n",
        "  U = M - na\n",
        "  print(U, end=' ')\n",
        "  print(M-U)"
      ]
    }
  ]
}