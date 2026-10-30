# `LACUITouchIDSensorReachabilityMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUITouchIDSensorReachabilityMonitoring`
- 3 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _sensorOutOfReach;
@"CMDeviceStateManager" _deviceStateManager;
@? _sensorReachabilityDidChangeHandler;
```

## Properties

```
@property (T@?,C,N,V_sensorReachabilityDidChangeHandler) sensorReachabilityDidChangeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUITouchIDSensorReachabilityMonitor stop];
-[LACUITouchIDSensorReachabilityMonitor dealloc];
-[LACUITouchIDSensorReachabilityMonitor start];
-[LACUITouchIDSensorReachabilityMonitor _applyDeviceStateEvent:];
-[LACUITouchIDSensorReachabilityMonitor _sensorOutOfReachInDeviceStateEvent:];
-[LACUITouchIDSensorReachabilityMonitor isSensorOutOfReach];
-[LACUITouchIDSensorReachabilityMonitor sensorReachabilityDidChangeHandler];
-[LACUITouchIDSensorReachabilityMonitor setSensorReachabilityDidChangeHandler:];
```
