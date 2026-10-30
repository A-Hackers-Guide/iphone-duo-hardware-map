# `PLSensorAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `CMPocketStateDelegate`
- 9 instance variables, 13 properties, 32 instance methods, 9 class methods

## Instance variables

```
B _firstProximityEvent;
@"PLTimer" _proximityTimer;
@"PLStateTrackingComposition" _stateTracker;
@"BrightnessSystemClient" _brightnessSystemClient;
@"NSOperationQueue" _operationQueue;
@"CMPocketStateManager" _pocketStateManager;
@"CMMotionActivityManager" _motionActivityManager;
@"CMDeviceOrientationManager" _deviceOrientationManager;
^{__IOHIDEventSystemClient=} _proximityHIDClient;
```

## Properties

```
@property (TB,V_firstProximityEvent) firstProximityEvent;
@property (T@"PLTimer",&,V_proximityTimer) proximityTimer;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
@property (T@"BrightnessSystemClient",&,V_brightnessSystemClient) brightnessSystemClient;
@property (T@"NSOperationQueue",&,V_operationQueue) operationQueue;
@property (T@"CMPocketStateManager",&,V_pocketStateManager) pocketStateManager;
@property (T@"CMMotionActivityManager",&,V_motionActivityManager) motionActivityManager;
@property (T@"CMDeviceOrientationManager",&,V_deviceOrientationManager) deviceOrientationManager;
@property (T^{__IOHIDEventSystemClient=},V_proximityHIDClient) proximityHIDClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLSensorAgent entryEventPointDefinitions];
+[PLSensorAgent load];
+[PLSensorAgent isEnabled];
+[PLSensorAgent entryEventPointDefinitionALS];
+[PLSensorAgent entryEventPointDefinitionActivity];
+[PLSensorAgent entryEventPointDefinitionOrientation];
+[PLSensorAgent entryEventPointDefinitionPocketState];
+[PLSensorAgent entryEventPointDefinitionProximity];
+[PLSensorAgent shouldLogRearLux];
```

## Instance methods

```
-[PLSensorAgent setMotionActivityManager:];
-[PLSensorAgent motionActivityManager];
-[PLSensorAgent init];
-[PLSensorAgent stateTracker];
-[PLSensorAgent initOperatorDependancies];
-[PLSensorAgent pocketStateManager:didUpdateState:];
-[PLSensorAgent setStateTracker:];
-[PLSensorAgent initTaskOperatorDependancies];
-[PLSensorAgent log];
-[PLSensorAgent operationQueue];
-[PLSensorAgent setOperationQueue:];
-[PLSensorAgent deviceOrientationManager];
-[PLSensorAgent setDeviceOrientationManager:];
-[PLSensorAgent pocketStateManager];
-[PLSensorAgent setPocketStateManager:];
-[PLSensorAgent brightnessSystemClient];
-[PLSensorAgent handleBrightnessClientNotification:withValue:];
-[PLSensorAgent setBrightnessSystemClient:];
-[PLSensorAgent logEventPointDeviceOrientation:];
-[PLSensorAgent firstProximityEvent];
-[PLSensorAgent handleMotionActivityManagerNotification:];
-[PLSensorAgent handleOrientationManagerNotification:];
-[PLSensorAgent handlePocketStateManagerNotification:];
-[PLSensorAgent logEventPointALS:];
-[PLSensorAgent logEventPointActivity:];
-[PLSensorAgent logEventPointPocketState:];
-[PLSensorAgent logEventPointProximity:];
-[PLSensorAgent proximityHIDClient];
-[PLSensorAgent proximityTimer];
-[PLSensorAgent setFirstProximityEvent:];
-[PLSensorAgent setProximityHIDClient:];
-[PLSensorAgent setProximityTimer:];
```
