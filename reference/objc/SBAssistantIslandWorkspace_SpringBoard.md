# `SBAssistantIslandWorkspace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AIWorkspaceEnvironmentDelegate`, `SBAmbientPresentationObserver`, `SBContinuitySessionStateObserver`, `SBWindowSceneAttachmentObserving`
- 4 instance variables, 8 properties, 26 instance methods, 5 class methods

## Instance variables

```
@"SBAssistantIslandStageCoordinator" _stageCoordinator;
@"AIWorkspaceEnvironment" _environment;
@"<BSInvalidatable>" _idleTimerDisableAssertion;
@"SBContinuitySession" _currentContinuitySession;
```

## Properties

```
@property (T@"AIWorkspaceEnvironment",R,N,V_environment) environment;
@property (T@"<BSInvalidatable>",&,N,V_idleTimerDisableAssertion) idleTimerDisableAssertion;
@property (T@"SBContinuitySession",&,N,V_currentContinuitySession) currentContinuitySession;
@property (T@"SBAssistantIslandStageCoordinator",R,N,V_stageCoordinator) stageCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAssistantIslandWorkspace isEnabled];
+[SBAssistantIslandWorkspace _computeEnabled];
+[SBAssistantIslandWorkspace _enhancedSiriAvailabilityDidChange];
+[SBAssistantIslandWorkspace _startTrackingEnablement];
+[SBAssistantIslandWorkspace terminateNonIslandSpotlight];
```

## Instance methods

```
-[SBAssistantIslandWorkspace _lockStateChanged:];
-[SBAssistantIslandWorkspace windowSceneDidDisconnect:];
-[SBAssistantIslandWorkspace dealloc];
-[SBAssistantIslandWorkspace ambientPresentationController:didUpdatePresented:];
-[SBAssistantIslandWorkspace _activeWindowScene];
-[SBAssistantIslandWorkspace setIdleTimerDisableAssertion:];
-[SBAssistantIslandWorkspace idleTimerDisableAssertion];
-[SBAssistantIslandWorkspace windowSceneDidConnect:];
-[SBAssistantIslandWorkspace environment];
-[SBAssistantIslandWorkspace handleIdleTimerStateDidChange:];
-[SBAssistantIslandWorkspace handleStageActivationWithRequest:actions:completion:];
-[SBAssistantIslandWorkspace handleWakeScreen];
-[SBAssistantIslandWorkspace _coverSheetSecureAppChanged:];
-[SBAssistantIslandWorkspace _currentContinuitySessionDidChange:];
-[SBAssistantIslandWorkspace _takeMomentaryProcessAssertion];
-[SBAssistantIslandWorkspace _updateContinuitySession];
-[SBAssistantIslandWorkspace _updateContinuitySessionState];
-[SBAssistantIslandWorkspace _updateMapsShowingOnLockScreen];
-[SBAssistantIslandWorkspace continuitySessionDidUpdateState:];
-[SBAssistantIslandWorkspace currentContinuitySession];
-[SBAssistantIslandWorkspace initWithStageCoordinator:];
-[SBAssistantIslandWorkspace requestActivation:];
-[SBAssistantIslandWorkspace requestActivationWithBuilder:];
-[SBAssistantIslandWorkspace setCurrentContinuitySession:];
-[SBAssistantIslandWorkspace stageCoordinator];
-[SBAssistantIslandWorkspace useWorkspaceEnvironment];
```
