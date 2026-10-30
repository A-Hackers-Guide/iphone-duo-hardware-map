# `SBHardwareButtonBezelEffectsCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCaptureButtonPreludeAnimatingPrivate`, `SBHardwareButtonHintDropletViewControllerDelegate`, `SBHardwareButtonPreludeAnimating`, `SBHardwareButtonHintDropletAnimating`
- 19 instance variables, 5 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"_SBCaptureButtonLaunchAnimationPreludeToken" _animatingPreludeToken;
q _lastRequestedLaunchOrigin;
@"<SBHardwareButtonLaunchZoomUpAnimationToken>" _animatingLaunchCompletionToken;
@"NSMutableArray" _portalObservationTokens;
@"SBFSecureTouchPassThroughWindow" _dropletLaunchWindow;
@"SBCaptureButtonDropletLaunchViewController" _dropletLaunchViewController;
@"SUIAShockwaveViewController" _shockwaveViewController;
@"SBCaptureButtonSettings" _settings;
B _animatingShockwave;
Q _shockwaveAnimationRevisionID;
B _animatingDropletCancellation;
B _animatingShockwaveCancellation;
@"NSCountedSet" _backlightAssertionRequiringReasons;
@"<BSInvalidatable>" _liveUpdatingAssertion;
@"SBFSecureTouchPassThroughWindow" _hintDropletWindow;
@"SBHardwareButtonHintDropletViewController" _hintDropletViewController;
@"BSCompoundAssertion" _systemGlowEffectAssertion;
B _systemGlowActivating;
```

## Properties

```
@property (T@"UIView",R,N) dropletLaunchPortalSourceView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHardwareButtonBezelEffectsCoordinator dealloc];
-[SBHardwareButtonBezelEffectsCoordinator activateHintDropletForButton:];
-[SBHardwareButtonBezelEffectsCoordinator updateSystemGlowStyle:];
-[SBHardwareButtonBezelEffectsCoordinator initWithWindowScene:];
-[SBHardwareButtonBezelEffectsCoordinator updateHintContentVisibility:forButton:animationSettings:];
-[SBHardwareButtonBezelEffectsCoordinator setDropletLayoutCallback:forButton:];
-[SBHardwareButtonBezelEffectsCoordinator associateHintView:withButton:];
-[SBHardwareButtonBezelEffectsCoordinator observePortalSourceWithHandler:];
-[SBHardwareButtonBezelEffectsCoordinator _beginRequiringBacklightAssertionForReason:];
-[SBHardwareButtonBezelEffectsCoordinator _endRequiringBacklightAssertionForReason:];
-[SBHardwareButtonBezelEffectsCoordinator _policyAggregator];
-[SBHardwareButtonBezelEffectsCoordinator _presentOrDismissLaunchAnimationWindowIfNecessary];
-[SBHardwareButtonBezelEffectsCoordinator _reevaluateSystemGlowEffect];
-[SBHardwareButtonBezelEffectsCoordinator _setHintDropletWindowVisible:];
-[SBHardwareButtonBezelEffectsCoordinator _setLaunchAnimationWindowVisible:];
-[SBHardwareButtonBezelEffectsCoordinator _setShockwaveState:completion:];
-[SBHardwareButtonBezelEffectsCoordinator _updateLaunchAnimationWindowLevelIfNecessary];
-[SBHardwareButtonBezelEffectsCoordinator animateLaunchZoomUpPreludeFromButton:];
-[SBHardwareButtonBezelEffectsCoordinator animatingDroplet];
-[SBHardwareButtonBezelEffectsCoordinator animatingDropletContext];
-[SBHardwareButtonBezelEffectsCoordinator cancelPrelude];
-[SBHardwareButtonBezelEffectsCoordinator commandeerDropletAnimationWithToken:];
-[SBHardwareButtonBezelEffectsCoordinator dropletLaunchPortalSourceView];
-[SBHardwareButtonBezelEffectsCoordinator hintDropletViewControllerDidBecomeIdle:];
-[SBHardwareButtonBezelEffectsCoordinator hintDropletsEnabled];
-[SBHardwareButtonBezelEffectsCoordinator preludeAnimationRectPresentationValue];
-[SBHardwareButtonBezelEffectsCoordinator preludeAnimationVelocity];
-[SBHardwareButtonBezelEffectsCoordinator preludeToken:expandHintingDropletByAddingComponents:shockwave:];
-[SBHardwareButtonBezelEffectsCoordinator preludeToken:updateShockwaveLightType:];
-[SBHardwareButtonBezelEffectsCoordinator requestSystemGlowEffectWithInitialStyle:reason:];
-[SBHardwareButtonBezelEffectsCoordinator updateLaunchAnimationWindowLevelBasedOnRequests];
-[SBHardwareButtonBezelEffectsCoordinator zoomUpToken:appendZoomUpCompletionBlock:];
```
