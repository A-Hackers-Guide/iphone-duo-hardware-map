# `_UIInputViewControllerOutput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 18 instance variables, 18 properties, 47 instance methods, 1 class methods

## Instance variables

```
B _shouldDismiss;
B _proceedShouldReturn;
B _shouldAdvanceInputMode;
B _setMarkedText;
B _unmarkText;
B _requiresInputManagerSync;
B _shouldAdvanceResponder;
B _shouldPostReturnKeyNotification;
@"NSArray" _keyboardOutputs;
@"NSString" _primaryLanguage;
@"NSNumber" _hasDictation;
@"NSString" _markedText;
q _inputModeListTouchPhase;
d _inputModeListTouchBegan;
q _source;
{_NSRange="location"Q"length"Q} _selectedRange;
{CGPoint="x"d"y"d} _inputModeListFromLocation;
{CGPoint="x"d"y"d} _inputModeListUpdatePoint;
```

## Properties

```
@property (T@"NSArray",&,N,V_keyboardOutputs) keyboardOutputs;
@property (TB,N,V_shouldDismiss) shouldDismiss;
@property (TB,N,V_proceedShouldReturn) proceedShouldReturn;
@property (TB,N,V_shouldAdvanceInputMode) shouldAdvanceInputMode;
@property (T@"NSString",C,N,V_primaryLanguage) primaryLanguage;
@property (T@"NSNumber",&,N,V_hasDictation) hasDictation;
@property (TB,N,V_setMarkedText) setMarkedText;
@property (T@"NSString",C,N,V_markedText) markedText;
@property (T{_NSRange=QQ},N,V_selectedRange) selectedRange;
@property (TB,N,V_unmarkText) unmarkText;
@property (Tq,N,V_inputModeListTouchPhase) inputModeListTouchPhase;
@property (Td,N,V_inputModeListTouchBegan) inputModeListTouchBegan;
@property (T{CGPoint=dd},N,V_inputModeListFromLocation) inputModeListFromLocation;
@property (T{CGPoint=dd},N,V_inputModeListUpdatePoint) inputModeListUpdatePoint;
@property (Tq,N,V_source) source;
@property (TB,N,V_requiresInputManagerSync) requiresInputManagerSync;
@property (TB,N,V_shouldAdvanceResponder) shouldAdvanceResponder;
@property (TB,N,V_shouldPostReturnKeyNotification) shouldPostReturnKeyNotification;
```

## Class methods

```
+[_UIInputViewControllerOutput supportsSecureCoding];
```

## Instance methods

```
-[_UIInputViewControllerOutput setSelectedRange:];
-[_UIInputViewControllerOutput selectedRange];
-[_UIInputViewControllerOutput setMarkedText:];
-[_UIInputViewControllerOutput insertText:];
-[_UIInputViewControllerOutput unmarkText];
-[_UIInputViewControllerOutput primaryLanguage];
-[_UIInputViewControllerOutput setSource:];
-[_UIInputViewControllerOutput markedText];
-[_UIInputViewControllerOutput encodeWithCoder:];
-[_UIInputViewControllerOutput adjustTextPositionByCharacterOffset:];
-[_UIInputViewControllerOutput description];
-[_UIInputViewControllerOutput initWithCoder:];
-[_UIInputViewControllerOutput setPrimaryLanguage:];
-[_UIInputViewControllerOutput copyWithZone:];
-[_UIInputViewControllerOutput isEqual:];
-[_UIInputViewControllerOutput deleteBackward];
-[_UIInputViewControllerOutput source];
-[_UIInputViewControllerOutput shouldDismiss];
-[_UIInputViewControllerOutput keyboardOutputs];
-[_UIInputViewControllerOutput shouldPostReturnKeyNotification];
-[_UIInputViewControllerOutput _currentKeyboardOutput];
-[_UIInputViewControllerOutput _pushNewKeyboardOutput];
-[_UIInputViewControllerOutput hasDictation];
-[_UIInputViewControllerOutput inputModeListFromLocation];
-[_UIInputViewControllerOutput inputModeListTouchBegan];
-[_UIInputViewControllerOutput inputModeListTouchPhase];
-[_UIInputViewControllerOutput inputModeListUpdatePoint];
-[_UIInputViewControllerOutput proceedShouldReturn];
-[_UIInputViewControllerOutput requiresInputManagerSync];
-[_UIInputViewControllerOutput setHasDictation:];
-[_UIInputViewControllerOutput setInputModeList:touchBegan:fromLocation:updatePoint:];
-[_UIInputViewControllerOutput setInputModeListFromLocation:];
-[_UIInputViewControllerOutput setInputModeListTouchBegan:];
-[_UIInputViewControllerOutput setInputModeListTouchPhase:];
-[_UIInputViewControllerOutput setInputModeListUpdatePoint:];
-[_UIInputViewControllerOutput setKeyboardOutputs:];
-[_UIInputViewControllerOutput setMarkedText];
-[_UIInputViewControllerOutput setProceedShouldReturn:];
-[_UIInputViewControllerOutput setRequiresInputManagerSync:];
-[_UIInputViewControllerOutput setSetMarkedText:];
-[_UIInputViewControllerOutput setShouldAdvanceInputMode:];
-[_UIInputViewControllerOutput setShouldAdvanceResponder:];
-[_UIInputViewControllerOutput setShouldDismiss:];
-[_UIInputViewControllerOutput setShouldPostReturnKeyNotification:];
-[_UIInputViewControllerOutput setUnmarkText:];
-[_UIInputViewControllerOutput shouldAdvanceInputMode];
-[_UIInputViewControllerOutput shouldAdvanceResponder];
```
