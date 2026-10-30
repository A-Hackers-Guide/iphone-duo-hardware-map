# `SBContinuitySession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `SBAppResizingCoordinatorObserver`, `SBAppResizingSessionDelegate`, `_SBContinuitySessionStateMachineDelegate`, `_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider`, `_SBContinuitySessionServiceClientDelegate`
- 38 instance variables, 17 properties, 77 instance methods, 0 class methods

## Instance variables

```
@"_SBContinuitySessionStateMachine" _stateMachine;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
@"<SBContinuityButtonActionsFactory>" _buttonActionsFactory;
@"<SBContinuityUIFlushing>" _uiFlusher;
@"NSHashTable" _observers;
@"SBContinuitySessionLaunchEventExecutor" _launchEventExecutor;
@"SBMultiDisplayUserInteractionCoordinator" _multiDisplayUserInteractionCoordinator;
@"SBContinuityScreenshotManager" _screenshotManager;
@"SBContinuitySessionStoreDemoController" _storeDemoModeController;
@"SBContinuityButtonActions" _continuityButtonActions;
@"UIWindowScene" _windowScene;
@"SBWindowScene" _mainSBWindowScene;
@"UIWindowScene" _systemApertureScene;
@"UIWindowScene" _systemApertureCurtainScene;
@"NSHashTable" _orientationObservers;
q _currentInterfaceOrientation;
Q _currentSupportedInterfaceOrientation;
@"_SBContinuitySessionServiceClient" _continuitySessionServiceClient;
@"SBContinuitySessionLaunchEvent" _pendingLaunchEvent;
B _invalid;
@"<BSInvalidatable>" _keepDisplayLinkActiveAssertion;
@"<BSInvalidatable>" _focusConstraint;
@"SBOverridableUserInterfaceStyleProvider" _userInterfaceStyleProvider;
@"SBUIContinuitySessionAppearanceSettings" _appearanceSettings;
@"SBContinuityDisplayLayoutPublisher" _displayLayoutPublisher;
B _isBeingScreenRecorded;
B _clientAdoptedScreenCaptureNotifications;
@"NSHashTable" _screenRecordingObservers;
@"SBAppResizingCoordinator" _resizingCoordinator;
@"SBAppResizingSession" _currentResizingSession;
d _resizeCornerRadius;
@"NSHashTable" _resizeObservers;
@"<SAInvalidatable>" _suppressSystemApertureAssertion;
@"<BSInvalidatable>" _disableHomeGestureAssertion;
@"NSString" _displayHardwareIdentifier;
@"<SBContinuitySessionOrientationDelegate>" _orientationDelegate;
@"<BSInvalidatable>" _authenticationSessionAssertion;
@"SBDisplayLinkController" _displayLinkController;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V_authenticationSessionAssertion) authenticationSessionAssertion;
@property (T@"SBDisplayLinkController",R,N,V_displayLinkController) displayLinkController;
@property (T@"SBContinuityDisplayLayoutPublisher",R,N) displayLayoutPublisher;
@property (TB,R,N,GisMainSceneConnected) mainSceneConnected;
@property (TB,R,N,GisSceneConnected) sceneConnected;
@property (T@"NSString",R,C,N,V_displayHardwareIdentifier) displayHardwareIdentifier;
@property (T@"SBWindowScene",R,W,N) mainWindowScene;
@property (TQ,R,N) state;
@property (T@"NSSet",R,C,N) reasons;
@property (T@"<SBContinuitySessionOrientationDelegate>",W,N,V_orientationDelegate) orientationDelegate;
@property (TB,R,N,GisActivelyScreenRecording) activelyScreenRecording;
@property (T{CGSize=dd},R,N) appHostingDisplaySize;
@property (T{CGAffineTransform=dddddd},R,N) appHostingTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuitySession reasons];
-[SBContinuitySession succinctDescription];
-[SBContinuitySession setDisplayLayoutPublisher:];
-[SBContinuitySession displayLayoutPublisher];
-[SBContinuitySession description];
-[SBContinuitySession appendDescriptionToStream:];
-[SBContinuitySession state];
-[SBContinuitySession displayHardwareIdentifier];
-[SBContinuitySession addStateObserver:];
-[SBContinuitySession removeStateObserver:];
-[SBContinuitySession setOrientationDelegate:];
-[SBContinuitySession mainWindowScene];
-[SBContinuitySession _isUniversalResizabilityEnabled];
-[SBContinuitySession _updateSystemGestureWindowFrame];
-[SBContinuitySession continuitySessionServiceClient:handleLaunchEventOfType:payload:];
-[SBContinuitySession _clientReportedScreenRecordingActive:];
-[SBContinuitySession _establishFocusConstraint];
-[SBContinuitySession _handleContinuityButtonEvent:];
-[SBContinuitySession _handlePendedLaunchEventIfNecessaryAnimatedly:];
-[SBContinuitySession _invalidateFocusConstraint];
-[SBContinuitySession _invalidateForReasons:];
-[SBContinuitySession _newContinuityButtonActionsForWindowScene:];
-[SBContinuitySession _setResizing:preferredSize:];
-[SBContinuitySession addOrientationObserver:];
-[SBContinuitySession addResizeObserver:];
-[SBContinuitySession addScreenRecordingObserver:];
-[SBContinuitySession appHostingDisplaySize];
-[SBContinuitySession appHostingTransform];
-[SBContinuitySession authenticationSessionAssertion];
-[SBContinuitySession clientExternallyBlockedReasons];
-[SBContinuitySession continuitySessionServiceClient:handleContinuityButtonEvent:];
-[SBContinuitySession continuitySessionServiceClient:setHostedInterfaceOrientation:];
-[SBContinuitySession continuitySessionServiceClient:updateCornerRadiusForResize:];
-[SBContinuitySession continuitySessionServiceClient:updateHostMaximumAllowableSize:];
-[SBContinuitySession continuitySessionServiceClient:updateUserPreferredSize:toggleToOriginalSize:];
-[SBContinuitySession continuitySessionServiceClient:updatedAppearanceSettings:transitionContext:completion:];
-[SBContinuitySession continuitySessionServiceClientConnected:];
-[SBContinuitySession continuitySessionServiceClientDidCaptureScreenshot:];
-[SBContinuitySession continuitySessionServiceClientDidConfigureHIDServices:];
-[SBContinuitySession continuitySessionServiceClientDidStartScreenRecording:];
-[SBContinuitySession continuitySessionServiceClientDidStopScreenRecording:];
-[SBContinuitySession continuitySessionServiceClientDidUpdateExternallyBlockedReasons:];
-[SBContinuitySession continuitySessionServiceClientHasAdoptedScreenCaptureNotifications:];
-[SBContinuitySession continuitySessionStateMachineDidUpdateState:oldState:];
-[SBContinuitySession displayLinkController];
-[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:displayLinkController:resizingCoordinator:];
-[SBContinuitySession initWithContinuitySessionManager:applicationController:displayLinkController:];
-[SBContinuitySession invalidateForReasons:];
-[SBContinuitySession isActivelyScreenRecording];
-[SBContinuitySession isMainSceneConnected];
-[SBContinuitySession isSceneConnected];
-[SBContinuitySession noteMainSceneConnected:];
-[SBContinuitySession noteMainSceneDisconnected:];
-[SBContinuitySession noteSceneConnected:];
-[SBContinuitySession noteSceneDisconnected:];
-[SBContinuitySession noteSceneHasValidDisplayUUID:];
-[SBContinuitySession noteStoreDemoLockFailed];
-[SBContinuitySession noteSystemApertureCurtainSceneConnected:];
-[SBContinuitySession noteSystemApertureCurtainSceneDisconnected:];
-[SBContinuitySession noteSystemApertureCurtainUIIsReady:];
-[SBContinuitySession noteSystemApertureSceneConnected:];
-[SBContinuitySession noteSystemApertureSceneDisconnected:];
-[SBContinuitySession noteSystemApertureUIIsReady:];
-[SBContinuitySession noteUIIsReady:];
-[SBContinuitySession orientationDelegate];
-[SBContinuitySession removeOrientationObserver:];
-[SBContinuitySession removeResizeObserver:];
-[SBContinuitySession removeScreenRecordingObserver:];
-[SBContinuitySession resizingCoordinator:didUpdateResizingPossible:preferredSize:];
-[SBContinuitySession resizingSession:canReceiveSceneHandle:];
-[SBContinuitySession resizingSession:changedMinimumSize:maximumSize:];
-[SBContinuitySession resizingSession:committedResolvedSize:];
-[SBContinuitySession resizingSession:didCompleteResizingTransactionWithFrame:success:];
-[SBContinuitySession resizingSessionDidInvalidate:];
-[SBContinuitySession sceneManagerforContinuityScreenshotManager:];
-[SBContinuitySession setAuthenticationSessionAssertion:];
-[SBContinuitySession setInterfaceOrientation:supportedInterfaceOrientations:];
```
