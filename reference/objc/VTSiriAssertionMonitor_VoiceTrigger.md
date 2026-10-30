# `VTSiriAssertionMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
C _assertionState;
```

## Class methods

```
+[VTSiriAssertionMonitor sharedInstance];
```

## Instance methods

```
-[VTSiriAssertionMonitor init];
-[VTSiriAssertionMonitor _stopMonitoring];
-[VTSiriAssertionMonitor dealloc];
-[VTSiriAssertionMonitor isEnabled];
-[VTSiriAssertionMonitor _startMonitoringWithQueue:];
-[VTSiriAssertionMonitor _notifyObserver:];
-[VTSiriAssertionMonitor disableAssertionReceived];
-[VTSiriAssertionMonitor enableAssertionReceived];
```
