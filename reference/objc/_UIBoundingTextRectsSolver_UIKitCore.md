# `_UIBoundingTextRectsSolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UITextRange" _range;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _firstRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _middleRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _totalRect;
B _calculated;
B _unifyRects;
@"NSTextContainer" _textContainer;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) firstLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bodyRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) lastLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundingRect;
@property (T@"NSArray",R,N) rects;
```

## Instance methods

```
-[_UIBoundingTextRectsSolver boundingRect];
-[_UIBoundingTextRectsSolver description];
-[_UIBoundingTextRectsSolver _calculate];
-[_UIBoundingTextRectsSolver _calculateRectsUsingLayoutManager:];
-[_UIBoundingTextRectsSolver _calculateRectsUsingTextLayoutManager:];
-[_UIBoundingTextRectsSolver _calculateTotalRect];
-[_UIBoundingTextRectsSolver _coalesceRectsForRects:];
-[_UIBoundingTextRectsSolver bodyRect];
-[_UIBoundingTextRectsSolver firstLineRect];
-[_UIBoundingTextRectsSolver initWithTextContainer:range:unifyRects:];
-[_UIBoundingTextRectsSolver lastLineRect];
-[_UIBoundingTextRectsSolver rects];
```
