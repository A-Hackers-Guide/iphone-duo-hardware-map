# `_UITextViewContentPadding`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _mode;
d _targetValue;
d _currentValue;
@"<_UITextViewContentPaddingDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UITextViewContentPaddingDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_mode) mode;
@property (Td,N,V_targetValue) targetValue;
@property (Td,R,N,V_currentValue) currentValue;
```

## Instance methods

```
-[_UITextViewContentPadding _checkNewCurrentValue];
-[_UITextViewContentPadding initWithDelegate:];
-[_UITextViewContentPadding setTargetValue:];
-[_UITextViewContentPadding resetCurrentValue];
-[_UITextViewContentPadding currentValue];
-[_UITextViewContentPadding setMode:];
-[_UITextViewContentPadding setDelegate:];
-[_UITextViewContentPadding targetValue];
-[_UITextViewContentPadding mode];
-[_UITextViewContentPadding delegate];
-[_UITextViewContentPadding description];
-[_UITextViewContentPadding increaseToValue:];
```
