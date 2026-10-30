# `UIKeyboardLayoutDictation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardLayout`
- 2 instance variables, 0 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"UIKBBackgroundView" _backgroundView;
@"UIKBTree" _keyplane;
```

## Class methods

```
+[UIKeyboardLayoutDictation activeInstance];
+[UIKeyboardLayoutDictation keyboardInputMode:supportsResizingOffsetForScreenTraits:];
+[UIKeyboardLayoutDictation keyboardSizeForInputMode:screenTraits:keyboardType:];
```

## Instance methods

```
-[UIKeyboardLayoutDictation _clipCornersOfView:];
-[UIKeyboardLayoutDictation _moveWithEvent:];
-[UIKeyboardLayoutDictation visible];
-[UIKeyboardLayoutDictation setRenderConfig:];
-[UIKeyboardLayoutDictation currentKeyplane];
-[UIKeyboardLayoutDictation dragGestureRectInView:];
-[UIKeyboardLayoutDictation layoutSubviews];
-[UIKeyboardLayoutDictation usesAutoShift];
-[UIKeyboardLayoutDictation initWithFrame:];
-[UIKeyboardLayoutDictation setupBackgroundViewForNewSplitTraits:];
-[UIKeyboardLayoutDictation shouldFadeFromLayout];
-[UIKeyboardLayoutDictation shouldFadeToLayout];
-[UIKeyboardLayoutDictation showKeyboardWithInputTraits:screenTraits:splitTraits:];
-[UIKeyboardLayoutDictation splitLeftSize];
```
