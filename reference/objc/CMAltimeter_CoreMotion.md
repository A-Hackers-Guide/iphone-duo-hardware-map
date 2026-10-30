# `CMAltimeter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 19 instance methods, 7 class methods

## Instance variables

```
@ _internal;
```

## Class methods

```
+[CMAltimeter authorizationStatus];
+[CMAltimeter initialize];
+[CMAltimeter isSignificantElevationAvailable];
+[CMAltimeter dummySelector:];
+[CMAltimeter isAbsoluteAltitudeAvailable];
+[CMAltimeter isCompanionRelativeElevationAvailable];
+[CMAltimeter isRelativeAltitudeAvailable];
```

## Instance methods

```
-[CMAltimeter init];
-[CMAltimeter initPrivate];
-[CMAltimeter dealloc];
-[CMAltimeter deallocPrivate];
-[CMAltimeter queryElevationProfileFromDate:toDate:withBatchSize:withHandler:];
-[CMAltimeter stopSignificantElevationUpdates];
-[CMAltimeter onFilteredPressure:];
-[CMAltimeter pauseAbsoluteAltitudeUpdates];
-[CMAltimeter querySignificantElevationChangeFromDate:toDate:withHandler:];
-[CMAltimeter resumeAbsoluteAltitudeUpdates];
-[CMAltimeter startAbsoluteAltitudeUpdatesToQueue:withHandler:];
-[CMAltimeter startCompanionRelativeElevationUpdatesToQueue:withHandler:];
-[CMAltimeter startRelativeAltitudeUpdatesPrivateToQueue:withHandler:];
-[CMAltimeter startRelativeAltitudeUpdatesToQueue:withHandler:];
-[CMAltimeter startSignificantElevationUpdatesWithHandler:];
-[CMAltimeter stopAbsoluteAltitudeUpdates];
-[CMAltimeter stopCompanionRelativeElevationUpdates];
-[CMAltimeter stopRelativeAltitudeUpdates];
-[CMAltimeter stopRelativeAltitudeUpdatesPrivate];
```
