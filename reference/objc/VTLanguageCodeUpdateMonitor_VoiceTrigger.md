# `VTLanguageCodeUpdateMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
```

## Class methods

```
+[VTLanguageCodeUpdateMonitor sharedInstance];
```

## Instance methods

```
-[VTLanguageCodeUpdateMonitor init];
-[VTLanguageCodeUpdateMonitor _stopMonitoring];
-[VTLanguageCodeUpdateMonitor _startMonitoringWithQueue:];
-[VTLanguageCodeUpdateMonitor _didReceiveLanguageCodeUpdate];
-[VTLanguageCodeUpdateMonitor _notifyObserver:withLanguageCode:];
```
