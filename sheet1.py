# 1.1 - two buckets problem

# a) 

# State representation: [W1/W2] -> W1:0..4, W2:0..3
# Initial state: [0/0]
# Objective state: [2/_] or in general case [NL/_]
# Operators: fill a bucket completely - bucket cant be full - fills the bucket to its max capacity - cost 1
#            empty a bucket - bucket cant be empty -  empties the bucket to contain no water -  cost 1
#            pour bucket into another one - goes until either the second one is full or the first one is empty - transfers water between containers - cost 1
# Objective Test: check that bucket A contains exactly two liters


# b)

# Initial state: buckets A and B both empty
# DUVIDA

