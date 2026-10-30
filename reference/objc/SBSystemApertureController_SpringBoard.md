# `SBSystemApertureController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTraitsParticipantDelegate`, `SBSystemApertureViewControllerVisibilityDelegate`, `SBBacklightControllerObserver`, `SBFBacklightEnvironmentSceneProviding`, `PTSettingsKeyObserver`, `SBSystemApertureControlling`
- 18 instance variables, 8 properties, 65 instance methods, 0 class methods

## Instance variables

```
@"SBSystemApertureViewController" _systemApertureViewController;
@"SBSystemApertureCaptureVisibilityShimViewController" _mainCloningShimViewController;
@"SBSystemApertureCurtainViewController" _systemApertureCurtainViewController;
@"SBSystemApertureCaptureVisibilityShimViewController" _curtainCloningShimViewController;
@"TRAParticipant" _traitsParticipant;
@"SBSystemAperturePortalSourceInfoRequestServer" _systemAperturePortalSourceRequestServer;
@"SBSystemApertureSettings" _settings;
@"SBSystemApertureDefaults" _systemApertureDefaults;
@"BSCompoundAssertion" _systemApertureSuppressionCompoundAssertion;
@"BSCompoundAssertion" _suppressHidingOnClonedDisplaysCompoundAssertion;
@"<SAInvalidatable>" _jindoDefaultsSuppressionAssertion;
@"CAGainMapLayer" _prototypingDefaultGainMapDefeatingLayer;
B _containsAnyContent;
B _registeredBacklightSceneProvider;
@"UIWindow" _window;
@"UIWindow" _auxillarySuperHighLevelWindow;
@"SBWindowScene" _associatedWindowScene;
@"SBSystemApertureWindowScene" _activeWindowScene;
```

## Properties

```
@property (T@"SBSystemApertureWindowScene",W,N,V_activeWindowScene) activeWindowScene;
@property (T@"UIWindow",&,N,V_window) window;
@property (T@"UIWindow",&,N,V_auxillarySuperHighLevelWindow) auxillarySuperHighLevelWindow;
@property (T@"SBWindowScene",R,W,N,V_associatedWindowScene) associatedWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureController scenesForBacklightSession];
-[SBSystemApertureController registerElement:];
-[SBSystemApertureController restrictSystemApertureToInertWithReason:];
-[SBSystemApertureController suppressHidingOfEmptySystemApertureOnClonedDisplaysWithReason:];
-[SBSystemApertureController animateTransitionAcceptanceBounceWithVelocityVector:triggeredBlock:];
-[SBSystemApertureController setAuxillarySuperHighLevelWindow:];
-[SBSystemApertureController systemApertureRepresentationSuppressionAssertionForProximityReaderVisibility];
-[SBSystemApertureController adoptElement:withRelinquishedState:];
-[SBSystemApertureController systemApertureProximityBacklightPolicy:isSystemApertureElementVisibleAtPoint:];
-[SBSystemApertureController tearDownSystemApertureWindowWithWindowScene:];
-[SBSystemApertureController requireHeavyShadowAssertionForTransition];
-[SBSystemApertureController systemApertureRepresentationSuppressionAssertionForLiquidDetectionVisibility];
-[SBSystemApertureController retrieveFoldTransitionAssociatedSuppressionBundleIdentifiers:sceneIdentifiers:];
-[SBSystemApertureController setSystemApertureUnderAutomationTesting:];
-[SBSystemApertureController overrideContainerRenderingStyleAssertion:];
-[SBSystemApertureController backlightController:willTransitionToBacklightState:source:];
-[SBSystemApertureController animateTransitionEjectionStretchWithVelocityVector:];
-[SBSystemApertureController auxillarySuperHighLevelWindow];
-[SBSystemApertureController createSystemApertureWindowWithWindowScene:];
-[SBSystemApertureController suppressSystemApertureCompletelyWithReason:];
-[SBSystemApertureController animateDiscreteAnimationStyleForFirstElement:];
-[SBSystemApertureController defaultIslandFrameInCoordinateSpace:];
-[SBSystemApertureController handleVolumeDownButtonPress];
-[SBSystemApertureController setRequestedIndicatorElevationStyle:];
-[SBSystemApertureController relinquishElement:forReason:];
-[SBSystemApertureController setFoldTransitionPreservedSuppressionBundleIdentifiers:sceneIdentifiers:];
-[SBSystemApertureController systemApertureRepresentationSuppressionAssertionForCoversheetVisibility];
-[SBSystemApertureController systemApertureProximityBacklightPolicy:removeProximityTouchTrackingView:touchBlockingView:];
-[SBSystemApertureController systemApertureProximityBacklightPolicy:embedProximityTouchTrackingView:touchBlockingView:];
-[SBSystemApertureController hostedScenesDidChange];
-[SBSystemApertureController systemApertureRepresentationSuppressionAssertionForAuxiliaryContentCompanionSceneVisibility];
-[SBSystemApertureController requireKeyLineAssertionForTransition];
-[SBSystemApertureController systemApertureProximityBacklightPolicyShouldDisableGracePeriod:];
-[SBSystemApertureController associatedWindowScene];
-[SBSystemApertureController destinationToken];
-[SBSystemApertureController currentFirstElementFrameInCoordinateSpace:];
-[SBSystemApertureController systemApertureProximityBacklightPolicyShouldConsiderSystemApertureInert:];
-[SBSystemApertureController handleHomeButtonLongPress];
-[SBSystemApertureController activeWindowScene];
-[SBSystemApertureController _updateVisibilityForCloningAndSnapshots];
-[SBSystemApertureController initWithAssociatedWindowScene:];
-[SBSystemApertureController handleVoiceCommandButtonPress];
-[SBSystemApertureController dealloc];
-[SBSystemApertureController participantAssociatedWindows:];
-[SBSystemApertureController handleHeadsetButtonPress:];
-[SBSystemApertureController didChangeSettingsForParticipant:context:];
-[SBSystemApertureController updatePreferencesForParticipant:updater:];
-[SBSystemApertureController window];
-[SBSystemApertureController handleLockButtonPress];
-[SBSystemApertureController handleVolumeUpButtonPress];
-[SBSystemApertureController settings:changedValueForKey:];
-[SBSystemApertureController setActiveWindowScene:];
-[SBSystemApertureController handleHomeButtonDoublePress];
-[SBSystemApertureController _updateSuppressionForDefaults];
-[SBSystemApertureController _configureBacklightEnvironmentSceneProviderIfNecessary];
-[SBSystemApertureController tearDownSuperHighLevelSystemApertureWindowWithWindowScene:];
-[SBSystemApertureController applyPersistentAnimationStyleForFirstElement:];
-[SBSystemApertureController isTransitionTargetForSceneIdentifier:bundleIdentifier:];
-[SBSystemApertureController restrictSystemApertureToDefaultLayoutWithReason:];
-[SBSystemApertureController appendDescriptionForParticipant:withBuilder:multilinePrefix:];
-[SBSystemApertureController createSuperHighLevelSystemApertureWindowWithWindowScene:];
-[SBSystemApertureController setWindow:];
-[SBSystemApertureController _reevaluateSystemApertureCompleteSuppression];
-[SBSystemApertureController handleHomeButtonPress];
-[SBSystemApertureController systemApertureViewController:containsAnyContent:];
```
