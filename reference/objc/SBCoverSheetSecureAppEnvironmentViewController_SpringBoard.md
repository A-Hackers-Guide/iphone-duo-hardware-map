# `SBCoverSheetSecureAppEnvironmentViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BLSBacklightStateObserving`, `SBFZStackParticipantDelegate`, `SBHomeGrabberDelegate`, `SBHomeGrabberPointerClickDelegate`, `SBSecureAppObserver`, `SBSystemApertureZStackPolicyAssistantWindowSceneProviding`, `SBTraitsParticipantDelegate`, `SBTraitsSceneSettingsUpdater`, `SBFApplicationHosting`, `SBCoverSheetSlidingViewControllerContentViewController`
- 10 instance variables, 8 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _biometricMatchingAssertion;
Q _currentOrientationMask;
@"TRAParticipant" _secureAppTraitsParticipant;
@"SBTraitsSceneParticipantDelegate" _secureAppTraitsParticipantDelegateHelper;
@"SBAudioCategoryZStackPolicyAssistant" _audioCategoryZStackPolicyAssistant;
@"SBPhysicalButtonZStackPolicyAssistant" _physicalButtonZStackPolicyAssistant;
@"SBSystemApertureZStackPolicyAssistant" _systemApertureZStackPolicyAssistant;
@"UIViewController<BSInvalidatable><CSSecureAppHosting><SBFApplicationHosting>" _secureAppViewController;
@"<SBCoverSheetSecureAppEnvironmentViewControllerDelegate>" _delegate;
@"SBFZStackParticipant" _zStackParticipant;
```

## Properties

```
@property (T@"UIViewController<BSInvalidatable><CSSecureAppHosting><SBFApplicationHosting>",R,N,V_secureAppViewController) secureAppViewController;
@property (T@"<SBCoverSheetSecureAppEnvironmentViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) contentOccludesBackground;
```

## Instance methods

```
-[SBCoverSheetSecureAppEnvironmentViewController zStackParticipant];
-[SBCoverSheetSecureAppEnvironmentViewController conformsToCSApplicationHosting];
-[SBCoverSheetSecureAppEnvironmentViewController setZStackParticipant:];
-[SBCoverSheetSecureAppEnvironmentViewController homeGrabberViewDidReceiveClick:];
-[SBCoverSheetSecureAppEnvironmentViewController zStackParticipant:updatePreferences:];
-[SBCoverSheetSecureAppEnvironmentViewController viewWillDisappear:];
-[SBCoverSheetSecureAppEnvironmentViewController supportedInterfaceOrientations];
-[SBCoverSheetSecureAppEnvironmentViewController dealloc];
-[SBCoverSheetSecureAppEnvironmentViewController participantAssociatedWindows:];
-[SBCoverSheetSecureAppEnvironmentViewController viewDidLoad];
-[SBCoverSheetSecureAppEnvironmentViewController didChangeSettingsForParticipant:context:];
-[SBCoverSheetSecureAppEnvironmentViewController handlesRotationIndependentOfCoverSheet];
-[SBCoverSheetSecureAppEnvironmentViewController secureAppViewController];
-[SBCoverSheetSecureAppEnvironmentViewController updatePreferencesForParticipant:updater:];
-[SBCoverSheetSecureAppEnvironmentViewController zStackParticipantDidChange:];
-[SBCoverSheetSecureAppEnvironmentViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBCoverSheetSecureAppEnvironmentViewController zStackParticipant:updateZOrderPreferences:];
-[SBCoverSheetSecureAppEnvironmentViewController _traitsArbiter];
-[SBCoverSheetSecureAppEnvironmentViewController viewWillAppear:];
-[SBCoverSheetSecureAppEnvironmentViewController conformsToSBApplicationHosting];
-[SBCoverSheetSecureAppEnvironmentViewController _canShowWhileLocked];
-[SBCoverSheetSecureAppEnvironmentViewController setDelegate:];
-[SBCoverSheetSecureAppEnvironmentViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBCoverSheetSecureAppEnvironmentViewController viewDidAppear:];
-[SBCoverSheetSecureAppEnvironmentViewController hostedAppSceneHandle];
-[SBCoverSheetSecureAppEnvironmentViewController canHostAnApp];
-[SBCoverSheetSecureAppEnvironmentViewController additionalEdgeSpacingForHomeGrabberView:];
-[SBCoverSheetSecureAppEnvironmentViewController traitsParticipantForSceneHandle:];
-[SBCoverSheetSecureAppEnvironmentViewController updateOrientationSceneSettingsForParticipant:];
-[SBCoverSheetSecureAppEnvironmentViewController hostedAppSceneHandles];
-[SBCoverSheetSecureAppEnvironmentViewController delegate];
-[SBCoverSheetSecureAppEnvironmentViewController needsActuationForUpdateReasons:];
-[SBCoverSheetSecureAppEnvironmentViewController appendDescriptionForParticipant:withBuilder:multilinePrefix:];
-[SBCoverSheetSecureAppEnvironmentViewController participantAssociatedSceneIdentityTokens:];
-[SBCoverSheetSecureAppEnvironmentViewController backlight:didChangeAlwaysOnEnabled:];
-[SBCoverSheetSecureAppEnvironmentViewController setBackgroundCornerRadii:forPresentationValue:];
-[SBCoverSheetSecureAppEnvironmentViewController _updateZStackPolicyAssistants];
-[SBCoverSheetSecureAppEnvironmentViewController isHostingAnApp];
-[SBCoverSheetSecureAppEnvironmentViewController secureAppOfTypeDidBegin:];
-[SBCoverSheetSecureAppEnvironmentViewController windowSceneForSystemApertureZStackPolicyAssistant:];
-[SBCoverSheetSecureAppEnvironmentViewController contentOccludesBackground];
-[SBCoverSheetSecureAppEnvironmentViewController _acquireSecureAppTraitsParticipantIfNeeded];
-[SBCoverSheetSecureAppEnvironmentViewController _actuateTraitsParticipantResolution];
-[SBCoverSheetSecureAppEnvironmentViewController _applicationSceneView];
-[SBCoverSheetSecureAppEnvironmentViewController _createTraitsSceneParticipantDelegate];
-[SBCoverSheetSecureAppEnvironmentViewController _currentSecureAppAction];
-[SBCoverSheetSecureAppEnvironmentViewController _hostableEntityPresenter];
-[SBCoverSheetSecureAppEnvironmentViewController _invalidateTraitsParticipantAndDelegateHelper];
-[SBCoverSheetSecureAppEnvironmentViewController _updateIdleWarnModeForAlwaysOnEnabled:];
-[SBCoverSheetSecureAppEnvironmentViewController _updateSupportedOrientationsMaskForSecureAppAction];
-[SBCoverSheetSecureAppEnvironmentViewController conformsToSBCoverSheetSlidingViewControllerContentViewController];
-[SBCoverSheetSecureAppEnvironmentViewController initWithSecureAppViewController:];
-[SBCoverSheetSecureAppEnvironmentViewController relinquishHiddenAssertionForHomeGrabber:animated:];
-[SBCoverSheetSecureAppEnvironmentViewController relinquishHomeGesture];
-[SBCoverSheetSecureAppEnvironmentViewController requestHomeGestureOwnership];
-[SBCoverSheetSecureAppEnvironmentViewController secureAppOfTypeDidTakeNewAssertion:];
-[SBCoverSheetSecureAppEnvironmentViewController takeHiddenAssertionForHomeGrabber:animated:];
-[SBCoverSheetSecureAppEnvironmentViewController updateHomeGrabberHiddenAssertion:];
```
