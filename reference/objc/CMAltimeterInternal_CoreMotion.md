# `CMAltimeterInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 21 instance methods, 2 class methods

## Instance variables

```
^{Dispatcher=^^?@} fFilteredPressureDispatcher;
@? fRelativeAltimeterHandler;
@"NSOperationQueue" fRelativeAltimeterQueue;
{Sample="timestamp"d"pressureData"{?="pressure"f"temperature"f}} fBaseAltimeterSample;
f fBarometricBaseAltitude;
B fBaselineReceived;
f fMostRecentFilteredPressure;
{deque<float, std::allocator<float>>="__map_"{__split_buffer<float *, std::allocator<float *>>="__first_"^^f"__begin_"^^f"__end_"^^f""{?="__cap_"^^f}}"__start_"Q""{?="__size_"Q}} fPressureSamples;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fAppQueue;
^v fLocationdConnection;
@? fHandler;
@? fSignificantElevationSampleHandler;
d fElevationAscendedOffset;
d fElevationDescendedOffset;
B fStopSignificantElevationUpdates;
d fFilteredElevationOffset;
B fStopRelativeAltitudeUpdates;
@"NSOperationQueue" fAbsoluteAltitudeClientQueue;
@? fAbsoluteAltitudeClientHandler;
@"NSOperationQueue" fCompanionRelativeElevationClientQueue;
@? fCompanionRelativeElevationClientHandler;
```

## Class methods

```
+[CMAltimeterInternal _bundleBeforeTCCCheck];
+[CMAltimeterInternal _bundleBeforeTCCCheck:];
```

## Instance methods

```
-[CMAltimeterInternal init];
-[CMAltimeterInternal dealloc];
-[CMAltimeterInternal _teardown];
-[CMAltimeterInternal _handleAbsoluteAltitudeUpdate:];
-[CMAltimeterInternal _handleCompanionRelativeElevationUpdate:];
-[CMAltimeterInternal _pauseAbsoluteAltitudeUpdates];
-[CMAltimeterInternal _queryElevationProfileFromDate:toDate:withBatchSize:fromRecordId:withHandler:];
-[CMAltimeterInternal _queryElevationProfileFromDate:toDate:withBatchSize:withHandler:];
-[CMAltimeterInternal _querySignificantElevationChangeFromDate:toDate:withHandler:];
-[CMAltimeterInternal _releaseHandlerObjects];
-[CMAltimeterInternal _resumeAbsoluteAltitudeUpdates];
-[CMAltimeterInternal _startAbsoluteAltitudeUpdatesToQueue:withHandler:];
-[CMAltimeterInternal _startCompanionRelativeElevationUpdatesToQueue:withHandler:];
-[CMAltimeterInternal _startElevationUpdatesWithHandler:];
-[CMAltimeterInternal _startRelativeAltitudeUpdates];
-[CMAltimeterInternal _startSignificantElevationUpdatesWithHandler:];
-[CMAltimeterInternal _stopAbsoluteAltitudeUpdates];
-[CMAltimeterInternal _stopCompanionRelativeElevationUpdates];
-[CMAltimeterInternal _stopElevationUpdates];
-[CMAltimeterInternal _stopRelativeAltitudeUpdates];
-[CMAltimeterInternal _stopSignificantElevationUpdates];
```
