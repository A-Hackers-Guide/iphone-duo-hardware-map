# `SBLockScreenSessionAnalyticsDeviceEnvironment`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BBObserverDelegate`, `SBLockScreenSessionAnalyticsEnvironment`
- 8 instance variables, 13 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBPocketStateMonitor" _pocketStateMonitor;
@"CMMotionActivityManager" _motionActivityManager;
@"BBObserver" _bulletinObserver;
@"BBSettingsGateway" _settingsGateway;
q _currentMotionActivity;
q _notificationPreviewSetting;
B _monitoringActive;
B _receivingActivityUpdates;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) currentPose;
@property (Tq,R,N) currentOrientation;
@property (TB,R,N) hasNotifications;
@property (TB,R,N,GisPAUEnabled) pauEnabled;
@property (Tq,R,N) notificationPreviewSetting;
@property (TB,R,N,GisInPocket) inPocket;
@property (TB,R,N,GisFaceDown) faceDown;
@property (Tq,R,N) currentMotionActivity;
@property (Tq,R,N) currentDeviceOrientation;
```

## Instance methods

```
-[SBLockScreenSessionAnalyticsDeviceEnvironment currentOrientation];
-[SBLockScreenSessionAnalyticsDeviceEnvironment observer:updateGlobalSettings:];
-[SBLockScreenSessionAnalyticsDeviceEnvironment init];
-[SBLockScreenSessionAnalyticsDeviceEnvironment dealloc];
-[SBLockScreenSessionAnalyticsDeviceEnvironment currentDeviceOrientation];
-[SBLockScreenSessionAnalyticsDeviceEnvironment currentPose];
-[SBLockScreenSessionAnalyticsDeviceEnvironment _primaryWindowScene];
-[SBLockScreenSessionAnalyticsDeviceEnvironment _stopActivityUpdates];
-[SBLockScreenSessionAnalyticsDeviceEnvironment _updateContentPreviewSetting:];
-[SBLockScreenSessionAnalyticsDeviceEnvironment _updateMotionActivity:];
-[SBLockScreenSessionAnalyticsDeviceEnvironment currentMotionActivity];
-[SBLockScreenSessionAnalyticsDeviceEnvironment hasNotifications];
-[SBLockScreenSessionAnalyticsDeviceEnvironment initWithPocketStateMonitor:motionActivityManager:bulletinObserver:settingsGateway:];
-[SBLockScreenSessionAnalyticsDeviceEnvironment isFaceDown];
-[SBLockScreenSessionAnalyticsDeviceEnvironment isInPocket];
-[SBLockScreenSessionAnalyticsDeviceEnvironment isPAUEnabled];
-[SBLockScreenSessionAnalyticsDeviceEnvironment notificationPreviewSetting];
-[SBLockScreenSessionAnalyticsDeviceEnvironment setMonitoringActive:];
```
