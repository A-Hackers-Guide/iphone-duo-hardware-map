# `SBHomeScreenReturnToSpotlightPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _lastKnownActivationState;
d _anchorTimeForReactivationWindow;
B _shouldReactivateSpotlight;
@"UIApplicationSceneDeactivationAssertion" _spotlightSceneDeactivationAssertion;
@"UIApplicationSceneDeactivationAssertion" _homeScreenInactiveReason;
B _shouldAnimateReactivation;
d _reactivationWindowDuration;
```

## Properties

```
@property (Td,N,V_reactivationWindowDuration) reactivationWindowDuration;
@property (TB,N,V_shouldAnimateReactivation) shouldAnimateReactivation;
```

## Class methods

```
+[SBHomeScreenReturnToSpotlightPolicy supportsSpotlightReturnToHomeForWindowScene:];
```

## Instance methods

```
-[SBHomeScreenReturnToSpotlightPolicy init];
-[SBHomeScreenReturnToSpotlightPolicy _elapsedTime];
-[SBHomeScreenReturnToSpotlightPolicy homeScreenZStackParticipantDidChange:launchingForSpotlight:];
-[SBHomeScreenReturnToSpotlightPolicy reactivationWindowDuration];
-[SBHomeScreenReturnToSpotlightPolicy setReactivationWindowDuration:];
-[SBHomeScreenReturnToSpotlightPolicy setShouldAnimateReactivation:];
-[SBHomeScreenReturnToSpotlightPolicy shouldAnimateReactivation];
-[SBHomeScreenReturnToSpotlightPolicy willReactivateSpotlight];
```
