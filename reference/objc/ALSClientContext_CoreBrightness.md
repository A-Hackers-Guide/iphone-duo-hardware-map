# `ALSClientContext`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ALSClientProtocol`
- 10 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
queue;
logHandle;
sensorContexts;
? addSensorsHandler;
? removeSensorHandler;
? handleSensorEvent;
storedExecutor;
? clientName;
Q state;
? observer;
```

## Properties

```
@property (T@?,N,C) addSensorsHandler;
@property (T@?,N,C) removeSensorHandler;
@property (T@?,N,C) handleSensorEvent;
@property (T@"<ALSClientExecutor>",N,&) executor;
@property (T@"NSString",N,R) clientName;
@property (TQ,N,Vstate) state;
@property (T@"<ALSClientObserver>",N,W,Vobserver) observer;
```

## Instance methods

```
-[ALSClientContext executor];
-[ALSClientContext handleEvent:];
-[ALSClientContext observer];
-[ALSClientContext setState:];
-[ALSClientContext init];
-[ALSClientContext activateWithError:];
-[ALSClientContext clientName];
-[ALSClientContext setObserver:];
-[ALSClientContext cancel];
-[ALSClientContext state];
-[ALSClientContext setExecutor:];
-[ALSClientContext addSensors:];
-[ALSClientContext addSensorsHandler];
-[ALSClientContext handleSensorEvent];
-[ALSClientContext initWithClientName:queue:];
-[ALSClientContext removeSensor:];
-[ALSClientContext removeSensorHandler];
-[ALSClientContext setAddSensorsHandler:];
-[ALSClientContext setHandleSensorEvent:];
-[ALSClientContext setPreferredInterval:forSensor:error:];
-[ALSClientContext setRemoveSensorHandler:];
-[ALSClientContext statusInfo];
```
