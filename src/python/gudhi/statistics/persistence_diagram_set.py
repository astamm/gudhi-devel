class PersistenceDiagramSetIterator(object):
    """
    Iterator class
    """
    def __init__(self, diagram_set):
        self._diagram_set = diagram_set
        self._index = 0
    
    def __next__(self):
        '''Returns the next value from team object's lists'''
        if (self._index < len(self._diagram_set)):
            old_index = self._index
            self._index += 1
            return self._diagram_set[old_index]
        raise StopIteration

class PersistenceDiagramSet(object):
	"""docstring for PersistenceDiagramSet"""
	def __init__(self, diagram_list = [], sample_description = ""):
		super(PersistenceDiagramSet, self).__init__()
		self.sample_description = sample_description
		self.diagram_list = diagram_list
		self.diagram_representation = "Persistence Diagram"
		self.diagram_metric = "Bottleneck Distance"

	def __repr__(self):
        return "PersistenceDiagramSet()"
    
    def __str__(self):
        return """
        Sample of persistence diagrams

        {sample_description}

        Size: {sample_size}
        Representation: {representation}
        Metric: {metric}
        """.format(
            sample_description = "No description provided" if self.sample_description is None else self.sample_description, 
            sample_size = len(self.diagram_list), 
            representation = self.diagram_representation, 
            metric = self.diagram_metric
        )

    def __len__(self):
        return len(self.diagram_list)
    
    def __getitem__(self, item):
        return self.diagram_list[item]
    
    def __iter__(self):
        ''' Returns the Iterator object '''
        return PersistenceDiagramSetIterator(self)

    def add_diagram(self, diagram_value):
    	self.diagram_list += [diagram_value]

    def set_description(self, description_value):
    	self.sample_description = description_value

    def set_representation(self, representation_class):
    	self.diagram_representation = representation_class.__name__
        self.diagram_list = representation_class.fit_transform(self.diagram_list)

    def set_metric(self, metric_value):
    	self.diagram_metric = metric_value
