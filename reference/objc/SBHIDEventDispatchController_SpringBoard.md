# `SBHIDEventDispatchController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 6 instance methods, 4 class methods

## Instance variables

```
@"<BSInvalidatable>" _dispatchingAssertion;
@"<BSInvalidatable>" _dispatchingAssertionForVoiceCommand;
@"<BSInvalidatable>" _keyCommandDispatchingAssertion;
@"<BSInvalidatable>" _dispatchingAssertionForPrototypingCaptureButton;
@"<BSInvalidatable>" _dispatchingAssertionForCaptureButton;
@"BSCompoundAssertion" _overrideKeyboardUsagesForSystemEnvironment;
@"BKSHIDEventDiscreteDispatchingRule" _overrideKeyboardUsagesRule;
@"BKSHIDEventDiscreteDispatchingRule" _chamoisTrackpadRule;
@"NSArray" _dispatchingRulesForMainRoot;
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"BKSHIDEventDispatchingTarget" _mainSystemDispatchingTarget;
@"BKSHIDEventDispatchingTarget" _keyboardFocusDispatchingTarget;
```

## Class methods

```
+[SBHIDEventDispatchController sharedInstance];
+[SBHIDEventDispatchController symbolicDeferringTokenForKeyboardFocus];
+[SBHIDEventDispatchController symbolicDeferringTokenForSystemGesturesInDisplayConfiguration:];
+[SBHIDEventDispatchController symbolicDeferringTokenForSystemGesturesOnMainDisplay];
```

## Instance methods

```
-[SBHIDEventDispatchController init];
-[SBHIDEventDispatchController _keyCommandDispatchingRule];
-[SBHIDEventDispatchController _resetMainDeliveryRoot];
-[SBHIDEventDispatchController configureDispatchRootsForChamoisDisplay:];
-[SBHIDEventDispatchController configureDispatchRootsForContinuityDisplay:];
-[SBHIDEventDispatchController dispatchKeyboardUsagesToSystemEnvironment:reason:];
```
