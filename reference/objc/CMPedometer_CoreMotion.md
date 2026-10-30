# `CMPedometer`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 19 instance methods, 8 class methods

## Instance variables

```
@"CMPedometerProxy" _pedometerProxy;
```

## Properties

```
@property (T@"CMPedometerProxy",R,N,V_pedometerProxy) pedometerProxy;
```

## Class methods

```
+[CMPedometer authorizationStatus];
+[CMPedometer isPaceAvailable];
+[CMPedometer isAllDayElevationAvailable];
+[CMPedometer isCadenceAvailable];
+[CMPedometer isDistanceAvailable];
+[CMPedometer isFloorCountingAvailable];
+[CMPedometer isPedometerEventTrackingAvailable];
+[CMPedometer isStepCountingAvailable];
```

## Instance methods

```
-[CMPedometer init];
-[CMPedometer dealloc];
-[CMPedometer _pedometerDataWithRecordID:];
-[CMPedometer _queryPedometerDataSinceDataRecord:withHandler:];
-[CMPedometer _startPedometerUpdatesSinceDataRecord:withHandler:];
-[CMPedometer pedometerProxy];
-[CMPedometer queryPedometerDataFromDate:toDate:withHandler:];
-[CMPedometer queryPedometerDataSinceDataRecord:withHandler:];
-[CMPedometer queryPedometerDataSinceRecord:withHandler:];
-[CMPedometer queryRawSpeedToKValueBinsWithHandler:];
-[CMPedometer queryRemoteRawSpeedToKValueBinsWithHandler:];
-[CMPedometer queryRemoteStepCadenceToStrideLengthBinsWithHandler:];
-[CMPedometer queryStepCadenceToStrideLengthBinsWithHandler:];
-[CMPedometer sendStrideCalibrationHistoryToFile:];
-[CMPedometer startPedometerEventUpdatesWithHandler:];
-[CMPedometer startPedometerUpdatesFromDate:withHandler:];
-[CMPedometer stopPedometerEventUpdates];
-[CMPedometer stopPedometerUpdates];
-[CMPedometer strideCalibrationDump];
```
