# `CMBatchedSensorManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"CMBatchedSensorManagerInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisAccelerometerActive) accelerometerActive;
@property (Tq,R,N) accelerometerDataFrequency;
@property (T@"NSArray",R) accelerometerBatch;
@property (Tq,R,N) deviceMotionDataFrequency;
@property (TB,R,N,GisDeviceMotionActive) deviceMotionActive;
@property (T@"NSArray",R) deviceMotionBatch;
```

## Class methods

```
+[CMBatchedSensorManager authorizationStatus];
+[CMBatchedSensorManager isAccelerometerSupported];
+[CMBatchedSensorManager isDeviceMotionSupported];
```

## Instance methods

```
-[CMBatchedSensorManager isAccelerometerActive];
-[CMBatchedSensorManager init];
-[CMBatchedSensorManager stopDeviceMotionUpdates];
-[CMBatchedSensorManager dealloc];
-[CMBatchedSensorManager stopAccelerometerUpdates];
-[CMBatchedSensorManager startDeviceMotionUpdates];
-[CMBatchedSensorManager isDeviceMotionActive];
-[CMBatchedSensorManager startAccelerometerUpdates];
-[CMBatchedSensorManager accelerometerBatch];
-[CMBatchedSensorManager accelerometerDataFrequency];
-[CMBatchedSensorManager deviceMotionBatch];
-[CMBatchedSensorManager deviceMotionDataFrequency];
-[CMBatchedSensorManager startAccelerometerUpdatesWithHandler:];
-[CMBatchedSensorManager startDeviceMotionUpdatesWithHandler:];
```
