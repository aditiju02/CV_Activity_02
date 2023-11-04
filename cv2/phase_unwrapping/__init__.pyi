import cv2
import cv2.typing
import typing


# Classes
class PhaseUnwrapping(cv2.Algorithm):
    # Functions
    @typing.overload
    def unwrapPhaseMap(self, wrappedPhaseMap: cv2.typing.MatLike, unwrappedPhaseMap: cv2.typing.MatLike | None = ..., shadowMask: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def unwrapPhaseMap(self, wrappedPhaseMap: cv2.UMat, unwrappedPhaseMap: cv2.UMat | None = ..., shadowMask: cv2.UMat | None = ...) -> cv2.UMat: ...


class HistogramPhaseUnwrapping(PhaseUnwrapping):
    # Classes
    class Params:
        width: int
        height: int
        histThresh: float
        nbrOfSmallBins: int
        nbrOfLargeBins: int

        # Functions
        def __init__(self) -> None: ...



    # Functions
    @classmethod
    def create(cls, parameters: HistogramPhaseUnwrapping.Params = ...) -> HistogramPhaseUnwrapping: ...

    @typing.overload
    def getInverseReliabilityMap(self, reliabilityMap: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getInverseReliabilityMap(self, reliabilityMap: cv2.UMat | None = ...) -> cv2.UMat: ...



