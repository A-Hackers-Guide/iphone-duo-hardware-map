# `SBHIDValueModifyingButtonSetArbiter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDButtonStateDelegate`
- 7 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _usageToButtonDictionary;
@"NSDictionary" _buttonToUsageDictionary;
@"BSAbsoluteMachTimer" _timer;
@"SBHIDButtonStateArbiter" _currentDownButton;
@"<SBHIDValueModifyingButtonSetArbiterDelegate>" _delegate;
d _initialRepeatDelay;
d _subsequentRepeatDelay;
```

## Properties

```
@property (Td,N,V_initialRepeatDelay) initialRepeatDelay;
@property (Td,N,V_subsequentRepeatDelay) subsequentRepeatDelay;
@property (T@"<SBHIDValueModifyingButtonSetArbiterDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBHIDValueModifyingButtonSetArbiter dealloc];
-[SBHIDValueModifyingButtonSetArbiter reset];
-[SBHIDValueModifyingButtonSetArbiter performActionsForButtonUp:];
-[SBHIDValueModifyingButtonSetArbiter setDelegate:];
-[SBHIDValueModifyingButtonSetArbiter performActionsForButtonDown:];
-[SBHIDValueModifyingButtonSetArbiter delegate];
-[SBHIDValueModifyingButtonSetArbiter performActionsForButtonLongPress:];
-[SBHIDValueModifyingButtonSetArbiter processKeyboardEvent:];
-[SBHIDValueModifyingButtonSetArbiter _invalidateRepeatingActionTimer];
-[SBHIDValueModifyingButtonSetArbiter _fireRepeatingActionTimer];
-[SBHIDValueModifyingButtonSetArbiter _performActionForButton:];
-[SBHIDValueModifyingButtonSetArbiter _startRepeatingActionTimer];
-[SBHIDValueModifyingButtonSetArbiter initWithHIDKeyPressEventUsages:initialRepeatDelay:subsequentRepeatDelay:];
-[SBHIDValueModifyingButtonSetArbiter initialRepeatDelay];
-[SBHIDValueModifyingButtonSetArbiter setInitialRepeatDelay:];
-[SBHIDValueModifyingButtonSetArbiter setSubsequentRepeatDelay:];
-[SBHIDValueModifyingButtonSetArbiter subsequentRepeatDelay];
```
