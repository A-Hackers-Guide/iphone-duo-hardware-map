# `CMPedometerProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 30 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fAppQueue;
^v fLocationdConnection;
@? fOffsetUpdateHandler;
@? fCumulativeUpdateHandler;
q fStepCountFromStart;
q fPushCountFromStart;
q fStepCountOffset;
q fPushCountOffset;
d fDistanceFromStart;
d fDistanceOffset;
i fFloorAscendedStart;
i fFloorAscendedOffset;
i fFloorDescendedStart;
i fFloorDescendedOffset;
d fActiveTimeFromStart;
d fActiveTimeOffset;
d fValidStartDate;
B fStopUpdates;
B fFloorCountingAvailable;
B fPaceAndCadenceAvailable;
@? fEventHandler;
B fStopEventUpdates;
i fWorkoutType;
i fElevationAscendedStart;
i fElevationAscendedOffset;
i fElevationDescendedStart;
i fElevationDescendedOffset;
B fElevationCountingAvailable;
i fDistanceSource;
```

## Instance methods

```
-[CMPedometerProxy init];
-[CMPedometerProxy dealloc];
-[CMPedometerProxy _handleQueryResponse:onQueue:withHandler:];
-[CMPedometerProxy _teardown];
-[CMPedometerProxy _internalQueryPedometerDataFromDate:toDate:onQueue:withHandler:];
-[CMPedometerProxy _handleRecordQueryResponse:withHandler:shouldStartUpdates:];
-[CMPedometerProxy _queryPedometerCalibrationBinsWithHandler:forType:forRemote:];
-[CMPedometerProxy _queryPedometerDataFromDate:toDate:withHandler:];
-[CMPedometerProxy _queryPedometerDataSinceDataRecord:withHandler:shouldStartUpdates:];
-[CMPedometerProxy _startPedometerEventUpdatesWithHandler:];
-[CMPedometerProxy _startPedometerUpdatesFromDate:withHandler:];
-[CMPedometerProxy _startPedometerUpdatesSinceDataRecord:withHandler:];
-[CMPedometerProxy _stopPedometerEventUpdates];
-[CMPedometerProxy _stopPedometerUpdates];
-[CMPedometerProxy _strideCalibrationDump];
-[CMPedometerProxy _subscribeToCumulativePedometerUpdates:];
```
