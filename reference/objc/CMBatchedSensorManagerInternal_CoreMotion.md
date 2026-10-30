# `CMBatchedSensorManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 2 properties, 14 instance methods, 3 class methods

## Instance variables

```
^v _connection;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _dataQueue;
B _available;
@? _accelHandler;
B _accelActive;
@? _deviceMotionHandler;
B _deviceMotionActive;
@"NSArray" _accelBatch;
@"NSArray" _deviceMotionBatch;
```

## Properties

```
@property (T@"NSArray",&,V_accelBatch) accelBatch;
@property (T@"NSArray",&,V_deviceMotionBatch) deviceMotionBatch;
```

## Class methods

```
+[CMBatchedSensorManagerInternal _newArrayByUnpackingAccelerometerBatch:];
+[CMBatchedSensorManagerInternal _newArrayByUnpackingDeviceMotionBatch:];
+[CMBatchedSensorManagerInternal areBatchedSensorsSupported];
```

## Instance methods

```
-[CMBatchedSensorManagerInternal _connect];
-[CMBatchedSensorManagerInternal init];
-[CMBatchedSensorManagerInternal dealloc];
-[CMBatchedSensorManagerInternal _teardown];
-[CMBatchedSensorManagerInternal _startAccelerometerUpdates];
-[CMBatchedSensorManagerInternal _startAccelerometerUpdatesWithHandler:];
-[CMBatchedSensorManagerInternal _startDeviceMotionUpdates];
-[CMBatchedSensorManagerInternal _startDeviceMotionUpdatesWithHandler:];
-[CMBatchedSensorManagerInternal _stopAccelerometerUpdates];
-[CMBatchedSensorManagerInternal _stopDeviceMotionUpdates];
-[CMBatchedSensorManagerInternal accelBatch];
-[CMBatchedSensorManagerInternal deviceMotionBatch];
-[CMBatchedSensorManagerInternal setAccelBatch:];
-[CMBatchedSensorManagerInternal setDeviceMotionBatch:];
```
