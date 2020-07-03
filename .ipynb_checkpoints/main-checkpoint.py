{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "import bs4\n",
    "from scipy import stats\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Method declaration space\n",
    "\n",
    "def sq(val):\n",
    "    return val*val\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean value is  :89.76923076923077\n",
      "Median value is  : 87.0\n",
      "Moe value is : ModeResult(mode=array([86]), count=array([3]))\n"
     ]
    }
   ],
   "source": [
    "''' We are dealing with this type of data : \n",
    "\n",
    "    Numerical\n",
    "    Categorical\n",
    "    Ordinal\n",
    "    \n",
    "    Numerical data are numbers, and can be split into two numerical categories:\n",
    "\n",
    "    Discrete Data\n",
    "    - numbers that are limited to integers. Example: The number of cars passing by.\n",
    "    Continuous Data\n",
    "    - numbers that are of infinite value. Example: The price of an item, or the size of an item\n",
    "\n",
    "    Categorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.\n",
    "\n",
    "    Ordinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.\n",
    "\n",
    "'''\n",
    "\n",
    "data = [99,86,87,88,111,86,103,87,94,78,77,85,86]\n",
    "mean = numpy.mean(data)\n",
    "print(\"Mean value is  :\"+str(mean))\n",
    "print(\"Median value is  : \" + str(numpy.median(data)))\n",
    "print(\"Moe value is : \"+ str(stats.mode(data)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean value of this speed data: 86.42857142857143\n",
      "standard deviation of this value is  ; 0.9035079029052513\n",
      "Mean value of speed2 data set is : 77.42857142857143\n",
      "Standard deviation of speed2 data set is : 37.84501153334721\n",
      "Variance of speed2 data set is : 1432.2448979591834\n",
      "Getting value of the variance of speed2 : 1432.2448979591834\n"
     ]
    }
   ],
   "source": [
    "speed = [86,87,88,86,87,85,86]\n",
    "print(\"Mean value of this speed data: \"+str(numpy.mean(speed)))\n",
    "print (\"standard deviation of this value is  ; \"+str(numpy.std(speed)))\n",
    "\n",
    "speed2 = [32,111,138,28,59,77,97]\n",
    "\n",
    "print(\"Mean value of speed2 data set is : \"+str(numpy.mean(speed2)))\n",
    "print(\"Standard deviation of speed2 data set is : \"+str(numpy.std(speed2)))\n",
    "print(\"Variance of speed2 data set is : \"+str(sq(numpy.std(speed2))))\n",
    "\n",
    "# we can also use var() method to get the value of variance\n",
    "\n",
    "print(\"Getting value of the variance of speed2 : \" + str(numpy.var(speed2)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data of speed2 are : [32, 111, 138, 28, 59, 77, 97]\n",
      "Value of 75. percentile: 104.0\n",
      "Data of speed2 are : [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]\n",
      "Value of 75. percentile: 43.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Data of speed2 are : \"+str(speed2))\n",
    "print(\"Value of 75. percentile: \"+str(numpy.percentile(speed2, 75)))\n",
    "\n",
    "ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]\n",
    "print(\"Data of speed2 are : \"+str(ages))\n",
    "print(\"Value of 75. percentile: \"+str(numpy.percentile(ages, 75)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Randomly generated data are : \n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "# creating some random data set\n",
    "x = numpy.random.uniform(0.0, 5.0, 250)\n",
    "print(\"Randomly generated data are : \")\n",
    "print(\"\")\n",
    "#for y in x:\n",
    " #   print(y)\n",
    "    \n",
    "# creating the histrogram from collected data\n",
    "\n",
    "plt.hist(x,5) # 5 means drawing data upto 5\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Showing the histrogram of this randomly created values : \n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAD4CAYAAAAAczaOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAPh0lEQVR4nO3db4xcV33G8e+DDQFCIxJlExnb1Knk0iaRWujKpY2EqoY2Lolw3qQyEtSqLFmq3BLaSmD3DeoLS6lUIaq2QbKAYgTFtYAqFpQ/qSFCSBCzTkLBMWkskiZbu/HSlkL6ImDz64u9KSNnN/bM7Mzszvl+JGvunDl37u/O3n3u2TN3xqkqJElteMmkC5AkjY+hL0kNMfQlqSGGviQ1xNCXpIasn3QBl3LttdfWli1bJl2GJK0pJ06c+F5VzVzcvupDf8uWLczNzU26DElaU5L821LtTu9IUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDVv0ncqWWbNn32f9ffvKe2ydYiaaVoS+tAMNaa4XTO5LUEENfkhpi6EtSQwx9SWqIoS9JDTH0JakhXrIpSRcZ9SW4k7zE19DvMYofhNdvX9ogr5GvqzQYQ18rzkDW8zwWVh9DX9LYeTKYHENf6hhEmrRxHIOGviStoNU+eDD0p8xqP+C09nhMTRdDf4r5yyrpYoZ+gzwZjM+oXutp+hlO076sBZcM/SQfBu4AzlXVzV3bNcA/AFuAJ4Hfrar/7h7bD+wGLgDvrKovdO2/AnwEeAXwT8DdVVUruzv96z3ghlm392Ad5jmnmdfjqx+eMEfjckb6HwH+BvhoT9s+4FhV3ZNkX3f/PUluBHYCNwGvAf45yc9X1QXgA8Ae4Osshv524HMrtSMrbbngnuRB0vrB2q/LOSn7Ov7UKAZAo3ZxzcttexQDscvZ59V4rF0y9KvqK0m2XNS8A/iNbvkQ8ADwnq79cFU9BzyR5DSwLcmTwFVV9TWAJB8F7mQVh/5a4l8Wo7Uaf3H7NQ378DyP9+EMOqd/fVWdBaiqs0mu69o3sjiSf9581/bjbvnidl3Ccgf4pEYuwzznKPpfvE6/dU8qQKYphLW2rPQbuVmirV6kfeknSfawOBXEa1/72oGL8RdLLXNErKUMGvrPJNnQjfI3AOe69nlgc0+/TcCZrn3TEu1LqqqDwEGA2dnZib/Zu1I8CakFK/XewFqyluoeNPSPAruAe7rb+3ra/z7J+1h8I3crcLyqLiT5YZI3Ag8Cvwf89VCVT5m1fkJYSwf9qE3za7Haj9O1Mu05SZdzyeYnWHzT9tok88B7WQz7I0l2A08BdwFU1ckkR4BHgfPA3u7KHYA/4KeXbH6ONfom7lr9hV6rda9m43i/ol/+nEdrGv6KuZyrd962zEO3LtP/AHBgifY54Oa+qptiL3YArIaDY61+BmG117eUSda8Fl8vDaeZT+SO83/C0Wj4GkvDayb0pbXmcgcqLZwMnRpbOYa+LmkafhmmYR+08lo8Ll4y6QIkSePjSF+SJmjcf20Y+lIfWpwO0HQx9BtniLXHn3nbmgx9D3pdisfIyvM1XR18I1eSGtLkSF+T56ivP6vx9VqNNenSHOlLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDRkq9JP8cZKTSb6d5BNJXp7kmiT3J3m8u726p//+JKeTPJbktuHLlyT1Y+DQT7IReCcwW1U3A+uAncA+4FhVbQWOdfdJcmP3+E3AduDeJOuGK1+S1I9hp3fWA69Ish54JXAG2AEc6h4/BNzZLe8ADlfVc1X1BHAa2Dbk9iVJfRg49Kvq34G/BJ4CzgL/U1VfBK6vqrNdn7PAdd0qG4Gne55ivmt7gSR7kswlmVtYWBi0REnSRYaZ3rmaxdH7DcBrgCuTvP3FVlmirZbqWFUHq2q2qmZnZmYGLVGSdJFhpnfeDDxRVQtV9WPg08CvA88k2QDQ3Z7r+s8Dm3vW38TidJAkaUyGCf2ngDcmeWWSALcCp4CjwK6uzy7gvm75KLAzyRVJbgC2AseH2L4kqU/rB12xqh5M8kngIeA88DBwEHgVcCTJbhZPDHd1/U8mOQI82vXfW1UXhqxfktSHgUMfoKreC7z3oubnWBz1L9X/AHBgmG1KkgbnJ3IlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUkKFCP8mrk3wyyXeSnErya0muSXJ/kse726t7+u9PcjrJY0luG758SVI/hh3p/xXw+ar6BeCXgFPAPuBYVW0FjnX3SXIjsBO4CdgO3Jtk3ZDblyT1YeDQT3IV8CbgQwBV9aOq+j6wAzjUdTsE3Nkt7wAOV9VzVfUEcBrYNuj2JUn9G2ak/3PAAvB3SR5O8sEkVwLXV9VZgO72uq7/RuDpnvXnu7YXSLInyVySuYWFhSFKlCT1Gib01wNvAD5QVa8H/pduKmcZWaKtlupYVQeraraqZmdmZoYoUZLUa5jQnwfmq+rB7v4nWTwJPJNkA0B3e66n/+ae9TcBZ4bYviSpTwOHflX9B/B0ktd1TbcCjwJHgV1d2y7gvm75KLAzyRVJbgC2AscH3b4kqX/rh1z/j4CPJ3kZ8F3g91k8kRxJsht4CrgLoKpOJjnC4onhPLC3qi4MuX1JUh+GCv2qegSYXeKhW5fpfwA4MMw2JUmD8xO5ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JasjQoZ9kXZKHk3ymu39NkvuTPN7dXt3Td3+S00keS3LbsNuWJPVnJUb6dwOneu7vA45V1VbgWHefJDcCO4GbgO3AvUnWrcD2JUmXaajQT7IJuB34YE/zDuBQt3wIuLOn/XBVPVdVTwCngW3DbF+S1J9hR/rvB94N/KSn7fqqOgvQ3V7XtW8Enu7pN9+1vUCSPUnmkswtLCwMWaIk6XkDh36SO4BzVXXicldZoq2W6lhVB6tqtqpmZ2ZmBi1RknSR9UOsewvw1iRvAV4OXJXkY8AzSTZU1dkkG4BzXf95YHPP+puAM0NsX5LUp4FH+lW1v6o2VdUWFt+g/VJVvR04Cuzquu0C7uuWjwI7k1yR5AZgK3B84MolSX0bZqS/nHuAI0l2A08BdwFU1ckkR4BHgfPA3qq6MILtS5KWsSKhX1UPAA90y/8J3LpMvwPAgZXYpiSpf34iV5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0ZOPSTbE7y5SSnkpxMcnfXfk2S+5M83t1e3bPO/iSnkzyW5LaV2AFJ0uUbZqR/HvjTqvpF4I3A3iQ3AvuAY1W1FTjW3ad7bCdwE7AduDfJumGKlyT1Z+DQr6qzVfVQt/xD4BSwEdgBHOq6HQLu7JZ3AIer6rmqegI4DWwbdPuSpP6tyJx+ki3A64EHgeur6iwsnhiA67puG4Gne1ab79okSWMydOgneRXwKeBdVfWDF+u6RFst85x7kswlmVtYWBi2RElSZ6jQT/JSFgP/41X16a75mSQbusc3AOe69nlgc8/qm4AzSz1vVR2sqtmqmp2ZmRmmRElSj2Gu3gnwIeBUVb2v56GjwK5ueRdwX0/7ziRXJLkB2AocH3T7kqT+rR9i3VuAdwDfSvJI1/ZnwD3AkSS7gaeAuwCq6mSSI8CjLF75s7eqLgyxfUlSnwYO/ar6KkvP0wPcusw6B4ADg25TkjQcP5ErSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktSQsYd+ku1JHktyOsm+cW9fklo21tBPsg74W+B3gBuBtyW5cZw1SFLLxj3S3wacrqrvVtWPgMPAjjHXIEnNWj/m7W0Enu65Pw/86sWdkuwB9nR3n03y2IDbuxb43oDrrlXucxta2+fW9pf8xdD7/LNLNY479LNEW72goeogcHDojSVzVTU77POsJe5zG1rb59b2F0a3z+Oe3pkHNvfc3wScGXMNktSscYf+N4CtSW5I8jJgJ3B0zDVIUrPGOr1TVeeT/CHwBWAd8OGqOjnCTQ49RbQGuc9taG2fW9tfGNE+p+oFU+qSpCnlJ3IlqSGGviQ1ZCpDv8Wvekjy4STnknx70rWMQ5LNSb6c5FSSk0nunnRNo5bk5UmOJ/lmt89/PumaxiXJuiQPJ/nMpGsZhyRPJvlWkkeSzK3oc0/bnH73VQ//CvwWi5eIfgN4W1U9OtHCRizJm4BngY9W1c2TrmfUkmwANlTVQ0l+BjgB3DnNP+ckAa6sqmeTvBT4KnB3VX19wqWNXJI/AWaBq6rqjknXM2pJngRmq2rFP5A2jSP9Jr/qoaq+AvzXpOsYl6o6W1UPdcs/BE6x+InvqVWLnu3uvrT7N12jtiUk2QTcDnxw0rVMg2kM/aW+6mGqw6B1SbYArwcenGwlo9dNczwCnAPur6qp32fg/cC7gZ9MupAxKuCLSU50X0uzYqYx9C/rqx40HZK8CvgU8K6q+sGk6xm1qrpQVb/M4qfZtyWZ6qm8JHcA56rqxKRrGbNbquoNLH4j8d5u+nZFTGPo+1UPjejmtT8FfLyqPj3pesapqr4PPABsn3Apo3YL8NZujvsw8JtJPjbZkkavqs50t+eAf2Rx2npFTGPo+1UPDeje1PwQcKqq3jfpesYhyUySV3fLrwDeDHxnslWNVlXtr6pNVbWFxd/lL1XV2ydc1kglubK7OIEkVwK/DazYVXlTF/pVdR54/qseTgFHRvxVD6tCkk8AXwNel2Q+ye5J1zRitwDvYHHk90j37y2TLmrENgBfTvIvLA5u7q+qJi5hbMz1wFeTfBM4Dny2qj6/Uk8+dZdsSpKWN3UjfUnS8gx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1JD/A7AxXfB1ImmSAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# creating very big data\n",
    "bigData = numpy.random.uniform(0.0,5.0,100000)\n",
    "\n",
    "print(\"Showing the histrogram of this randomly created values : \")\n",
    "plt.hist(bigData,100)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAD4CAYAAAD1jb0+AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nO3dbWxc13kn8P8zw0tpKDcaqlF3rYllyUYhtVpVYszWSggUa6W1iih2uHEaNbCLIthdf1lkI8VQQRduJAdemICaxsF+WEBI2rSw4ZVtCVw5ylYuKhWLaldaUCZVVbGEwrEleeRs2MijNuLYHA7Pfhje0Z07577NvXNfZv4/IIg1HM4cDjnPnPuc5zxHlFIgIqLsySU9ACIi6gwDOBFRRjGAExFlFAM4EVFGMYATEWXUQJxP9vGPf1xt2LAhzqckIsq88+fP/5NSaq399lgD+IYNGzA9PR3nUxIRZZ6IXNXdzhQKEVFGeQZwEfkzEfmpiPyD5bY1IvLXIvKPy/8/3N1hEhGRnZ8Z+PcB/I7ttgkAf6OU+mUAf7P8byIiipFnAFdK/S8AN203fx7AXyz/918AGI94XERE5KHTHPi/Ukq9DwDL//9LTncUkSdFZFpEpufm5jp8OiIisuv6IqZS6rBSalQpNbp2bVsVDBERdajTMsL/JyJ3K6XeF5G7Afw0ykER+TU1U8ahk1dwo1LFumIB+3dtwvhIKelhEcWi0xn4cQB/sPzffwDgf0QzHCL/pmbKePrYRZQrVSgA5UoVTx+7iKmZctJDI4qFnzLClwH8HwCbROQ9Efn3ACYB/LaI/COA317+N1GsDp28gmqt3nJbtVbHoZNXEhoRUbw8UyhKqS87fOkzEY+FKJAblWqg2ykeTGvFhzsxKbPWFQuBbqfuY1orXgzglFn7d21Cwci33FYw8ti/a1NCIyKmteIVazMroiiZl+W8XE8PprXixQBOmTY+Uur5gJ2lnPK6YgFlTbBmWqs7mEIhSrGs5ZSZ1ooXAzhRimUtpzw+UsLzX9iKUrEAAVAqFvD8F7am9ooh65hCIYpJJ6mQLOaU+yGtlRYM4NQ3kswlm6kQczZtpkIAuI6BOWVywxQK9YWkc8mdpkKYUyY3nIFnUJaqEuLk9rq4BdA4XrtOUyEslSQ3DOAZ0+mleK/zel2SziWHSYUwp0xOmELJmKxVJcTF63VJets9UyHUDQzgGZP0TDKtvF6XpAMoy+uoG5hCyRhWJeh5vS5pyCVnIRXC9ZVsYQDPmP27NrXkegFeigP610UAPLT5zjF+WQigSeL6SvYwgGdMGmaSaWKdMa40WjOCCsDR82WM3rvG8fXhjPOOpCt1KDgG8AziTLLBPmOs1pba7uMWgHQzzn1HZjF99SaeG9/a3cGnENdXsoeLmJRZuhmjjlMA0n2/AvDS2WupbRbVTUlX6lBwDOCkNTVTxtjkKWycOIGxyVOxBzQ/z+93ZugUgJy+XwF9WZaZdKUOBccUCrVJejHL7/M7VZ5YuQUgt++/Ual2NT+extw711eyR5RSsT3Z6Oiomp6eju35qDNjk6e0ga1ULODMxM6OHjNIwPL7/PZADwBGTnDXygFU5muezzM1U8a+I7PQvQNEAPtbo2DkA9du635uANpKItaFkxMROa+UGrXfzhk4tYl6MSvojN7v8zvNGK23makQ877WgFocMjCQAzRrn23BGwhekeH0c68YyLHagyLBAE5tot4sFLQ8Lcjz2yty3D4sgNaZ7wfztbbHywmw5HJRav8QsX4grC4YEEFz9n/7o0Xtz+208MpqDwqKAZzaRL1ZKOiMPszze/VE8apacQveALC6YGBs8lRzBv/zDxdRW/6mSvXOB4JXbl6H1R4UFAM4tYliMcs6M3WKicUhI9DzA2gGT6cxdbOW2cgJbi8sNgO1bgbfKT8fUGlc+KRkMYCTlp/NQk4BRbe4qOO2fh4kNeKnMsWc3XYyMwaA4nJ6JMqgbeW2gDk1U8bB45faZvjc5k6sAydHbrXYbifc+N1gc6vqPxh6pUbMseoCtDm71dU5+zE8ZODgo1tQ6SB458T7PsWC4Rq8nz52sSV4m9hGmBjAScvrCDK3gBp2g42OW2pkaqaMr78yqw3eAuCxB0rNGf1jD5TgI6a2+GC+hqePXXRM+TgRAJ+6b433/VwG5PVhyIXP/sYUSkbEnf/0qhxxC6h+NtgIEGhR1C018kfH/t5x8VEBOH15rvnv05fnHHPybqq1OlYM5FAw8m2viyw/z5CRw7ylJlEBePParbbb7dxm9l4B2vwQZH68P3EGngFJHMjrtRjo1jfDT6rC3K7u92dw2ub90Oa1rsERaLxeZgoozIy1Uq2hWqu3pUXU8lgGB9p/5mqtjsGBvOvr4XYl4vY1MzWk+/vYd2QWGxJqg0DxYQDPgCSOUfNqbOTWN8N6+oybIB9EuhNtHnughKPn/QUnM6jZW852Qjfbr9bq2jw10Mj1P/+FrRjWpGCs1SdmHn/DxAnc//QPsWHiBOYXFmFoEunDQ0Zz4dOpKRcQz4c9JYcBPAM6LY0L05DKaRY9v7CIqZmy5xFh4yMlnJnY6RnEg3wQjY+UsH/XJqwrFnCjUsXL5677Wiw1KehbznZbbjnJPfONh/HCnu3a18w6iwaA+nKJzgfzNSwBzbx9XgRP7FiPmW88DMC57YAVFzt7F3PgGdDJzsiwDanM+9jL18wFPfM+Xo/lJ2Whu4+Z03ULTvUI+vjoep5Era4U9h6Zxb5XZqFUI3B/e8/2ZuD2CsJ1y5S/rlTzquPo+bLvDzC3HaTMmWcXZ+Ap4DVT7qTNZxRpl/GRElataP+MD/I4fio37B9E9tloN61bXcATO9Z3/XmAOx8U5ofpM1MXO/o5q7V64KsP62ucxJqKTtIti+PQ7Z8x1AxcRPYB+A9oXJ1eBPAVpdSHUQysX/iZKXeyMzJo2sU+I3to81qcvjzn2m7Vz8/mlBe2Kleq2DBxAsWCgc9tuxsvn7seyezaj3KlihfPXovluayqtXqo53V7fcyqGJP9wz5ob5puzNaTblkchzh+xo7byYpICcDfAfhVpVRVRF4B8EOl1PedvoftZNt1o3UrAIx88w3trsHS8hvQHqyDXI67jU+3a5CilxfRBnGn3+/py3PNhltOvxsB8M7k7rYGXbcXFlGr33muKFrfduvvPk2i/Bm71U52AEBBRGoAhgDcCPl4fcfPTNnPDMjeJvWWJngbecFDm9e2zQpeOnstUG20U/pmaqaM/a9eaDZ3ou7Zcd8w3rx2S9vwy7o2YZ8Fun2wrisW2n6HbjtAwwTwfjh/M46fseMcuFKqDOBPAFwD8D6AW0qpN6IaWL/wKtfzk6+038esXLBbNTiA05fnHEvO/MiLOM6+Dp28wuAdk9nrt7Bi4M7bd9VgHisGcth3ZLYl1+q3rYEZ/A8ev+Trdxg2CPXD+Ztx/IwdB3ARGQbweQAbAawDsEpEntDc70kRmRaR6bm5OfuX+57XAqVTvvLg8UvNfwfpPRL2jeeUe52aKcey6EgNtxda687Nf9s/5P3+vs0PZb+pLwWEWpTrh/M34/gZw1Sh/BaAd5RSc0qpGoBjAD5tv5NS6rBSalQpNbp27doQT9ebvOqpnd6AlWqt+eYJ0nvE6dM/SH+Q/a9eaHnjPjN1EXuPzAZ4BOo2M83hZ7ZXKhY6Sod0Wr1ibXiWX66Rt//d9wKv93YUwixiPgjgzwD8OoAqgO8DmFZK/Ven7+EiZnBuNcLmYoifzRwA8MKe7Zi+elNb/TB2/xq8+7NqoFl0aXmBLGgOneIzdv8anHn7puPXBWjWpAPOi99u8iJYUspXhYqu1TDPA/XmtIgZJgd+DsBrAN5Eo4QwB+BwxyMkLbfLLXPm/dDmtZ4z6FWDeYyPlFoaO1m9+7MqzkzsDDQTN0vwGLzTyy14A41UiDVwHnhkS+DnqCvlu548ibYQvSxUFYpS6gCAAxGNhSysVSVO5zSaVQNHz5c9g+jthTqembroq0kVc9n9o2g5Im5dsYANvxhuga1aq2PvkVkcOnkl9hOT+hG30qeQ/TJTl+UyF0P8LmACwEtnrznWAedEsHHiBFYXDBh5aan7pd5Vqdaafw/lSrAUmptOT0yiYBjAU8gpKOtyjfsCLB4qAAuL9badesCd6pJKtQYjJxjICRZZEkghVGt1PPXKBew9MtvceDQ8ZMDISUupYq9Vn8SJATyFnC4nl5TCO5O7W24LmvLw6p0NgLXcFBlzYmDtrmjkBcWCgVvVGhtphcQAnkJBLjP379rk6wBhorSo1RVWrRjA7IGHkx5K5rEbYQoF2QAwPlLCJ9evjmtoRJHgomU0OANPIa/ug356ZRNFYcjIYYWR76g23K1jIhcto8EAHjOnxlTWoGz+8Vsb/1u/nykT6jbr5pqNEycCfa8A+IWVA67b8p0WLXnQRDAM4D5F8Yfl1B94+urNlnau5sxFV4oVpGyQqBMC4LEH7nQ0DLpQruDe9bBYMNquJnWta3uxR3jUmAP3IaoTTJx2obmdrmLfpca0CXWbAvDyueuYmiljaqaM2x8tdvxY9p29BSOPg482dnva31eVaq1t/wF3abrjDNyHoCeYOHEKvl6nz5QrVWycOIF1y01xWORH3Wae4xmWQqNnju7K1e/VJBc8nXEG7kNU23/NzmudMGf+DN6UNqViAUOGPpSYtysAP7n1IfZa+pUH6aJJegzgPkTVmD2ucx6J4lSuVB03iM3XlppXnta1na+/MovVBe8DrwXuDd36HQO4D1E0Zp+aKTvOwMPMzImyaEkB8wuLbe8rO3u3RGrFAO5D2Mbs5mKNbgZu5AVffvCeiEdMlH4LddV8Xzlx+xpxEdM360GxQbku1ihg9N41+MGF93mSO/Ud833ldNDD/l2bWBvugjPwGLgt1tSWFA6dvIKDj26BkWMqhfqHNXPodJULIJIS3l7FGXgMvDZC3KhUMT5SwrOvXwq8ZZkoqx5/cH3Lv3VXuWOTpyIp4e1VnIHHQLcIamUepsDgTdSKJ/i44wy8y6wncIvoT9dheSH1I/Nw7efGt7bc3nqcoL4pFmvDGxjAu0h3NJqRE9y1cgCV+ZrjHydRv3j53PWWAG5/z+jeH9YSXq8Fzl5fAGUKpYt01Se1JYWhwQG8M7kbSwze1OfsAdpre721hNerR1FUPYzSjDPwLuIJ8ETu8iIts2S3KU1xeefmvuVT729/tKhd4Hz29UuO/fJ7bQGUM/Au8tqCv3/XprZubUT9pK4U9h2Z9dXnp1KttcymnfZNfDBf86z66hWpD+BTM2WMTZ7CxokTzSY4WRmL1xb88ZESHt+xXvetRH0j7kRiLy2ApjqApymH1clY/GzBH713TfcHT0QAgvcwSjtRMS6kjY6Oqunpad/3H5s8pb0UKhULODOxM8qhxTIW+4r4Q5vXtpzEQ0TdU8pwFYqInFdKjdpvT/UiZpqK+IOMRVe6BKDtOLWXzl5jf28inzo9zMR6vmevSXUAd6rSSCKH5XcsUzNl7H/1AmpLd3ofO51swuBN5N/jO9bj9OW5QJVbWZ51+5HqHHgUfbjjHsvB45eawZuIorFqMI/nxrfizMROvLBnu2cf8YKRxwt7tuPMxM6eDd5AygN42D7cSYyFLWGJorewuNQsGNC9F5/YsT4VcSJuqV7EzKINEyeSHgJRT0qieCEtMrmImSVTM2U8+/qlpIdB1LPKlSqmZsqBTsLq5T4oAAN4YLo/iumrN1lRQhSDp49dBIBmLxSnAG1vimXu25i+ehOnL8/1TFBnCiUA3bFPRl5QqzN0E8XFrCzRHcFm5r6d9m3YSxGzUmLolEJJ9SJm2mi7CzJ4E8XKLM11amQFOO/bsL9bzeZWWRUqgItIUUReE5HLIvKWiHwqqoGlUS81wSHqRR/M1zA1Uw60VyTL7+uwOfDvAPgrpdQXRWQQwFAEY0ottn8lSr+nXrmAHfcNt7WnddrJaQb7LC56djwDF5GPAfhNAN8DAKXUglKqEtXA0ki3mcfIC0+TJ0qRulI48/bNtmCtgLb2zeZmvDQ1zgsiTArlPgBzAP5cRGZE5Lsissp+JxF5UkSmRWR6bm4uxNMlT7eB4NAXt+HQ725r3sZYTpRe1iBu3fCjW9/KQn48TAplAMAnAXxVKXVORL4DYALAH1vvpJQ6DOAw0KhCCfF8sXO6pHK6rHr29Us8WZ4o5RTaNwWlqXFeEGEC+HsA3lNKnVv+92toBPCe4FRHCqDt0FQGbqJssQfmNDXOC6LjFIpS6icArouI2c3pMwB+FMmoUsDPJZUZ5Bm8ibLFHpjT1DgviLBVKF8F8NJyBcqPAXwl/JCSNzVTdqw2sX5ye52gTUTpowvM5lV11qpQQgVwpdQsgLbdQVlmzqqdWD+5054fI6JWxYKBg49uaQvMWSwhBNgLpY3brDonwPzCIjZOnEBxyIh5ZEQUVKlY8AzKfte70oi9UGw2TpxgUyqiHlAsGJg98DCembqIl89dR10p5EXw5Qfvwei9a5oz7pwI6po4mKb2tWwn62FqpoyDxy8xeBP1CBHgmamLePHsteZtdaXw4tlrePn/Xkd9+eQsXfAGspEiZQBH+zmWnRIA70zuBsCDHYiSVpmv4eVz17Vfq/t4r6e9hBBgAAfQyHtHcY7lumKhuRhCRMkqGDnM15Y6/N70lxACPRjAg6wmm/eNokFVwchjwy8WHE+gJ6J4BQ3eeREsKcUqlKQEWU3WHc6gY/2lPrR5bfM0j+KQAaWAW9Va82vWXBsRpVc+Jy1plKwc7GDXUwHcbfek/RfjZxOOkRcc+uI21xn8weOXUK5UGbyJUqpg5LCwqByrULI047brqQAepCGN1wrz8JCBA4/oC/7Z+4QoOz6sLTWLC4B4N+10+7l6KoAHaUjjdF+32s+pmTL2v3aBx6gRZYj1/R/npp04nqunzsQM0pBGd19B40UemzylbeR+6OQVBm+iDDFy0vL+d0qzHjx+CWOTp7Bx4oTj+z+oOHqM99QMPEhDGut9y5Vqy3FLTp+UPE6NKFvuWjnQ8h52Sp1WqjVUqo20aFQz5Th6jPdUAAfgeuCC033HJk+1BWfzhGvzw2B1gb1PiLKmYlur8nuurVPxQxBx9BjvqRRKp5w+ET+YrzXPyDM/nYkoO/z0/XaiiwtTM2XfqZY4eoz33Ay8Ezxtnqj32IOlWRFSrdWRX25gVSoWML+wqK0qswf/oIuScfQYZwBH45PSz6YeIko3WV7MsgdLe/CtK9US4O3vf91MOcg+E1OQlG4nGMCh/6S8/dEi0yZEGaMU8K6m5lt3hW0G3zMTOzF99WZLy9nHHmgPvGk8+JgBfJn9k9LvVnsiSpexyVOOM2u7cqWKDRMnWqrQ6krh6PkyRu9d0xIT0njwMRcxHYyPlPD8F7aiVCxA0OiJQkTpV65UsffILPa9Mut7Ambf3aGr107jwcecgbuwzso3sr83UaaEPWzMnhpJ48HHDOA+sVKFqL/oUiPdXpQMqidTKEFqNf0KUj9KROlUMPJ4Yc92lHzkrXmgQwI6aSDjp2OYfes9EWVLyfLenr5607UF9PCQkaqZtpOeC+B+ajWtAXt1wcDthcVmkyprwDcfzxrYz0zs1G69J6L0MvKC2x8tYt+RWRw6eQXzC4uO9xUAu3/t7ua/42w/G1TPBXCvWk37DF1X6232QfmwttQ2k391+lomTqsmojtqddXSrMqNApplhABiaz/biZ4L4F61mn5O4gGg3VpbrdVx5u2b4QdJRKlmLSMMuvsyTj23iOlVqxnn7Jml40TZdaNSTeXuS6ueC+D2DTilYqHlsFI/u6YKRh7FgO1j7R8aRl7adwcQUdcVjByimDutKxYc40WSuy+tei6FArjXauoaVxk5wV0rB1CZrzUXKQDvbbimnAArBnLN+64azGNhcYnxmygB1dpS6McI2ugqKT0ZwN0E3U1l3i+33H5SZ0m1LobOL9QZvIkyJi+CJaW0McErXiRVqSIq7H7TAEZHR9X09HRszxeljRMnGJSJUqZg5H33O8m7TMKARvmg9fR6v3SN7wpGviV1G5aInFdKjdpv77kceFTsuzl5pBpR+tjXu4aH9O/TUrGAt5//LN6d3O24C7PTvHYchxc76bsUih+63ZxGXmDkBLUlzsOJ0mDVYN5XG2h7zlq3DhYmr51kpQpn4BrPvn6p7RO1Vle4a+WArx4KRNR9/+6T+mPMzFk50EibmLNhsyeSV6VaUElWqjCA20zNlLWbeIDGCddnJnbihT3b2diKKGGnL89pbx8fKTX3g5g5b3MHpTWIn5nYiW/v2Q4A2HdktuPGd0n2CQ8dwEUkLyIzIvKDKAaUNLe8lfmJOj5SwmMPJL8Li6ifuaUo/OSlzXRLuVKFQnuQ9yvqGX0QUeTAvwbgLQAfi+CxEjU1U3btk2B+ok7NlHH0fPgWtUTUObcUhVNwL1eqGJs85Vga3Ok2+aT6hIcK4CLyCQC7AfwXAF+PZEQJMT+NnQjQ0smMZ2USJUfg3q/bqSeS4E4zK6eSwrRsk/cjbArlBQB/CMBx65OIPCki0yIyPTenz1mlgVeTK7X8v3Kl6pgjd8KWKETRUmi8Z50ObdHlpa0HF7tJyzZ5PzqegYvI5wD8VCl1XkT+rdP9lFKHARwGGht5On2+IDrZFdXNT10WHhJFz5xJ61q86nZc++nhb118THMfcFOYFMoYgEdF5LMAVgL4mIi8qJR6IpqhdaaTE3kAnnlJlGW63LU9L+10EItuC32ncSRuHadQlFJPK6U+oZTaAOD3AJxKOngDne+KcjrzMueS/2BqhCg9vK6incr9vvWlbXhncjfOTOxsmbkntbsyiJ7bidnprijzF3fw+KWWxlRuGy8VvPsrEFE8vHLXQRrZpb0PuCmSAK6U+lsAfxvFY4XldSKPm/GREg6dvKI9Zs0JgzdROjy0ea3nffyW+4WJI3HquZ2YYXdFBf2EzfPYHaJUcNqZ2Ykkd1cG0XMBPOyuqCCfsAUjjy8/eA+31ROlQJTpjSR3VwbRczlwINyuKF2nMp28SPMXOnrvGhw6eYVVLEQJijq9kdTuyiB6bgYelv2Td3jIgGErRTFXrs1yI3NRpFgwGmdh+sTOhkTBrRrMa9+TaUtvxKEnZ+Bh6XoM61au7bWilWoNRk4wPGR47tYcHjKwf9cm7Dsyy40+RAEsKWDPb9yDH1x4v1lwsNLoz7koj1QLwW1jgNfRTasLBm5VawzeRB0YHjLwYW2pq8eYpQmPVOsCp0UTr9JChcZsncGbqDMfzNcysdGm2xjAQ0hbTShRrwlapJu2jTbdxgAegtP2eyKKxuM71mvrsYsOh4z326SKATwEe8WKn0093PZD5N9z41u19dgHH92SiY023cYqlJCsFSu6E7HtBnJAzbF7OlFvG8wLFBqHhHsZHmrMst3qsbvV7jULrWQBBvBIWZvlOG3qYfCmfrZQV76uQo284MAjW1zv062NNllpJQswhRI580RsItLzmnsLgD2/fk9iwTIrrWQBBvDIeZ2tSUTuFKJtTBVUVlrJAgzgkfM6W5OIvCUZLJ0qWdJY4cIAHrFO/vDYkpaoVZLBMiutZAEG8Mg5/eHlRTB2/5q2BRy2pCVqlXSwzEorWYC9UCLnVkpYMPJ47IESTl+eQ7lSbfZMKRULeGjz2ubtRL3A73GDw0MGhgYHUl+ylySnXigsI4yY+Yf31CsX2v54q7U6Tl+ea+s5Xq5UcfR8Gc9/YSsA+OpHTpR2daWak5aXzl7TVp8IgAOPbGHA7hBTKF0wPlLCksPM40al6lqmND5SwmMPlLhjk3qCOWlxopC+2uosYQDvEreVbK8ypdOX59ipkHqGmRrR4aEm4TCAd4nbSrZXmVIa602JvDhVU60uGJhfWGy7PenFyl7AAN4lbivZXmVKaaw3JfJi5rytjJzg9sJi2wlVxYKR2sqOLOEiZhc59Wqw9kzRrbzzqDXKqpVGDisGcrhVrWFdsYB5TfAGgFUrBhi8I8AAnhDduZtjk6eaAf3T96/B/377JoM4ZcoH8zUUjDy+vWc7xkdK2DhxQns/pgmjwRRKCpi14+VKFQqNssI3r93C4zvWc5GHMsfa+ClL29KziDPwhFj7Dec0Gx6qtTpePHstVAA3N1IIvDvAEUXJnGE/tHltWw04Fy+jwwCeAPtuTbfdauVKteMAbN1I8fK56752xRFFoThkYOSbb7TlvwXAYw90p493P2IKJQFBOxYqdH4Um7mR4ltf2sZ+KxQLIy/4+Yf6xcukW8X2GgbwBHSygKPQedfC8vLuz8ceKDGnTl1jlsuuGhxAbcn5ao8LmNFhAE+AW8dCJ6ViIdQs2uy3sn/XJgZx6gqzHPZWtX3mbb8fRYMBPCZmmeDGiRO4/dEijHxrsC4YeXzrS9vwwp7tjpt87JuDhocMGDn/s3KzOkC3kUgA/PIvrer0xyNqnh1ZXD6MWIcLmNHiImYM7IuWlWoNRk4wPGSgMl/TttB02uSjqx+33terLe2NShXjIyVMX73ZUh2gALz7s/mu/PzUG/IiWFIKxSEDSjX+ju2qtTpWDORQMPJt6zzFgoGDj7LzYJQYwGOgW7SsLSkMDQ5g5hsPt90/yGnbTvcdmzylDeLm5euJv3+/rbKlVmeVCukJgG99aVvL39oGh006t6o1fHvPdsdJCEWn4wAuIvcA+EsA/xrAEoDDSqnvRDWwXpLEIan2nuPAncvXqZmytkKASEcAPL5jfduVn1N567piIdAkhDoXZga+COAppdSbIvILAM6LyF8rpX4U0dh6xrpiwXU23A1u/Va2P/tGJM+RE8Cl2IB6QGn57wZAS6uH+YVFxwMamOOOT8cBXCn1PoD3l//7X0TkLQAlAAzgNm6z4W7SzYKmZsra3GUnGLyjocsXp0GpWMCZiZ1tazhux/7xgIZ4RVKFIiIbAIwAOBfF4/WaNB2Savao8GvVYD5QpQsFZ/5tJMXIS9vv2DrBCLLxjCWq8Qq9iCkidwE4CmCvUuqfNV9/EsCTALB+/fqwT5dZackJBsm7C4BL3/wdPDN1ES+evda9QfWxvEjL34Zu+3lUjLxg1eAAKtVay4Ha1qV5GvsAAAllSURBVECtW3T0+zfDEsH4hQrgImKgEbxfUkod091HKXUYwGGgcSp9mOej8Jzy8U73Bbj1uZt23Dfc8u8Dj2zB/tcutFQEGXnBb2wYxpm3b4Z6rlpdoVKtNYO2fULhNMHw8zfj9JjUXR2nUEREAHwPwFtKqT+NbkjUTX5nSEZOmhUrfgM+BffuzxqvrbnRa9+RWawaHMDwkNFMtx364ja89B8/hSd2rO+4nYJVuVLF3iOz2P7sG5iaKXvef/+uTW0bz6wEwJmJnQzeCQiTAx8D8PsAdorI7PL/PhvRuKhLxkdKGHbZKQc0Nlwc+t1tAICnj110vJ8AeGLHejbJCuFGpdrWD75SreHD2hK+vWd7S2B8bnwr3n7+s3hiRzSpyEq1hqePXfQVxN3aYXJrfHLCVKH8HTpvkkcJOvDIFm1VjH1hdWzylOPilVkb/Nz4VgBo6/ncDUZeem6z0bpiQbtIaLY90M1q3VJaeU1veTduz2M6dPKKY3Mq5r2TxZ2YfchaI16uVJEXaTlFxc/ilXlkFtAIKHGE1SjywGkicC/JC7oBTAAsddDz3WuR0u3rPJg4WQzgfcp809nre82UyfhIyXHxqrS8087kt0oh7MlAZ3/8QYjvbpUXwZcfvAej965pfpAFHZ9ZMudnjUAEUCrYKUlux5G5bQwLumZhfx57f53VBUO7d8D+d0DxYwDvY16X7n43IPmpUjBPBgpTjhj2RCFdmgi482FmD1yV+QXcXtCnkKyvg/01srKnmgDnPjVOj2/n9XvZ/+qFtpRHThr3sf889ufRbdox68Stj8nUSTowgPcxr0t0t+34Vvt3bcLeI7OOz2MtMXPrlGhymp0Gze86jcGJtR57aqaM/a9e0N5veMjAgUfudNWbvnqzeWSdABgazGN+oe74enldsZgprWdfv4SDxy/hVrW1Y6Wf38vB45eas2breHXdKw+dvIJ9R2abW+TbGq/VFYaHDAwNDrA5VcqIivGcxNHRUTU9PR3b85E7p5mguYU6iO3PvuF4mW19LK9NQU5B2pzBHz1fDrztvFgwsGpFe/CxBzNrUHJ6bcyWqOb3FYcM/PzDxbbZqVtu2Omxh4cMfFhbcvz5nB7X7edwY59tuxEA70zu9rwfdYeInFdKjdpv54EOfUx3sEOnl8YHH93i67G8NgVZg7dZ4mS2HnhufGtLS4Jiwb0c0nR7YbFZoleuVLH/tQv4lT/+n9h7ZLbl9n1HZvHMVGMNwGmWbJbemd/3wXytLV1hpqGsh3iMTZ5qlus5ve5KwTWYWheaTfYSRHMdw09pYJAt8iwVTCemUPqY3xRJlI8VZCu/QvsM3t6SwGvruaC9z3mtrrTliAqNcsjRe9c45vXN9IYXM5A6LRAD7a/VPpc0lMn++gUtQXR7LCfMd6cXA3ifs+d9rfnQoMHcT7+XIFv5Ae8gU/HoGxI0QaiA5rFzuoVCvzNWXaC3Blbda2VWw7ixz4TD9Jp3+l04pZwofZhCIQD6S/Eg2639ckofOKVDvC7d3b7+xI71HXXHM4+d03WQ9PN4AueKGbfAqnttrJwqgHT8pDycfhcHH92CMxM78c7kbm6RTznOwAmAcz7UzPkC0fR5dkofAO3leG6X7ubVgq5+21q6F2ShzmQGP6crCq/HU3CupHELrPbXxjx70l6FYhWm13yUKTRKBqtQCACwceKEa7qhk8qUoPxWU+iCshkwdeWC1sfVVY1YmdUupy/POY5jaqaMp1654FnSaA/iXtUpneq0CoWyw6kKhTNwAuCdm9Zd+kcdOPz2TNddLegWPHWGBgew+9fubgbo1QUDIo1culkXbS1V1C0+jo+UfC04mmPqdmBNS695ih8DOAHQX4pb6bZbe1VZdEuQhTvdOI+eLzvOhHUNvHRVHX57ZHf7qoX6GxcxCcCdY990rWZ1OVW38rVuC7JwF3Scfj8cOllwJIoaAzg1jY+UMPONh/HCnu2e53eGKV8LK8gGpKDj9PvhYK9SGR4yUCwYiZ95Sv2FKRRqE6aeO44de0GqJ4KOM0hVR6/knrkIml0M4NSRMOVrUfAbPIOOM2xpXdaCYZJrGRQeAzh1JCs1xJ2Ms9OZdRaDYZit+JQ8BnDqWFZSCHGNM4vBMMm1DAqPAbwPZO2yPquyGAyTXMug8FiF0uPCtBulYML0JUlKlC2FKX4M4D0uyXrtfpPFYOjUtItXaNnAFEqPy+JlfVZlZWHXLitrGdSOAbzHMccZLwZDihNTKD0ui5f1ROQPZ+A9LquX9UTkjQG8D/Cynqg3MYVCRJRRDOBERBnFAE5ElFEM4EREGcUATkSUUbGeSi8icwCuxvaE6fNxAP+U9CBShK9HK74e7fiaNNyrlFprvzHWAN7vRGRaKTWa9DjSgq9HK74e7fiauGMKhYgooxjAiYgyigE8XoeTHkDK8PVoxdejHV8TF8yBExFlFGfgREQZxQBORJRRDOBdJiL3iMhpEXlLRC6JyNeSHlMaiEheRGZE5AdJjyUNRKQoIq+JyOXlv5VPJT2mJInIvuX3yz+IyMsisjLpMaURA3j3LQJ4Sin1KwB2APhPIvKrCY8pDb4G4K2kB5Ei3wHwV0qpzQC2oY9fGxEpAfjPAEaVUv8GQB7A7yU7qnRiAO8ypdT7Sqk3l//7X9B4Y/Z1c24R+QSA3QC+m/RY0kBEPgbgNwF8DwCUUgtKqUqyo0rcAICCiAwAGAJwI+HxpBIDeIxEZAOAEQDnkh1J4l4A8IcAlpIeSErcB2AOwJ8vp5W+KyKrkh5UUpRSZQB/AuAagPcB3FJKvZHsqNKJATwmInIXgKMA9iql/jnp8SRFRD4H4KdKqfNJjyVFBgB8EsB/U0qNALgNYCLZISVHRIYBfB7ARgDrAKwSkSeSHVU6MYDHQEQMNIL3S0qpY0mPJ2FjAB4VkXcB/HcAO0XkxWSHlLj3ALynlDKvzF5DI6D3q98C8I5Sak4pVQNwDMCnEx5TKjGAd5mICBq5zbeUUn+a9HiSppR6Win1CaXUBjQWpk4ppfp6dqWU+gmA6yKyafmmzwD4UYJDSto1ADtEZGj5/fMZ9PGirhseatx9YwB+H8BFEZldvu2PlFI/THBMlD5fBfCSiAwC+DGAryQ8nsQopc6JyGsA3kSjimsG3FKvxa30REQZxRQKEVFGMYATEWUUAzgRUUYxgBMRZRQDOBFRRjGAExFlFAM4EVFG/X+8je/FJ/2GJQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Normal data distribution\n",
    "norm = numpy.random.normal(5.0,1.0,100000) # First parameter is  : mean of the total value and Second vlaue is Standard deviation of that mean value\n",
    "normY = numpy.random.normal(5.0,1.0,100000) # First parameter is  : mean of the total value and Second vlaue is Standard deviation of that mean value\n",
    "plt.hist(norm,100)\n",
    "plt.show()\n",
    "\n",
    "# Ploting the scatter diagram\n",
    "plt.scatter(norm,normY)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value of mymodel list: [94.3495217071376, 90.84694628403237, 89.09565857247976, 90.84694628403237, 99.60338484179543, 73.33406916850626, 99.60338484179543, 87.34437086092716, 96.1008094186902, 83.84179543782193, 82.09050772626932, 87.34437086092716, 92.59823399558499]\n"
     ]
    }
   ],
   "source": [
    "# Linear regression\n",
    "\n",
    "\n",
    "x = [5,7,8,7,2,17,2,9,4,11,12,9,6]\n",
    "y = [99,86,87,88,111,86,103,87,94,78,77,85,86]\n",
    "\n",
    "slope, intercept, r, p, std_err = stats.linregress(x, y)\n",
    "\n",
    "def myfunc(x):\n",
    "    return slope * x + intercept\n",
    "\n",
    "mymodel = list(map(myfunc, x))\n",
    "\n",
    "plt.scatter(x, y)\n",
    "plt.plot(x, mymodel)\n",
    "plt.show() \n",
    "stats.linregress(x, y) # Trying to understand the behavior of this function\n",
    "print(\"Value of mymodel list: \"+str(mymodel))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "5\n",
      "6\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(4, 5, 6)"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Understanding multiple variable init\n",
    "\n",
    "def data():\n",
    "    return 4,5,6\n",
    "a,b,c = data()\n",
    "print(a)\n",
    "print(b)\n",
    "print(c)\n",
    "data()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Polyinominal regression\n",
    "\n",
    "\n",
    "x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] # Hour of the day that the card pass the tollbooth\n",
    "y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]  # speed of the car\n",
    "\n",
    "mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))\n",
    "myline = numpy.linspace(1, 22, 100)\n",
    "\n",
    "# creating the scatter plot\n",
    "plt.scatter(x,y)\n",
    "plt.plot(myline, mymodel(myline))\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
