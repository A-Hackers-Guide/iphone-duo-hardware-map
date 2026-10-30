# `LACDTOLostModeController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLostModeFetchService`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOLostModeProvider>" _lostModeProvider;
@"<LACDTOKVStore>" _store;
@"<LACDTOTelemetryReporting>" _telemetry;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"LACBackgroundTask" _lostModeBackgroundTask;
```

## Properties

```
@property (T@"LACBackgroundTask",&,N,V_lostModeBackgroundTask) lostModeBackgroundTask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOLostModeController description];
-[LACDTOLostModeController _storeLostModeState:completion:];
-[LACDTOLostModeController _lostModeStateFromBackgroundTaskResult:];
-[LACDTOLostModeController _runLostModeBackgroundTaskWithStrategy:completion:];
-[LACDTOLostModeController _runLostModeBackgroundTaskWithTimeout:completion:];
-[LACDTOLostModeController fetchLostMode:completion:];
-[LACDTOLostModeController initWithLostModeProvider:store:telemetry:workQueue:];
-[LACDTOLostModeController lostModeBackgroundTask];
-[LACDTOLostModeController setLostModeBackgroundTask:];
```
