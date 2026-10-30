# `ULBluetoothMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 2 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _powerOn;
@"CBController" _controller;
```

## Properties

```
@property (T@"CBController",&,N,V_controller) controller;
@property (TB,N,V_powerOn) powerOn;
```

## Instance methods

```
-[ULBluetoothMonitor stopMonitoring:];
-[ULBluetoothMonitor powerOn];
-[ULBluetoothMonitor controller];
-[ULBluetoothMonitor setController:];
-[ULBluetoothMonitor latestEventAfterAddingObserverForEventName:];
-[ULBluetoothMonitor startMonitoring:];
-[ULBluetoothMonitor _checkPowerOnForBluetoothState:];
-[ULBluetoothMonitor _bluetoothStateChangeHandler];
-[ULBluetoothMonitor _invalidationHandler];
-[ULBluetoothMonitor setPowerOn:];
```
