# `_UIFocusEnvironmentPrivate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIFocusEnvironment`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N,G_isEligibleForFocusInteraction) eligibleForFocusInteraction;
@property (TB,?,R,N,G_isEligibleForFocusOcclusion) eligibleForFocusOcclusion;
@property (Tq,?,R,N,G_preferredFocusMovementStyle) preferredFocusMovementStyle;
@property (T@"NSArray",?,R,C,N,G_linearFocusMovementSequences) linearFocusMovementSequences;
```

## Instance methods

```
-[_UIFocusEnvironmentPrivate _isEligibleForFocusInteraction];
-[_UIFocusEnvironmentPrivate _rotaryFocusMovementAxis];
-[_UIFocusEnvironmentPrivate _isEligibleForFocusOcclusion];
-[_UIFocusEnvironmentPrivate _clippingRectInCoordinateSpace:];
-[_UIFocusEnvironmentPrivate _setNeedsNonDeferredFocusUpdate];
-[_UIFocusEnvironmentPrivate _allowsFocusToLeaveViaHeading:];
-[_UIFocusEnvironmentPrivate _focusFallbackScroller];
-[_UIFocusEnvironmentPrivate _linearFocusMovementSequences];
-[_UIFocusEnvironmentPrivate _preferredFocusMovementStyle];
```
