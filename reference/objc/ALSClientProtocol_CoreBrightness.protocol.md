# `ALSClientProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@?,C) addSensorsHandler;
@property (T@?,C) removeSensorHandler;
@property (T@?,C) handleSensorEvent;
@property (T@"<ALSClientExecutor>",&) executor;
```

## Instance methods

```
-[ALSClientProtocol executor];
-[ALSClientProtocol activateWithError:];
-[ALSClientProtocol cancel];
-[ALSClientProtocol setExecutor:];
-[ALSClientProtocol addSensorsHandler];
-[ALSClientProtocol handleSensorEvent];
-[ALSClientProtocol removeSensorHandler];
-[ALSClientProtocol setAddSensorsHandler:];
-[ALSClientProtocol setHandleSensorEvent:];
-[ALSClientProtocol setPreferredInterval:forSensor:error:];
-[ALSClientProtocol setRemoveSensorHandler:];
```
