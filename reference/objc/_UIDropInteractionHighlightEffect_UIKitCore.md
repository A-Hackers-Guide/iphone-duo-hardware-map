# `_UIDropInteractionHighlightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropInteractionEffect`
- 6 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _visualState;
d _highlightWidth;
d _cornerRadius;
d _highlightInset;
@"UIColor" _highlightColor;
@"CAShapeLayer" _shapeLayer;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_shapeLayer) shapeLayer;
@property (Td,N,V_highlightWidth) highlightWidth;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Td,N,V_highlightInset) highlightInset;
@property (T@"UIColor",C,N,V_highlightColor) highlightColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDropInteractionHighlightEffect shapeLayer];
-[_UIDropInteractionHighlightEffect init];
-[_UIDropInteractionHighlightEffect setShapeLayer:];
-[_UIDropInteractionHighlightEffect dealloc];
-[_UIDropInteractionHighlightEffect setHighlightColor:];
-[_UIDropInteractionHighlightEffect setCornerRadius:];
-[_UIDropInteractionHighlightEffect interaction:didChangeWithContext:];
-[_UIDropInteractionHighlightEffect cornerRadius];
-[_UIDropInteractionHighlightEffect highlightColor];
-[_UIDropInteractionHighlightEffect clippingRectInView:forView:];
-[_UIDropInteractionHighlightEffect highlightInset];
-[_UIDropInteractionHighlightEffect highlightRectInView:forDragInteraction:withContext:];
-[_UIDropInteractionHighlightEffect highlightWidth];
-[_UIDropInteractionHighlightEffect removeShapeLayer];
-[_UIDropInteractionHighlightEffect setHighlightInset:];
-[_UIDropInteractionHighlightEffect setHighlightWidth:];
-[_UIDropInteractionHighlightEffect updateShapeLayerForFrame:inView:];
```
