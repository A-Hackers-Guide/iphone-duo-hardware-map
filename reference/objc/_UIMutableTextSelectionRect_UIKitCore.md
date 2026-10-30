# `_UIMutableTextSelectionRect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextSelectionRect`
- 10 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _containsStart;
B _containsEnd;
B _isVertical;
B __drawsOwnHighlight;
q _writingDirection;
@"CAShapeLayer" _hostHighlightContainerLayer;
@"UIBezierPath" __path;
@"UITextSelectionRectCustomHandleInfo" __customHandleInfo;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (Tq,N,V_writingDirection) writingDirection;
@property (TB,N,V_containsStart) containsStart;
@property (TB,N,V_containsEnd) containsEnd;
@property (TB,N,V_isVertical) isVertical;
@property (TB,N,S_setDrawsOwnHighlight:,V__drawsOwnHighlight) _drawsOwnHighlight;
@property (T@"UIBezierPath",&,N,V__path) _path;
@property (T@"UITextSelectionRectCustomHandleInfo",&,N,V__customHandleInfo) _customHandleInfo;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (T@"CAShapeLayer",W,N,V_hostHighlightContainerLayer) _highlightContainerLayer;
```

## Class methods

```
+[_UIMutableTextSelectionRect selectionRectWithRect:fromView:];
```

## Instance methods

```
-[_UIMutableTextSelectionRect _highlightContainerLayer];
-[_UIMutableTextSelectionRect setContainsStart:];
-[_UIMutableTextSelectionRect init];
-[_UIMutableTextSelectionRect isVertical];
-[_UIMutableTextSelectionRect _path];
-[_UIMutableTextSelectionRect setContainsEnd:];
-[_UIMutableTextSelectionRect _setDrawsOwnHighlight:];
-[_UIMutableTextSelectionRect set_highlightContainerLayer:];
-[_UIMutableTextSelectionRect setTransform:];
-[_UIMutableTextSelectionRect setWritingDirection:];
-[_UIMutableTextSelectionRect transform];
-[_UIMutableTextSelectionRect rect];
-[_UIMutableTextSelectionRect containsStart];
-[_UIMutableTextSelectionRect set_customHandleInfo:];
-[_UIMutableTextSelectionRect hash];
-[_UIMutableTextSelectionRect description];
-[_UIMutableTextSelectionRect setIsVertical:];
-[_UIMutableTextSelectionRect set_path:];
-[_UIMutableTextSelectionRect containsEnd];
-[_UIMutableTextSelectionRect writingDirection];
-[_UIMutableTextSelectionRect isEqual:];
-[_UIMutableTextSelectionRect _ui_isKindOfTextSelectionRect];
-[_UIMutableTextSelectionRect _customHandleInfo];
-[_UIMutableTextSelectionRect _drawsOwnHighlight];
-[_UIMutableTextSelectionRect setRect:fromView:];
```
