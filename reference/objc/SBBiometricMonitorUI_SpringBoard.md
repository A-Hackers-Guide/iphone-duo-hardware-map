# `SBBiometricMonitorUI`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBiometricMonitorObserver`
- 7 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _enabled;
@"UIWindow" _debugWindow;
@"SBBiometricMonitorViewController" _debugViewController;
B _deferredMatchUpdatePending;
B _deferredPresenceDetectUpdatePending;
@"<SBBiometricMonitorDataSource>" _dataSource;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"<SBBiometricMonitorDataSource>",&,N,V_dataSource) dataSource;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBiometricMonitorUI enable];
-[SBBiometricMonitorUI setWindowScene:];
-[SBBiometricMonitorUI init];
-[SBBiometricMonitorUI setDataSource:];
-[SBBiometricMonitorUI disable];
-[SBBiometricMonitorUI dataSource];
-[SBBiometricMonitorUI windowScene];
-[SBBiometricMonitorUI _cancelDeferredUpdateMatchState];
-[SBBiometricMonitorUI _doDeferredPresenceDetectUpdate];
-[SBBiometricMonitorUI _cancelDeferredUpdatePresenceDetectState];
-[SBBiometricMonitorUI _deferredUpdateMatchState];
-[SBBiometricMonitorUI _deferredUpdatePresenceDetectState];
-[SBBiometricMonitorUI _doDeferredMatchStateUpdate];
-[SBBiometricMonitorUI _isDeferredMatchStateUpdatePending];
-[SBBiometricMonitorUI _isDeferredPresenceDetectStateUpdatePending];
-[SBBiometricMonitorUI _updateMatchState];
-[SBBiometricMonitorUI _updatePresenceDetectState];
-[SBBiometricMonitorUI biometricMonitorDataSourceMatchingEnded:];
-[SBBiometricMonitorUI biometricMonitorDataSourceMatchingFailed:];
-[SBBiometricMonitorUI biometricMonitorDataSourceMatchingStarted:];
-[SBBiometricMonitorUI biometricMonitorDataSourceMatchingSucceeded:];
-[SBBiometricMonitorUI biometricMonitorDataSourcePoseUpdated:];
-[SBBiometricMonitorUI biometricMonitorDataSourcePresenceDetectionEnded:];
-[SBBiometricMonitorUI biometricMonitorDataSourcePresenceDetectionFailed:];
-[SBBiometricMonitorUI biometricMonitorDataSourcePresenceDetectionStarted:];
-[SBBiometricMonitorUI biometricMonitorDataSourcePresenceDetectionSucceeded:];
```
