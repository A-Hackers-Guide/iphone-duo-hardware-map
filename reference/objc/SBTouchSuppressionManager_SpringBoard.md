# `SBTouchSuppressionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _touchSuppressionEnabled;
@"SBTouchSuppressionShieldWindow" _touchSuppressionShieldWindow;
@"SBWindowScene" _windowScene;
@"BSCompoundAssertion" _touchSuppressionAssertions;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"BSCompoundAssertion",R,N,V_touchSuppressionAssertions) touchSuppressionAssertions;
@property (TB,N,G_isTouchSuppressionEnabled,S_setTouchSuppressionEnabled:,V_touchSuppressionEnabled) touchSuppressionEnabled;
@property (T@"SBTouchSuppressionShieldWindow",R,N,G_touchSuppressionShieldWindow,V_touchSuppressionShieldWindow) touchSuppressionShieldWindow;
```

## Instance methods

```
-[SBTouchSuppressionManager _loggingIdentifier];
-[SBTouchSuppressionManager setWindowScene:];
-[SBTouchSuppressionManager dealloc];
-[SBTouchSuppressionManager initWithWindowScene:];
-[SBTouchSuppressionManager windowScene];
-[SBTouchSuppressionManager _evaluateTouchSuppression];
-[SBTouchSuppressionManager _isTouchSuppressionEnabled];
-[SBTouchSuppressionManager _setTouchSuppressionEnabled:];
-[SBTouchSuppressionManager _touchSuppressionShieldWindow];
-[SBTouchSuppressionManager acquireTouchSuppressionAssertionWithReason:];
-[SBTouchSuppressionManager touchSuppressionAssertions];
```
