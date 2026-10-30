# `SBLockScreenSessionAnalyticsEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 10 instance methods, 0 class methods

## Properties

```
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
-[SBLockScreenSessionAnalyticsEnvironment currentOrientation];
-[SBLockScreenSessionAnalyticsEnvironment currentDeviceOrientation];
-[SBLockScreenSessionAnalyticsEnvironment currentPose];
-[SBLockScreenSessionAnalyticsEnvironment currentMotionActivity];
-[SBLockScreenSessionAnalyticsEnvironment hasNotifications];
-[SBLockScreenSessionAnalyticsEnvironment isFaceDown];
-[SBLockScreenSessionAnalyticsEnvironment isInPocket];
-[SBLockScreenSessionAnalyticsEnvironment isPAUEnabled];
-[SBLockScreenSessionAnalyticsEnvironment notificationPreviewSetting];
-[SBLockScreenSessionAnalyticsEnvironment setMonitoringActive:];
```
