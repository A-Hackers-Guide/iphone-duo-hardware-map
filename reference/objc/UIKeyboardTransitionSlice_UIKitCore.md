# `UIKeyboardTransitionSlice`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endRect;
@"UIKBCacheToken" _startToken;
@"UIKBCacheToken" _endToken;
B _shiftContents;
B _delayCrossfade;
i _normalization;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_startRect) startRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_endRect) endRect;
@property (T@"UIKBCacheToken",&,V_startToken) startToken;
@property (T@"UIKBCacheToken",&,V_endToken) endToken;
@property (Ti,V_normalization) normalization;
@property (TB,V_delayCrossfade) delayCrossfade;
@property (TB,R) hasGeometry;
```

## Class methods

```
+[UIKeyboardTransitionSlice sliceWithStart:end:];
```

## Instance methods

```
-[UIKeyboardTransitionSlice init];
-[UIKeyboardTransitionSlice description];
-[UIKeyboardTransitionSlice endRect];
-[UIKeyboardTransitionSlice addStartRect:end:];
-[UIKeyboardTransitionSlice delayCrossfade];
-[UIKeyboardTransitionSlice endToken];
-[UIKeyboardTransitionSlice hasGeometry];
-[UIKeyboardTransitionSlice normalization];
-[UIKeyboardTransitionSlice setDelayCrossfade:];
-[UIKeyboardTransitionSlice setEndRect:];
-[UIKeyboardTransitionSlice setEndToken:];
-[UIKeyboardTransitionSlice setNormalization:];
-[UIKeyboardTransitionSlice setStartRect:];
-[UIKeyboardTransitionSlice setStartToken:];
-[UIKeyboardTransitionSlice startRect];
-[UIKeyboardTransitionSlice startToken];
```
