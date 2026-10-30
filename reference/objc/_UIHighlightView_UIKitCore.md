# `_UIHighlightView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _color;
d _cornerRadius;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _invertedHighlightClipRect;
@"NSArray" _cornerRadii;
@"NSMutableArray" _innerBounds;
@"NSMutableArray" _innerQuads;
B _invertHighlight;
```

## Instance methods

```
-[_UIHighlightView cleanUp];
-[_UIHighlightView setColor:];
-[_UIHighlightView drawRect:];
-[_UIHighlightView setCornerRadii:];
-[_UIHighlightView setQuads:boundaryRect:];
-[_UIHighlightView setCornerRadius:];
-[_UIHighlightView setFrame:];
-[_UIHighlightView initWithFrame:];
-[_UIHighlightView hitTest:forEvent:];
-[_UIHighlightView setFrames:boundaryRect:];
-[_UIHighlightView setInvertHighlight:clipRect:];
```
