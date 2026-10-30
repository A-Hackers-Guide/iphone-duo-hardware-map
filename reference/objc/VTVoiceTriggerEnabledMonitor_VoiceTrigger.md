# `VTVoiceTriggerEnabledMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
B _isVoiceTriggerEnabled;
```

## Class methods

```
+[VTVoiceTriggerEnabledMonitor sharedInstance];
```

## Instance methods

```
-[VTVoiceTriggerEnabledMonitor init];
-[VTVoiceTriggerEnabledMonitor _stopMonitoring];
-[VTVoiceTriggerEnabledMonitor isEnabled];
-[VTVoiceTriggerEnabledMonitor _startMonitoringWithQueue:];
-[VTVoiceTriggerEnabledMonitor _checkVoiceTriggerEnabled];
-[VTVoiceTriggerEnabledMonitor _didReceiveVoiceTriggerSettingChanged:];
-[VTVoiceTriggerEnabledMonitor _didReceiveVoiceTriggerSettingChangedInQueue:];
-[VTVoiceTriggerEnabledMonitor _notifyObserver:withEnabled:];
```
