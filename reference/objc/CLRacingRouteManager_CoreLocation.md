# `CLRacingRouteManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CLRacingRoute="fDistanceCalculator"{CLDistanceCalc="fM"d"fN"d"fRefLatRads"d"fRefLatDegs"d"fCosRefLat"d}"fSignalEnvironmentType"i"fWorkoutActivity"i"fRoutePoints"@"NSMutableArray""fRouteBoundingBox"{RouteBoundingBox="fMinLatitude_deg"d"fMaxLatitude_deg"d"fMinLongitude_deg"d"fMaxLongitude_deg"d"fRows"i"fColumns"i}"fRouteMatrixIndexVec"{vector<std::vector<std::pair<int, int>>, std::allocator<std::vector<std::pair<int, int>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}"fRaceStartPointOnCurrentRoute"{RacingRouteState="fLatitude_deg"d"fLongitude_deg"d"fAltitude_m"d"fOdometer_m"d"fTimestamp_s"d"fTimeSinceStartOfRace_s"d"fOffRouteTraveledTime_s"d"fDistanceSinceStartOfRace_m"d"fOffRouteTraveledDistance_m"d"fAveragePace_s_per_m"d"fDistanceAlongReferenceRoute_m"d}"fRaceStartPointOnReferenceRoute"{RacingRouteState="fLatitude_deg"d"fLongitude_deg"d"fAltitude_m"d"fOdometer_m"d"fTimestamp_s"d"fTimeSinceStartOfRace_s"d"fOffRouteTraveledTime_s"d"fDistanceSinceStartOfRace_m"d"fOffRouteTraveledDistance_m"d"fAveragePace_s_per_m"d"fDistanceAlongReferenceRoute_m"d}"fLastOnRouteDataPoint"{RacingRouteState="fLatitude_deg"d"fLongitude_deg"d"fAltitude_m"d"fOdometer_m"d"fTimestamp_s"d"fTimeSinceStartOfRace_s"d"fOffRouteTraveledTime_s"d"fDistanceSinceStartOfRace_m"d"fOffRouteTraveledDistance_m"d"fAveragePace_s_per_m"d"fDistanceAlongReferenceRoute_m"d}"fLastProjectedDataPoint"{RacingRouteState="fLatitude_deg"d"fLongitude_deg"d"fAltitude_m"d"fOdometer_m"d"fTimestamp_s"d"fTimeSinceStartOfRace_s"d"fOffRouteTraveledTime_s"d"fDistanceSinceStartOfRace_m"d"fOffRouteTraveledDistance_m"d"fAveragePace_s_per_m"d"fDistanceAlongReferenceRoute_m"d}"fRoutePointsArrayInitialized"B"fRecoveryMode"B"fRaceStartPointDetected"B"fRaceEndPointDetected"B"fUserIsOffRoute"B"fProjectedOnNearestPoint"B"fRaceSessionExpired"B"fRollingBufferReachedEndOfReferenceRoute"B"fRouteConfigurationSuccessful"B"fRacingRouteAnalyticsSent"B"fPrematureRaceEndDetected"B"fReferenceRouteTotalLengthDetermined"B"fLocationPointIsOutsideOfAcceptedRange"B"fLocationPointNotMatched"B"fRoutePointsBufferSize"i"fNumberOfRoutePointsToAdd"i"fOffRouteGraceDuration_s"i"fMatchedPointCounter"i"fReferenceRouteDataPointCounter"i"fCurrentRouteDataPointCounter"i"fOffRouteDataPointCounter"i"fInutileDataPointCounter"i"fRollingBufferUpdateCounter"i"fLastMatchedPointIndex"i"fLastMatchedPointIndexOnReferenceRoute"i"fRollingBufferStartIndexOnReferenceRoute"i"fMatrixCellIndexForLastMatchedPoint"i"fRaceStartLineProximityIndex"i"fReferenceRouteTotalLength_m"d"fTimestampOfLastMatchedPointOnReferenceRoute_s"d"fRegisteredTimeAtThresholdDistance_s"d"fEndOfRaceTimeThreshold_s"d"fNearestNeighborMaximumAcceptedDistance_m"d} clrr;
```

## Instance methods

```
-[CLRacingRouteManager reset];
-[CLRacingRouteManager addRoutePoints:];
-[CLRacingRouteManager advanceToPoint:];
-[CLRacingRouteManager configureWithWorkoutActivityType:bufferSize:offRouteGraceDurationInSec:];
-[CLRacingRouteManager getRaceParameters];
-[CLRacingRouteManager numberOfRoutePointsToAdd];
-[CLRacingRouteManager recoverRaceAtTimestamp];
-[CLRacingRouteManager setRaceParameters:];
```
