# `VTSiriEnabledMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
B _isSiriEnabled;
```

## Class methods

```
+[VTSiriEnabledMonitor sharedInstance];
```

## Instance methods

```
-[VTSiriEnabledMonitor init];
-[VTSiriEnabledMonitor _stopMonitoring];
-[VTSiriEnabledMonitor isEnabled];
-[VTSiriEnabledMonitor _startMonitoringWithQueue:];
-[VTSiriEnabledMonitor _didReceiveSiriSettingChanged:];
-[VTSiriEnabledMonitor _notifyObserver:withEnabled:];
```
