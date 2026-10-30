# `SBPhysicalButtonSceneOverrideManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAVSystemControllerCacheObserver`, `SBCameraViewfinderMonitorObserver`, `SBDisplayContentModeTransitionObserver`, `SBFZStackParticipantObserver`, `SBPhysicalButtonSceneOverrideObservationState`, `SBWindowSceneAttachmentObserving`
- 23 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _sendsPhysicalVolumeButtonActions;
B _sendsPhysicalLockButtonActions;
@"SBWindowScene" _mainWindowScene;
@"SBWindowScene" _windowScene;
@"SBFZStackResolver" _observedZStackResolver;
@"SBVolumeControl" _volumeControl;
@"SBAVSystemControllerCache" _avCache;
@"<SBCameraViewfinderMonitoring>" _cameraViewfinderMonitorToken;
@"NSArray" _lastPhysicalButtonSceneTargets;
@"NSArray" _lastScenesRequestingFullFidelityCaptureButtonEvents;
@"NSHashTable" _buttonActionCompletionHandlers;
@"BSCompoundAssertion" _observers;
@"SBPhysicalButtonBehaviorRequest" _volumeUpButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _volumeDownButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _headphoneLeftButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _headphoneRightButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _lockButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _actionButtonRequest;
@"SBPhysicalButtonBehaviorRequest" _cameraCaptureButtonRequest;
@"<SBFCaptureApplicationProviding>" _captureApplicationProvider;
@"SBSPhysicalButtonTargetMonitorServer" _physicalButtonTargetMonitorServer;
@"SBSceneManager" _sceneManager;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPhysicalButtonSceneOverrideManager cache:didUpdateAudioSessionPlaying:];
-[SBPhysicalButtonSceneOverrideManager _sendButtonDownForButtonType:request:scene:];
-[SBPhysicalButtonSceneOverrideManager zStackParticipantWithIdentifier:settingsDidChange:];
-[SBPhysicalButtonSceneOverrideManager _overrideWindowScene];
-[SBPhysicalButtonSceneOverrideManager _sceneForSceneTarget:];
-[SBPhysicalButtonSceneOverrideManager _processZStackParticipantSettings:];
-[SBPhysicalButtonSceneOverrideManager reasonCameraBehaviorSceneIsNotEligibleForSupplementalUI];
-[SBPhysicalButtonSceneOverrideManager cameraViewfinderMonitorSessionDidBegin:auditToken:];
-[SBPhysicalButtonSceneOverrideManager zStackParticipantWithIdentifier:wasAcquiredWithSettings:];
-[SBPhysicalButtonSceneOverrideManager windowSceneDidDisconnect:];
-[SBPhysicalButtonSceneOverrideManager _addButtonActionCompletionHandler:];
-[SBPhysicalButtonSceneOverrideManager _removeButtonActionCompletionHandler:];
-[SBPhysicalButtonSceneOverrideManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBPhysicalButtonSceneOverrideManager cameraViewfinderMonitorSessionDidEnd:auditToken:];
-[SBPhysicalButtonSceneOverrideManager _activeRequestForButton:];
-[SBPhysicalButtonSceneOverrideManager dealloc];
-[SBPhysicalButtonSceneOverrideManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBPhysicalButtonSceneOverrideManager cache:didUpdateActiveCategoryName:];
-[SBPhysicalButtonSceneOverrideManager _applicationBundleIdentifierForClientBundleIdentifier:];
-[SBPhysicalButtonSceneOverrideManager _canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:isAudioSessionPlaying:];
-[SBPhysicalButtonSceneOverrideManager _sendActionForButtonType:buttonState:request:];
-[SBPhysicalButtonSceneOverrideManager auditTokenForRequestingProcessOfCameraBehaviorScene];
-[SBPhysicalButtonSceneOverrideManager _sendsActionsForButtonType:];
-[SBPhysicalButtonSceneOverrideManager windowSceneDidConnect:];
-[SBPhysicalButtonSceneOverrideManager _canSendActionButtonEventsToScene:withConfiguration:];
-[SBPhysicalButtonSceneOverrideManager _configureForWindowScene:];
-[SBPhysicalButtonSceneOverrideManager cameraBehaviorScene];
-[SBPhysicalButtonSceneOverrideManager _notifyObserversSomethingDidChange];
-[SBPhysicalButtonSceneOverrideManager cameraViewfinderMonitorSessionWillBegin:auditToken:];
-[SBPhysicalButtonSceneOverrideManager _canSendCameraCaptureFullPressEventsToScene:withConfiguration:];
-[SBPhysicalButtonSceneOverrideManager _canSendCameraShutterButtonEventsForRequestAuditToken:];
```
