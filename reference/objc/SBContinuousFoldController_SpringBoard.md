# `SBContinuousFoldController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `PTSettingsKeyPathObserver`
- 13 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBContinuousFoldCoordinator" _continuousFoldCoordinator;
@"SBDeviceContinuousFoldInteractionSettings" _continuousFoldSettings;
@"SBSecureWindow" _window;
@"<SBContinuousFoldEffectViewControlling>" _effectViewController;
@"<BSInvalidatable>" _settleOrientationLock;
d _lastContinuousFoldPosition;
d _lastHingeAngleDegrees;
q _lastEffectMode;
B _awaitingCloakReveal;
@"BSCompoundAssertion" _suppressionAssertion;
@"BSCompoundAssertion" _transitionAssertion;
@"<BSInvalidatable>" _accessibilitySuppresionAssertion;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N) isEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuousFoldController _updateWindowVisibility];
-[SBContinuousFoldController isSuppressed];
-[SBContinuousFoldController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBContinuousFoldController dealloc];
-[SBContinuousFoldController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBContinuousFoldController isEnabled];
-[SBContinuousFoldController windowScene];
-[SBContinuousFoldController settings:changedValueForKeyPath:];
-[SBContinuousFoldController _updateWindowForCurrentSettings];
-[SBContinuousFoldController _applyDebugWindowBorder];
-[SBContinuousFoldController _effectModeForTransitionContext:];
-[SBContinuousFoldController _installEffectViewController:];
-[SBContinuousFoldController _presentEffectWithMode:foldEffectProgress:];
-[SBContinuousFoldController _requiredEffectViewControllerClass];
-[SBContinuousFoldController _shouldDeferEffectUntilRevealForContext:displayContentModeCoordinator:];
-[SBContinuousFoldController _updateAccessbilitySuppressionAssertion];
-[SBContinuousFoldController _updateEffectViewControllerForCurrentSettings];
-[SBContinuousFoldController _updateWindowContentsForCurrentSettings];
-[SBContinuousFoldController initWithWindowScene:continuousFoldCoordinator:];
-[SBContinuousFoldController noteCloakRevealBegan];
-[SBContinuousFoldController requestSuppressionAssertionWithReason:];
-[SBContinuousFoldController requestTransitionAssertion:];
```
