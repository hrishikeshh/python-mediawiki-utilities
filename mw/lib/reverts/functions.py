from .detector import Detector

from . import defaults

def reverts(checksum_revisions, radius=defaults.RADIUS):
	"""
	Detects identity reverts that occur in a sequence of revisions based on 
	matching checksums and limited by a radius -- the maximum distance that a
	revert can span.
	
	:Parameters:
		checksum_revisions : iterable((checksum, revision))
			an iterable of checksums and revisions 
	
	:Return:
		a generator of (reverting, reverteds, reverted_to) for each reverting revision
	"""
	
	revert_detector = Detector(radius)
	
	for checksum, revision in checksum_revisions:
		revert = revert_detector.process(checksum_revisions)
		if revert != None: yield revert
