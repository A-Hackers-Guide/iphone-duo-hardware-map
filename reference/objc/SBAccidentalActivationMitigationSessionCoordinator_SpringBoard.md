# `SBAccidentalActivationMitigationSessionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAccidentalActivationMitigationSessionObserver`, `SBSAccidentalActivationMitigationSessionServiceServerDelegate`, `SBAccidentalActivationMitigationHostSessionDelegate`, `SBBacklightControllerObserver`, `SBIdleTimerProviding`
- 5 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"SBSAccidentalActivationMitigationSessionServiceServer" _server;
@"SBCaptureButtonSuppressionManager" _suppressionManager;
@"NSHashTable" _observers;
@"SBAccidentalActivationMitigationHostSession" _lock_host_session;
```

## Properties

```
@property (T@"SBAccidentalActivationMitigationHostSession",&,N,V_lock_host_session) hostSession;
@property (T@"<SBSAccidentalActivationMitigationSession>",R,N) currentSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBAccidentalActivationMitigationSessionCoordinator backlightController:willTransitionToBacklightState:source:];
-[SBAccidentalActivationMitigationSessionCoordinator removeObserver:];
-[SBAccidentalActivationMitigationSessionCoordinator addObserver:];
-[SBAccidentalActivationMitigationSessionCoordinator hasIdleTimerBehaviors];
-[SBAccidentalActivationMitigationSessionCoordinator currentSession];
-[SBAccidentalActivationMitigationSessionCoordinator coordinatorRequestedIdleTimerBehavior:];
-[SBAccidentalActivationMitigationSessionCoordinator accidentalActivationMitigationSessionStateDidChange:];
-[SBAccidentalActivationMitigationSessionCoordinator serverDidRequestCreateHostSessionUponConnection:];
-[SBAccidentalActivationMitigationSessionCoordinator serverDidRequestDestroyNonActiveHostSessionUponDisconnection:];
-[SBAccidentalActivationMitigationSessionCoordinator setHostSession:];
-[SBAccidentalActivationMitigationSessionCoordinator _publishDidCancelMitigationSession:];
-[SBAccidentalActivationMitigationSessionCoordinator _publishDidMitigateMitigationSession:];
-[SBAccidentalActivationMitigationSessionCoordinator _publishDidStartMitigationSession:];
-[SBAccidentalActivationMitigationSessionCoordinator _targetWindowSceneForMitigationSession:];
-[SBAccidentalActivationMitigationSessionCoordinator hostSession];
-[SBAccidentalActivationMitigationSessionCoordinator hostSessionDidRequestCancelMitigation:];
-[SBAccidentalActivationMitigationSessionCoordinator hostSessionDidRequestMitigateAccidentalActivation:];
-[SBAccidentalActivationMitigationSessionCoordinator hostSessionDidRequestStartMitigation:outIdleTimer:];
-[SBAccidentalActivationMitigationSessionCoordinator initWithSuppressionManager:];
```
