# `SBDeviceOrientationUpdateDeferralManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _globalDeferralAssertion;
@"NSMapTable" _windowSceneToDeferralAssertions;
@"NSHashTable" _observers;
@"<BSInvalidatable>" _stateCaptureHandle;
```

## Instance methods

```
-[SBDeviceOrientationUpdateDeferralManager succinctDescriptionBuilder];
-[SBDeviceOrientationUpdateDeferralManager removeObserver:];
-[SBDeviceOrientationUpdateDeferralManager init];
-[SBDeviceOrientationUpdateDeferralManager dealloc];
-[SBDeviceOrientationUpdateDeferralManager descriptionWithMultilinePrefix:];
-[SBDeviceOrientationUpdateDeferralManager succinctDescription];
-[SBDeviceOrientationUpdateDeferralManager addObserver:];
-[SBDeviceOrientationUpdateDeferralManager description];
-[SBDeviceOrientationUpdateDeferralManager descriptionBuilderWithMultilinePrefix:];
-[SBDeviceOrientationUpdateDeferralManager _notifyObserversForWindowScene:];
-[SBDeviceOrientationUpdateDeferralManager _deferralStateDidUpdateForWindowScene:];
-[SBDeviceOrientationUpdateDeferralManager _globalDeferralStateDidUpdate];
-[SBDeviceOrientationUpdateDeferralManager acquireDeviceOrientationUpdateDeferralAssertionForWindowScene:reason:];
-[SBDeviceOrientationUpdateDeferralManager acquireDeviceOrientationUpdateDeferralAssertionWithReason:];
-[SBDeviceOrientationUpdateDeferralManager isCurrentlyDeferringOrientationUpdatesForWindowScene:];
```
