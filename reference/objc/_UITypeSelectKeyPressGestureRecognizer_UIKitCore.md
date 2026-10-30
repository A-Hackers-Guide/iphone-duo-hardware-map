# `_UITypeSelectKeyPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 3 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _presses;
@"NSMutableString" _inputString;
@"NSString" _programmaticInput;
```

## Properties

```
@property (T@"NSMutableString",&,N,V_inputString) inputString;
@property (T@"NSString",&,N,V_programmaticInput) programmaticInput;
```

## Instance methods

```
-[_UITypeSelectKeyPressGestureRecognizer _shouldReceivePress:];
-[_UITypeSelectKeyPressGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UITypeSelectKeyPressGestureRecognizer pressesCancelled:withEvent:];
-[_UITypeSelectKeyPressGestureRecognizer pressesEnded:withEvent:];
-[_UITypeSelectKeyPressGestureRecognizer setProgrammaticInput:];
-[_UITypeSelectKeyPressGestureRecognizer initWithTarget:action:];
-[_UITypeSelectKeyPressGestureRecognizer pressesBegan:withEvent:];
-[_UITypeSelectKeyPressGestureRecognizer pressesChanged:withEvent:];
-[_UITypeSelectKeyPressGestureRecognizer setInputString:];
-[_UITypeSelectKeyPressGestureRecognizer _shouldReceiveEvent:];
-[_UITypeSelectKeyPressGestureRecognizer hasActiveTypeSelectSession];
-[_UITypeSelectKeyPressGestureRecognizer programmaticInput];
-[_UITypeSelectKeyPressGestureRecognizer resetInput];
-[_UITypeSelectKeyPressGestureRecognizer inputString];
```
