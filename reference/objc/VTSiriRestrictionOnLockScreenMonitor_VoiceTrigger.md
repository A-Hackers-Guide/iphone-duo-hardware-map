# `VTSiriRestrictionOnLockScreenMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- Protocols: `MCProfileConnectionObserver`
- 1 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _isRestricted;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTSiriRestrictionOnLockScreenMonitor sharedInstance];
```

## Instance methods

```
-[VTSiriRestrictionOnLockScreenMonitor isRestricted];
-[VTSiriRestrictionOnLockScreenMonitor profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[VTSiriRestrictionOnLockScreenMonitor init];
-[VTSiriRestrictionOnLockScreenMonitor _stopMonitoring];
-[VTSiriRestrictionOnLockScreenMonitor _startMonitoringWithQueue:];
-[VTSiriRestrictionOnLockScreenMonitor _notifyObserver:withRestricted:];
-[VTSiriRestrictionOnLockScreenMonitor _checkSiriRestrictedOnLockScreen];
-[VTSiriRestrictionOnLockScreenMonitor _didReceiveRestrictionChanged:];
-[VTSiriRestrictionOnLockScreenMonitor _didReceiveRestrictionChangedInQueue:];
```
