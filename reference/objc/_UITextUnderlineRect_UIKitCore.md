# `_UITextUnderlineRect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextSelectionRect`
- 5 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"UIColor" _underlineColor;
q _underlineType;
@"UITextRange" _associatedTextRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (T@"UIColor",&,N,V_underlineColor) underlineColor;
@property (Tq,N,V_underlineType) underlineType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) fullRect;
@property (T@"UITextRange",&,N,V_associatedTextRange) associatedTextRange;
```

## Class methods

```
+[_UITextUnderlineRect underlineRectWithRect:offset:transform:];
```

## Instance methods

```
-[_UITextUnderlineRect init];
-[_UITextUnderlineRect setTransform:];
-[_UITextUnderlineRect transform];
-[_UITextUnderlineRect rect];
-[_UITextUnderlineRect setRect:];
-[_UITextUnderlineRect description];
-[_UITextUnderlineRect associatedTextRange];
-[_UITextUnderlineRect fullRect];
-[_UITextUnderlineRect setAssociatedTextRange:];
-[_UITextUnderlineRect setUnderlineColor:];
-[_UITextUnderlineRect setUnderlineType:];
-[_UITextUnderlineRect underlineColor];
-[_UITextUnderlineRect underlineType];
```
