# `SBWindowSceneAuxiliaryContentController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBDisplayContentModeTransitionObserver`, `SBDisplayYoinkingControllerDelegate`, `PTSettingsKeyPathObserver`, `SBCompanionScenePresenterObserving`
- 15 instance variables, 17 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceContinuousFoldInteractionSettings" _continuousFoldSettings;
@"BSCompoundAssertion" _systemUISceneContentAssertions;
q _lastActivationPolicyForParticipantsBelow;
B _windowVisible;
@"SBWindowScene" _windowScene;
@"SBContinuousFoldCoordinator" _continuousFoldCoordinator;
@"SBWindowSceneAuxiliaryContentWindow" _window;
@"SBWindowSceneAuxiliaryContentTransitionViewController" _transitionViewController;
@"SBDisplayYoinkingController" _displayYoinkingController;
@"SBCompanionScenePresenter" _companionScenePresenter;
@"SBFZStackParticipant" _zStackParticipant;
@"<BSInvalidatable>" _continuousFoldSuppressionAssertion;
@"<BSInvalidatable>" _systemGestureDisabledAssertion;
@"NSSet" _disabledSystemGestureTypes;
@"<BSInvalidatable>" _companionSceneApertureSuppressionAssertion;
```

## Properties

```
@property (T@"SBContinuousFoldCoordinator",R,N,V_continuousFoldCoordinator) continuousFoldCoordinator;
@property (T@"SBWindowSceneAuxiliaryContentWindow",R,N,V_window) window;
@property (T@"SBWindowSceneAuxiliaryContentTransitionViewController",R,N,V_transitionViewController) transitionViewController;
@property (T@"SBDisplayYoinkingController",R,N,V_displayYoinkingController) displayYoinkingController;
@property (T@"SBCompanionScenePresenter",R,N,V_companionScenePresenter) companionScenePresenter;
@property (T@"SBFZStackParticipant",R,N,V_zStackParticipant) zStackParticipant;
@property (T@"<BSInvalidatable>",&,N,V_continuousFoldSuppressionAssertion) continuousFoldSuppressionAssertion;
@property (T@"<BSInvalidatable>",&,N,V_systemGestureDisabledAssertion) systemGestureDisabledAssertion;
@property (T@"NSSet",C,N,V_disabledSystemGestureTypes) disabledSystemGestureTypes;
@property (T@"<BSInvalidatable>",&,N,V_companionSceneApertureSuppressionAssertion) companionSceneApertureSuppressionAssertion;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N) isHostingCompanionScene;
@property (TB,R,N) isYoinkingSliderVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowSceneAuxiliaryContentController zStackParticipant];
-[SBWindowSceneAuxiliaryContentController isAvailable];
-[SBWindowSceneAuxiliaryContentController zStackParticipant:updatePreferences:];
-[SBWindowSceneAuxiliaryContentController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBWindowSceneAuxiliaryContentController continuousFoldCoordinator];
-[SBWindowSceneAuxiliaryContentController dealloc];
-[SBWindowSceneAuxiliaryContentController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBWindowSceneAuxiliaryContentController window];
-[SBWindowSceneAuxiliaryContentController zStackParticipantDidChange:];
-[SBWindowSceneAuxiliaryContentController zStackParticipant:updateZOrderPreferences:];
-[SBWindowSceneAuxiliaryContentController companionScenePresenter:hostingDidChange:];
-[SBWindowSceneAuxiliaryContentController windowScene];
-[SBWindowSceneAuxiliaryContentController companionScenePresenter];
-[SBWindowSceneAuxiliaryContentController settings:changedValueForKeyPath:];
-[SBWindowSceneAuxiliaryContentController transitionViewController];
-[SBWindowSceneAuxiliaryContentController _updateFoldSuppressionAssertion];
-[SBWindowSceneAuxiliaryContentController _activationPolicyForParticipantsBelow];
-[SBWindowSceneAuxiliaryContentController _activationPolicyForParticipantsBelowWithWindowAlpha:hasOpaqueBackground:auxiliaryContentType:];
-[SBWindowSceneAuxiliaryContentController _auxiliaryContentType];
-[SBWindowSceneAuxiliaryContentController _disabledSystemGestureTypesForAuxiliaryContentType:];
-[SBWindowSceneAuxiliaryContentController _installWindow];
-[SBWindowSceneAuxiliaryContentController _isWindowSceneEligibleForCompanionSceneHosting];
-[SBWindowSceneAuxiliaryContentController _shouldExceptWakeGesturesForAuxiliaryContentType:];
-[SBWindowSceneAuxiliaryContentController _updateAuxiliaryContent];
-[SBWindowSceneAuxiliaryContentController _updateAuxiliaryContentWithContinuationLockProvider:];
-[SBWindowSceneAuxiliaryContentController _windowSceneDisplayContentModeContext];
-[SBWindowSceneAuxiliaryContentController acquireSystemUISceneContentAssertionForReason:];
-[SBWindowSceneAuxiliaryContentController companionSceneApertureSuppressionAssertion];
-[SBWindowSceneAuxiliaryContentController continuousFoldSuppressionAssertion];
-[SBWindowSceneAuxiliaryContentController disabledSystemGestureTypes];
-[SBWindowSceneAuxiliaryContentController displayYoinkingController];
-[SBWindowSceneAuxiliaryContentController displayYoinkingControllerDidUpdateRevealState:];
-[SBWindowSceneAuxiliaryContentController initWithWindowScene:continuousFoldCoordinator:displayYoinkingCoordinator:companionScenePresenter:];
-[SBWindowSceneAuxiliaryContentController isHostingCompanionScene];
-[SBWindowSceneAuxiliaryContentController isYoinkingSliderVisible];
-[SBWindowSceneAuxiliaryContentController setCompanionSceneApertureSuppressionAssertion:];
-[SBWindowSceneAuxiliaryContentController setContinuousFoldSuppressionAssertion:];
-[SBWindowSceneAuxiliaryContentController setDisabledSystemGestureTypes:];
-[SBWindowSceneAuxiliaryContentController setSystemGestureDisabledAssertion:];
-[SBWindowSceneAuxiliaryContentController systemGestureDisabledAssertion];
```
