# `UIKBHandwritingBezierPathPointFIFO`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBHandwritingPointFIFO`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIBezierPath" _path;
@? _emissionHandler;
@"NSMutableArray" _prevPoints;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_prevPoints) prevPoints;
@property (T@"UIBezierPath",&,N,V_path) path;
@property (T@?,C,V_emissionHandler) emissionHandler;
```

## Instance methods

```
-[UIKBHandwritingBezierPathPointFIFO clear];
-[UIKBHandwritingBezierPathPointFIFO flush];
-[UIKBHandwritingBezierPathPointFIFO setPath:];
-[UIKBHandwritingBezierPathPointFIFO path];
-[UIKBHandwritingBezierPathPointFIFO emissionHandler];
-[UIKBHandwritingBezierPathPointFIFO addPoint:];
-[UIKBHandwritingBezierPathPointFIFO initWithFIFO:];
-[UIKBHandwritingBezierPathPointFIFO prevPoints];
-[UIKBHandwritingBezierPathPointFIFO setEmissionHandler:];
-[UIKBHandwritingBezierPathPointFIFO setPrevPoints:];
```
