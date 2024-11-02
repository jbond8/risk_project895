import risk

results = [
  [
    {
      "slope": 0.48,
      "intercept": 0,
      "x_min": 0,
      "x_max": 6.25
    }
  ],
  [
    {
      "slope": 0.26666666666666666,
      "intercept": 1.3333333333333333,
      "x_min": 6.25,
      "x_max": 25
    }
  ],
  [
    {
      "slope": 0.16,
      "intercept": 4,
      "x_min": 25,
      "x_max": 56.25
    }
  ],
  [
    {
      "slope": 0.11428571428571428,
      "intercept": 6.571428571428572,
      "x_min": 56.25,
      "x_max": 100
    }
  ]
]

risk.plot_utility(results)