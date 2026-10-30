# `_TtC20SpeakerGroupSetupKit16SGSAVCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpeakerGroupSetupKit.framework/SpeakerGroupSetupKit`](../userland/System__Library__PrivateFrameworks__SpeakerGroupSetupKit.framework__SpeakerGroupSetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
os.Logger logger;
SpeakerGroupSetupKit.SGSAVScheduler ? pendingScheduler;
SpeakerGroupSetupKit.SGSAVScheduler ? activeScheduler;
SpeakerGroupSetupKit.SGSAVSessionState ? sessionState;
Swift.AsyncStream.Continuation SpeakerGroupSetupKit.SGSAVScheduleEvent _$s_GSg -> avScheduleEvents;
_$sScCyyt Swift.Error ? startSessionContinuation;
_$sSayScCyyt Swift.Never stopSessionContinuations;
_$sScTyyt Swift.Never ? stopSessionTimeoutTask;
_$sScC -> SpeakerGroupSetupKit.SGSAVCalibrationResult Swift.Error ? calibrationContinuation;
_$sSayScCyyt Swift.Never stopSceneContinuations;
_$sScTyyt Swift.Never ? stopSceneTimeoutTask;
SpeakerGroupSetupKit.SGSAVSessionType ? sessionType;
SpeakerGroupSetupKit.SGSAVError _$scSg -> onError;
```

## Instance methods

```
-[_TtC20SpeakerGroupSetupKit16SGSAVCoordinator init];
```
