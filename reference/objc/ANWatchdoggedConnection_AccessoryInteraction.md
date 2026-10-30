# `ANWatchdoggedConnection`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CBPeripheral" _peripheral;
d _startTime;
q _latency;
@"NSString" _accessoryTypeName;
```

## Properties

```
@property (T@"CBPeripheral",&,V_peripheral) peripheral;
@property (Td,N,V_startTime) startTime;
@property (Tq,V_latency) latency;
@property (T@"NSString",R,V_accessoryTypeName) accessoryTypeName;
```

## Instance methods

```
-[ANWatchdoggedConnection setLatency:];
-[ANWatchdoggedConnection latency];
-[ANWatchdoggedConnection init];
-[ANWatchdoggedConnection startTime];
-[ANWatchdoggedConnection dealloc];
-[ANWatchdoggedConnection setStartTime:];
-[ANWatchdoggedConnection peripheral];
-[ANWatchdoggedConnection setPeripheral:];
-[ANWatchdoggedConnection accessoryTypeName];
-[ANWatchdoggedConnection computeTimeConnected];
-[ANWatchdoggedConnection initWithPeripheral:latency:accessoryTypeName:];
```
