# `UIKBHandwritingBoxcarFilterPointFIFO`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBHandwritingPointFIFO`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _prevPoints;
Q _width;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_prevPoints) prevPoints;
@property (TQ,N,V_width) width;
```

## Instance methods

```
-[UIKBHandwritingBoxcarFilterPointFIFO clear];
-[UIKBHandwritingBoxcarFilterPointFIFO flush];
-[UIKBHandwritingBoxcarFilterPointFIFO setWidth:];
-[UIKBHandwritingBoxcarFilterPointFIFO width];
-[UIKBHandwritingBoxcarFilterPointFIFO addPoint:];
-[UIKBHandwritingBoxcarFilterPointFIFO emitAveragedPoint];
-[UIKBHandwritingBoxcarFilterPointFIFO initWithFIFO:width:];
-[UIKBHandwritingBoxcarFilterPointFIFO prevPoints];
-[UIKBHandwritingBoxcarFilterPointFIFO setPrevPoints:];
```
