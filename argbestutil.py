def argbest(candidates, transform_func, best_comparator):
	best_val = None
	argbest = None
	for candidate in candidates:
		this_val = transform_func(candidate)
		if best_val == None or best_comparator(best_val, this_val) == this_val:
			best_val = this_val
			best_arg = candidate
	return (best_arg, best_val)

def argbest_generator(candidate_generator_func, transform_func, best_comparator, stop_val = None):
	best_val = None
	argbest = None
	candidate = candidate_generator_func()
	while candidate != stop_val:
		this_val = transform_func(candidate)
		if best_val == None or best_comparator(best_val, this_val) == this_val:
			best_val = this_val
			best_arg = candidate
		candidates = candidate_generator_func()
	return (best_arg, best_val)


class ArgbestFinder:

	def __init__(self, transform_func, best_comparator):
		self.best_val = None
		self.argbest = None
		self.transform_func = transform_func
		self.best_comparator = best_comparator

	def add_candidate(self, candidate_arg):
		this_val = self.transform_func(candidate_arg)
		if self.best_val == None or self.best_comparator(self.best_val, this_val) == this_val:
			self.best_val = this_val
			self.argbest = candidate_arg
		pass

	def get_argbest(self):
		return self.argbest

