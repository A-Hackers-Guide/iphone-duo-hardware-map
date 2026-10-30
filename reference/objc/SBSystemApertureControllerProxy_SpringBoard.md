# `SBSystemApertureControllerProxy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureControllingPrivate`, `SBSystemApertureCoordinatingTest`
- 8 instance variables, 14 properties, 63 instance methods, 0 class methods

## Instance variables

```
B _disconnected;
@"<SBSystemApertureControllerProxyDelegate>" _delegate;
@"SBSystemApertureController" _controller;
@"SBWindowScene" _associatedWindowScene;
@"NSMapTable" _elementsToAssertions;
@"<SAInvalidatable>" _restrictSystemApertureToInertAssertion;
@"<SAInvalidatable>" _suppressSystemApertureCompletelyAssertion;
@"<SAInvalidatable>" _suppressHidingOfEmptySystemApertureOnClonedDisplaysAssertion;
```

## Properties

```
@property (T@"SBSystemApertureController",R,N,V_controller) controller;
@property (TB,N,GisDisconnected,V_disconnected) disconnected;
@property (T@"<SBSystemApertureControllerProxyDelegate>",R,W,N,V_delegate) delegate;
@property (T@"SBWindowScene",R,W,N,V_associatedWindowScene) associatedWindowScene;
@property (T@"NSMapTable",&,N,V_elementsToAssertions) elementsToAssertions;
@property (T@"<SAInvalidatable>",&,N,V_restrictSystemApertureToInertAssertion) restrictSystemApertureToInertAssertion;
@property (T@"<SAInvalidatable>",&,N,V_suppressSystemApertureCompletelyAssertion) suppressSystemApertureCompletelyAssertion;
@property (T@"<SAInvalidatable>",&,N,V_suppressHidingOfEmptySystemApertureOnClonedDisplaysAssertion) suppressHidingOfEmptySystemApertureOnClonedDisplaysAssertion;
@property (T@"UIWindow",R,N) window;
@property (T@"UIWindow",R,N) auxillarySuperHighLevelWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureControllerProxy registerElement:];
-[SBSystemApertureControllerProxy restrictSystemApertureToInertWithReason:];
-[SBSystemApertureControllerProxy suppressHidingOfEmptySystemApertureOnClonedDisplaysWithReason:];
-[SBSystemApertureControllerProxy animateTransitionAcceptanceBounceWithVelocityVector:triggeredBlock:];
-[SBSystemApertureControllerProxy systemApertureRepresentationSuppressionAssertionForProximityReaderVisibility];
-[SBSystemApertureControllerProxy adoptElement:withRelinquishedState:];
-[SBSystemApertureControllerProxy systemApertureProximityBacklightPolicy:isSystemApertureElementVisibleAtPoint:];
-[SBSystemApertureControllerProxy tearDownSystemApertureWindowWithWindowScene:];
-[SBSystemApertureControllerProxy requireHeavyShadowAssertionForTransition];
-[SBSystemApertureControllerProxy systemApertureRepresentationSuppressionAssertionForLiquidDetectionVisibility];
-[SBSystemApertureControllerProxy retrieveFoldTransitionAssociatedSuppressionBundleIdentifiers:sceneIdentifiers:];
-[SBSystemApertureControllerProxy setSystemApertureUnderAutomationTesting:];
-[SBSystemApertureControllerProxy overrideContainerRenderingStyleAssertion:];
-[SBSystemApertureControllerProxy animateTransitionEjectionStretchWithVelocityVector:];
-[SBSystemApertureControllerProxy auxillarySuperHighLevelWindow];
-[SBSystemApertureControllerProxy createSystemApertureWindowWithWindowScene:];
-[SBSystemApertureControllerProxy suppressSystemApertureCompletelyWithReason:];
-[SBSystemApertureControllerProxy restrictSystemApertureToInertAssertion];
-[SBSystemApertureControllerProxy animateDiscreteAnimationStyleForFirstElement:];
-[SBSystemApertureControllerProxy defaultIslandFrameInCoordinateSpace:];
-[SBSystemApertureControllerProxy handleVolumeDownButtonPress];
-[SBSystemApertureControllerProxy setRequestedIndicatorElevationStyle:];
-[SBSystemApertureControllerProxy relinquishElement:forReason:];
-[SBSystemApertureControllerProxy setFoldTransitionPreservedSuppressionBundleIdentifiers:sceneIdentifiers:];
-[SBSystemApertureControllerProxy systemApertureRepresentationSuppressionAssertionForCoversheetVisibility];
-[SBSystemApertureControllerProxy systemApertureProximityBacklightPolicy:removeProximityTouchTrackingView:touchBlockingView:];
-[SBSystemApertureControllerProxy systemApertureProximityBacklightPolicy:embedProximityTouchTrackingView:touchBlockingView:];
-[SBSystemApertureControllerProxy hostedScenesDidChange];
-[SBSystemApertureControllerProxy systemApertureRepresentationSuppressionAssertionForAuxiliaryContentCompanionSceneVisibility];
-[SBSystemApertureControllerProxy requireKeyLineAssertionForTransition];
-[SBSystemApertureControllerProxy systemApertureProximityBacklightPolicyShouldDisableGracePeriod:];
-[SBSystemApertureControllerProxy associatedWindowScene];
-[SBSystemApertureControllerProxy destinationToken];
-[SBSystemApertureControllerProxy currentFirstElementFrameInCoordinateSpace:];
-[SBSystemApertureControllerProxy controller];
-[SBSystemApertureControllerProxy systemApertureProximityBacklightPolicyShouldConsiderSystemApertureInert:];
-[SBSystemApertureControllerProxy handleHomeButtonLongPress];
-[SBSystemApertureControllerProxy elementsToAssertions];
-[SBSystemApertureControllerProxy setSuppressSystemApertureCompletelyAssertion:];
-[SBSystemApertureControllerProxy invalidateElement:forReason:];
-[SBSystemApertureControllerProxy handleVoiceCommandButtonPress];
-[SBSystemApertureControllerProxy dealloc];
-[SBSystemApertureControllerProxy suppressHidingOfEmptySystemApertureOnClonedDisplaysAssertion];
-[SBSystemApertureControllerProxy handleHeadsetButtonPress:];
-[SBSystemApertureControllerProxy setRestrictSystemApertureToInertAssertion:];
-[SBSystemApertureControllerProxy window];
-[SBSystemApertureControllerProxy handleLockButtonPress];
-[SBSystemApertureControllerProxy setSuppressHidingOfEmptySystemApertureOnClonedDisplaysAssertion:];
-[SBSystemApertureControllerProxy handleVolumeUpButtonPress];
-[SBSystemApertureControllerProxy handleHomeButtonDoublePress];
-[SBSystemApertureControllerProxy initWithDelegate:associatedWindowScene:];
-[SBSystemApertureControllerProxy setDisconnected:];
-[SBSystemApertureControllerProxy tearDownSuperHighLevelSystemApertureWindowWithWindowScene:];
-[SBSystemApertureControllerProxy delegate];
-[SBSystemApertureControllerProxy applyPersistentAnimationStyleForFirstElement:];
-[SBSystemApertureControllerProxy isTransitionTargetForSceneIdentifier:bundleIdentifier:];
-[SBSystemApertureControllerProxy restrictSystemApertureToDefaultLayoutWithReason:];
-[SBSystemApertureControllerProxy isDisconnected];
-[SBSystemApertureControllerProxy registerElementWithController:];
-[SBSystemApertureControllerProxy suppressSystemApertureCompletelyAssertion];
-[SBSystemApertureControllerProxy createSuperHighLevelSystemApertureWindowWithWindowScene:];
-[SBSystemApertureControllerProxy handleHomeButtonPress];
-[SBSystemApertureControllerProxy setElementsToAssertions:];
```
