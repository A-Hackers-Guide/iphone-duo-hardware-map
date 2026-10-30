# `CLRacingRouteVariables`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 30 instance variables, 30 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _raceStartPointDetected;
B _raceEndPointDetected;
B _userIsOffRoute;
B _projectedOnNearestPoint;
B _raceSessionExpired;
B _rollingBufferReachedEndOfReferenceRoute;
B _routeConfigurationSuccessful;
B _racingRouteAnalyticsSent;
B _prematureRaceEndDetected;
B _referenceRouteTotalLengthDetermined;
B _locationPointIsOutsideOfAcceptedRange;
B _locationPointNotMatched;
i _routePointsBufferSize;
i _numberOfRoutePointsToAdd;
i _offRouteGraceDuration;
i _matchedPointCounter;
i _referenceRouteDataPointCounter;
i _currentRouteDataPointCounter;
i _offRouteDataPointCounter;
i _inutileDataPointCounter;
i _rollingBufferUpdateCounter;
i _lastMatchedPointIndex;
i _lastMatchedPointIndexOnReferenceRoute;
i _rollingBufferStartIndexOnReferenceRoute;
i _matrixCellIndexForLastMatchedPoint;
d _referenceRouteTotalLength;
d _timestampOfLastMatchedPointOnReferenceRoute;
d _registeredTimeAtThresholdDistance;
d _endOfRaceTimeThreshold;
d _nearestNeighborMaximumAcceptedDistance;
```

## Properties

```
@property (TB,R,N,V_raceStartPointDetected) raceStartPointDetected;
@property (TB,R,N,V_raceEndPointDetected) raceEndPointDetected;
@property (TB,R,N,V_userIsOffRoute) userIsOffRoute;
@property (TB,R,N,V_projectedOnNearestPoint) projectedOnNearestPoint;
@property (TB,R,N,V_raceSessionExpired) raceSessionExpired;
@property (TB,R,N,V_rollingBufferReachedEndOfReferenceRoute) rollingBufferReachedEndOfReferenceRoute;
@property (TB,R,N,V_routeConfigurationSuccessful) routeConfigurationSuccessful;
@property (TB,R,N,V_racingRouteAnalyticsSent) racingRouteAnalyticsSent;
@property (TB,R,N,V_prematureRaceEndDetected) prematureRaceEndDetected;
@property (TB,R,N,V_referenceRouteTotalLengthDetermined) referenceRouteTotalLengthDetermined;
@property (TB,R,N,V_locationPointIsOutsideOfAcceptedRange) locationPointIsOutsideOfAcceptedRange;
@property (TB,R,N,V_locationPointNotMatched) locationPointNotMatched;
@property (Ti,R,N,V_routePointsBufferSize) routePointsBufferSize;
@property (Ti,R,N,V_numberOfRoutePointsToAdd) numberOfRoutePointsToAdd;
@property (Ti,R,N,V_offRouteGraceDuration) offRouteGraceDuration;
@property (Ti,R,N,V_matchedPointCounter) matchedPointCounter;
@property (Ti,R,N,V_referenceRouteDataPointCounter) referenceRouteDataPointCounter;
@property (Ti,R,N,V_currentRouteDataPointCounter) currentRouteDataPointCounter;
@property (Ti,R,N,V_offRouteDataPointCounter) offRouteDataPointCounter;
@property (Ti,R,N,V_inutileDataPointCounter) inutileDataPointCounter;
@property (Ti,R,N,V_rollingBufferUpdateCounter) rollingBufferUpdateCounter;
@property (Ti,R,N,V_lastMatchedPointIndex) lastMatchedPointIndex;
@property (Ti,R,N,V_lastMatchedPointIndexOnReferenceRoute) lastMatchedPointIndexOnReferenceRoute;
@property (Ti,R,N,V_rollingBufferStartIndexOnReferenceRoute) rollingBufferStartIndexOnReferenceRoute;
@property (Ti,R,N,V_matrixCellIndexForLastMatchedPoint) matrixCellIndexForLastMatchedPoint;
@property (Td,R,N,V_referenceRouteTotalLength) referenceRouteTotalLength;
@property (Td,R,N,V_timestampOfLastMatchedPointOnReferenceRoute) timestampOfLastMatchedPointOnReferenceRoute;
@property (Td,R,N,V_registeredTimeAtThresholdDistance) registeredTimeAtThresholdDistance;
@property (Td,R,N,V_endOfRaceTimeThreshold) endOfRaceTimeThreshold;
@property (Td,R,N,V_nearestNeighborMaximumAcceptedDistance) nearestNeighborMaximumAcceptedDistance;
```

## Class methods

```
+[CLRacingRouteVariables supportsSecureCoding];
```

## Instance methods

```
-[CLRacingRouteVariables encodeWithCoder:];
-[CLRacingRouteVariables initWithCoder:];
-[CLRacingRouteVariables copyWithZone:];
-[CLRacingRouteVariables currentRouteDataPointCounter];
-[CLRacingRouteVariables endOfRaceTimeThreshold];
-[CLRacingRouteVariables initWithRaceStartPointDetected:raceEndPointDetected:userIsOffRoute:projectedOnNearestPoint:raceSessionExpired:rollingBufferReachedEndOfReferenceRoute:routeConfigurationSuccessful:racingRouteAnalyticsSent:prematureRaceEndDetected:referenceRouteTotalLengthDetermined:locationPointIsOutsideOfAcceptedRange:locationPointNotMatched:routePointsBufferSize:numberOfRoutePointsToAdd:offRouteGraceDuration:matchedPointCounter:referenceRouteDataPointCounter:currentRouteDataPointCounter:offRouteDataPointCounter:inutileDataPointCounter:rollingBufferUpdateCounter:lastMatchedPointIndex:lastMatchedPointIndexOnReferenceRoute:rollingBufferStartIndexOnReferenceRoute:matrixCellIndexForLastMatchedPoint:referenceRouteTotalLength:timestampOfLastMatchedPointOnReferenceRoute:registeredTimeAtThresholdDistance:endOfRaceTimeThreshold:nearestNeighborMaximumAcceptedDistance:];
-[CLRacingRouteVariables inutileDataPointCounter];
-[CLRacingRouteVariables lastMatchedPointIndex];
-[CLRacingRouteVariables lastMatchedPointIndexOnReferenceRoute];
-[CLRacingRouteVariables locationPointIsOutsideOfAcceptedRange];
-[CLRacingRouteVariables locationPointNotMatched];
-[CLRacingRouteVariables matchedPointCounter];
-[CLRacingRouteVariables matrixCellIndexForLastMatchedPoint];
-[CLRacingRouteVariables nearestNeighborMaximumAcceptedDistance];
-[CLRacingRouteVariables numberOfRoutePointsToAdd];
-[CLRacingRouteVariables offRouteDataPointCounter];
-[CLRacingRouteVariables offRouteGraceDuration];
-[CLRacingRouteVariables prematureRaceEndDetected];
-[CLRacingRouteVariables projectedOnNearestPoint];
-[CLRacingRouteVariables raceEndPointDetected];
-[CLRacingRouteVariables raceSessionExpired];
-[CLRacingRouteVariables raceStartPointDetected];
-[CLRacingRouteVariables racingRouteAnalyticsSent];
-[CLRacingRouteVariables referenceRouteDataPointCounter];
-[CLRacingRouteVariables referenceRouteTotalLength];
-[CLRacingRouteVariables referenceRouteTotalLengthDetermined];
-[CLRacingRouteVariables registeredTimeAtThresholdDistance];
-[CLRacingRouteVariables rollingBufferReachedEndOfReferenceRoute];
-[CLRacingRouteVariables rollingBufferStartIndexOnReferenceRoute];
-[CLRacingRouteVariables rollingBufferUpdateCounter];
-[CLRacingRouteVariables routeConfigurationSuccessful];
-[CLRacingRouteVariables routePointsBufferSize];
-[CLRacingRouteVariables timestampOfLastMatchedPointOnReferenceRoute];
-[CLRacingRouteVariables userIsOffRoute];
```
