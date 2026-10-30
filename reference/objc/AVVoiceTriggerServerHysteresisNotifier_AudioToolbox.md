# `AVVoiceTriggerServerHysteresisNotifier`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _portsToMonitor;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableArray",&,N,V_portsToMonitor) portsToMonitor;
```

## Instance methods

```
-[AVVoiceTriggerServerHysteresisNotifier initWithSerialQueue:];
-[AVVoiceTriggerServerHysteresisNotifier dealloc];
-[AVVoiceTriggerServerHysteresisNotifier queue];
-[AVVoiceTriggerServerHysteresisNotifier stateChanged:];
-[AVVoiceTriggerServerHysteresisNotifier setQueue:];
-[AVVoiceTriggerServerHysteresisNotifier addPortToMonitor:hysteresisDurationSeconds:notificationBlock:];
-[AVVoiceTriggerServerHysteresisNotifier getPortManagerForType:];
-[AVVoiceTriggerServerHysteresisNotifier isPortActive:activePortsToken:];
-[AVVoiceTriggerServerHysteresisNotifier portsToMonitor];
-[AVVoiceTriggerServerHysteresisNotifier processState:];
-[AVVoiceTriggerServerHysteresisNotifier removePortToMonitor:];
-[AVVoiceTriggerServerHysteresisNotifier sendState:];
-[AVVoiceTriggerServerHysteresisNotifier setPortsToMonitor:];
-[AVVoiceTriggerServerHysteresisNotifier stateChanged:forPort:];
```
