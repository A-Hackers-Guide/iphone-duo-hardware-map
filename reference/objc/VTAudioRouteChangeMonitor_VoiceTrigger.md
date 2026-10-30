# `VTAudioRouteChangeMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _hearstConnection;
```

## Class methods

```
+[VTAudioRouteChangeMonitor sharedInstance];
```

## Instance methods

```
-[VTAudioRouteChangeMonitor init];
-[VTAudioRouteChangeMonitor _stopMonitoring];
-[VTAudioRouteChangeMonitor _startMonitoringWithQueue:];
-[VTAudioRouteChangeMonitor _notifyObserver:];
-[VTAudioRouteChangeMonitor _isActiveRoute:];
-[VTAudioRouteChangeMonitor _CMSessionDispatchQueue];
-[VTAudioRouteChangeMonitor _hasDoAPSupport:];
-[VTAudioRouteChangeMonitor _hasInEarDetectSupport:];
-[VTAudioRouteChangeMonitor _updateHearstConnectionStatus];
-[VTAudioRouteChangeMonitor hearstConnectionStatus];
-[VTAudioRouteChangeMonitor updateExternalRouteConnectionStatus];
```
