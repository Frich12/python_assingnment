{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5h6AT3y8mmqXYDJlD/uz8",
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
        "<a href=\"https://colab.research.google.com/github/Frich12/python_assingnment/blob/main/User_input.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "vQhEJBVLzkQ4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "94d1fe27-b09d-4bed-ee8b-9c384ec85bf4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your nameFelix\n",
            "Please enter your age 20\n",
            "Please enter your location Meru\n",
            "HelloFelix you are 20 years old you live in Meru\n"
          ]
        }
      ],
      "source": [
        "name=input(\"Please enter your name\")\n",
        "age=input(\"Please enter your age\")\n",
        "location=input(\"Please enter your location\")\n",
        "print(\"Hello\"+ name,\"you are\"+age,\"years old\",\"you live in\"+location)"
      ]
    }
  ]
}