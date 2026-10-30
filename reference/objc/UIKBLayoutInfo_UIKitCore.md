# `UIKBLayoutInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isAutoShifted;
B _isShiftLocked;
@"UIKBScreenTraits" _screenTraits;
@"UITextInputTraits" _textInputTraits;
```

## Properties

```
@property (TB,N,V_isAutoShifted) isAutoShifted;
@property (TB,N,V_isShiftLocked) isShiftLocked;
@property (T@"UIKBScreenTraits",&,N,V_screenTraits) screenTraits;
@property (T@"UITextInputTraits",&,N,V_textInputTraits) textInputTraits;
```

## Instance methods

```
-[UIKBLayoutInfo isShiftLocked];
-[UIKBLayoutInfo isAutoShifted];
-[UIKBLayoutInfo textInputTraits];
-[UIKBLayoutInfo setTextInputTraits:];
-[UIKBLayoutInfo setScreenTraits:];
-[UIKBLayoutInfo screenTraits];
-[UIKBLayoutInfo setIsAutoShifted:];
-[UIKBLayoutInfo setIsShiftLocked:];
```
