# `UIKBHandwritingStrokeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIKBHandwritingView" _keyView;
^{CGContext=} _bitmapContext;
d _scaleFactor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _aggregateInvalidRect;
```

## Properties

```
@property (T^{CGContext=},R,N,V_bitmapContext) bitmapContext;
@property (Td,R,N,V_scaleFactor) scaleFactor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_aggregateInvalidRect) aggregateInvalidRect;
@property (T@"UIKBHandwritingView",W,N,V_keyView) keyView;
```

## Instance methods

```
-[UIKBHandwritingStrokeView dealloc];
-[UIKBHandwritingStrokeView drawRect:];
-[UIKBHandwritingStrokeView scaleFactor];
-[UIKBHandwritingStrokeView bitmapContext];
-[UIKBHandwritingStrokeView convertRectToBitmapCoordinates:];
-[UIKBHandwritingStrokeView keyView];
-[UIKBHandwritingStrokeView _wantsDeepDrawing];
-[UIKBHandwritingStrokeView addHandwritingPoint:];
-[UIKBHandwritingStrokeView addTrapezoidFromFirstPoint:secondPoint:];
-[UIKBHandwritingStrokeView aggregateInvalidRect];
-[UIKBHandwritingStrokeView clearRect:];
-[UIKBHandwritingStrokeView convertRectToViewCoordinates:];
-[UIKBHandwritingStrokeView createBitmapIfNeeded];
-[UIKBHandwritingStrokeView displayAggregateInvalidRect];
-[UIKBHandwritingStrokeView handwritingPointToRect:];
-[UIKBHandwritingStrokeView redrawStrokesInRect:];
-[UIKBHandwritingStrokeView setKeyView:];
-[UIKBHandwritingStrokeView updateInkColor];
-[UIKBHandwritingStrokeView viewPointFromDataPoint:];
```
