# `CMNatalimeter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 11 class methods

## Instance variables

```
@"CMNatalimeterInternal" _internal;
```

## Properties

```
@property (T@"CMNatalimeterInternal",R,N,V_internal) _internal;
```

## Class methods

```
+[CMNatalimeter userProfile];
+[CMNatalimeter computeRestingCaloriesAtRate:user:duration:];
+[CMNatalimeter activeMetsThreshold];
+[CMNatalimeter briskMinuteMetsThreshold];
+[CMNatalimeter computeTimeToActiveCalories:user:workoutType:];
+[CMNatalimeter defaultUserProfile];
+[CMNatalimeter isNatalimeterAvailable];
+[CMNatalimeter maxNatalieEntries];
+[CMNatalimeter resetCalibrationDataWithError:];
+[CMNatalimeter setUserInfo:error:];
+[CMNatalimeter setUserProfile:error:];
```

## Instance methods

```
-[CMNatalimeter _internal];
-[CMNatalimeter init];
-[CMNatalimeter dealloc];
-[CMNatalimeter queryAbsoluteNatalimetryDataSinceDataRecord:withHandler:];
-[CMNatalimeter queryAbsoluteNatalimetryDataSinceRecord:withHandler:];
-[CMNatalimeter startAbsoluteNatalimetryDataUpdatesWithHandler:];
-[CMNatalimeter stopAbsoluteNatalimetryDataUpdates];
```
