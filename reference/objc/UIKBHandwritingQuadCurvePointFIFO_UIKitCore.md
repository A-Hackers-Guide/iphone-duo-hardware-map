# `UIKBHandwritingQuadCurvePointFIFO`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBHandwritingPointFIFO`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@? _emissionHandler;
d _scale;
@"NSMutableArray" _prevPoints;
{?="point"{CGPoint="x"d"y"d}"force"d} _lastPoint;
```

## Properties

```
@property (Td,N,V_scale) scale;
@property (T@"NSMutableArray",&,N,V_prevPoints) prevPoints;
@property (T{?={CGPoint=dd}d},N,V_lastPoint) lastPoint;
@property (T@?,C,V_emissionHandler) emissionHandler;
```

## Instance methods

```
-[UIKBHandwritingQuadCurvePointFIFO clear];
-[UIKBHandwritingQuadCurvePointFIFO flush];
-[UIKBHandwritingQuadCurvePointFIFO setScale:];
-[UIKBHandwritingQuadCurvePointFIFO scale];
-[UIKBHandwritingQuadCurvePointFIFO emissionHandler];
-[UIKBHandwritingQuadCurvePointFIFO addPoint:];
-[UIKBHandwritingQuadCurvePointFIFO initWithFIFO:scale:];
-[UIKBHandwritingQuadCurvePointFIFO lastPoint];
-[UIKBHandwritingQuadCurvePointFIFO prevPoints];
-[UIKBHandwritingQuadCurvePointFIFO setEmissionHandler:];
-[UIKBHandwritingQuadCurvePointFIFO setLastPoint:];
-[UIKBHandwritingQuadCurvePointFIFO setPrevPoints:];
```
