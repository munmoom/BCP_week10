{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyN7sVjSW7c5wLx5YYcw1//F",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_week10/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jm0KHlCfIOFC",
        "outputId": "802f88ec-db92-4910-b46d-6f8f92e5c766"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "22\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "h = 0\n",
        "for i in range(1,N+1):\n",
        "  h += 5*i\n",
        "  if i>=2:\n",
        "    d = -3-2*(i-2)\n",
        "    h += d\n",
        "print(h%45678)"
      ]
    }
  ]
}