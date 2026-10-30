# `VTAssetMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
```

## Class methods

```
+[VTAssetMonitor sharedInstance];
```

## Instance methods

```
-[VTAssetMonitor init];
-[VTAssetMonitor _stopMonitoring];
-[VTAssetMonitor _startMonitoringWithQueue:];
-[VTAssetMonitor _notifyObserver:];
-[VTAssetMonitor _didReceiveNewAssetAvailable];
-[VTAssetMonitor notifyNewAssetDownloaded];
```
