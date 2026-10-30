# `VTEventMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[VTEventMonitor removeObserver:];
-[VTEventMonitor init];
-[VTEventMonitor _stopMonitoring];
-[VTEventMonitor dealloc];
-[VTEventMonitor addObserver:];
-[VTEventMonitor _startMonitoringWithQueue:];
-[VTEventMonitor notifyObserver:];
-[VTEventMonitor enumerateObservers:];
-[VTEventMonitor enumerateObserversInQueue:];
```
