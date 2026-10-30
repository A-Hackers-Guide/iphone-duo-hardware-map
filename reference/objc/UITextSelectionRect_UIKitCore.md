# `UITextSelectionRect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 17 properties, 24 instance methods, 8 class methods

## Instance variables

```
@"NSValue" _legacyTransform;
d _baselineOffset;
```

## Properties

```
@property (T@"UITextSelectionRectImpl",R,N,G_isImpl) isImpl;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _startEdgeRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _endEdgeRect;
@property (T@"UISelectionGrabberCustomPath",R,N) _startCustomSelectionPath;
@property (T@"UISelectionGrabberCustomPath",R,N) _endCustomSelectionPath;
@property (TB,R,N) _drawsOwnHighlight;
@property (T@"UIBezierPath",R,N) _path;
@property (T@"UITextSelectionRectCustomHandleInfo",R,N) _customHandleInfo;
@property (T@"CAShapeLayer",R,N) _highlightContainerLayer;
@property (T@"NSValue",&,N,S_setTransform:,V_legacyTransform) _transform;
@property (Td,N,V_baselineOffset) baselineOffset;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) rect;
@property (Tq,R,N) writingDirection;
@property (TB,R,N) containsStart;
@property (TB,R,N) containsEnd;
@property (TB,R,N) isVertical;
@property (T{CGAffineTransform=dddddd},R,N) transform;
```

## Class methods

```
+[UITextSelectionRect endCustomSelectionPathFromRects:];
+[UITextSelectionRect endEdgeFromRects:];
+[UITextSelectionRect endIsHorizontal:];
+[UITextSelectionRect endRectFromRects:];
+[UITextSelectionRect startCustomSelectionPathFromRects:];
+[UITextSelectionRect startEdgeFromRects:];
+[UITextSelectionRect startIsHorizontal:];
+[UITextSelectionRect startRectFromRects:];
```

## Instance methods

```
-[UITextSelectionRect setBaselineOffset:];
-[UITextSelectionRect _transform];
-[UITextSelectionRect baselineOffset];
-[UITextSelectionRect _highlightContainerLayer];
-[UITextSelectionRect range];
-[UITextSelectionRect isVertical];
-[UITextSelectionRect _path];
-[UITextSelectionRect transform];
-[UITextSelectionRect rect];
-[UITextSelectionRect containsStart];
-[UITextSelectionRect hash];
-[UITextSelectionRect _setTransform:];
-[UITextSelectionRect containsEnd];
-[UITextSelectionRect writingDirection];
-[UITextSelectionRect isEqual:];
-[UITextSelectionRect mutableCopy];
-[UITextSelectionRect _customHandleInfo];
-[UITextSelectionRect _drawsOwnHighlight];
-[UITextSelectionRect _isImpl];
-[UITextSelectionRect _appendToPath:cornerRadius:edgeInsets:];
-[UITextSelectionRect _endCustomSelectionPath];
-[UITextSelectionRect _endEdgeRect];
-[UITextSelectionRect _startCustomSelectionPath];
-[UITextSelectionRect _startEdgeRect];
```
