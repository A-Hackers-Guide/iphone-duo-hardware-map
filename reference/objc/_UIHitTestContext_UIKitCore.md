# `_UIHitTestContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 2 class methods

## Instance variables

```
d _radius;
@"UIEvent" _event;
{CGPoint="x"d"y"d} _point;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_point) point;
@property (Td,R,N,V_radius) radius;
@property (T@"UIEvent",R,N,V_event) event;
```

## Class methods

```
+[_UIHitTestContext contextWithPoint:radius:event:];
+[_UIHitTestContext contextWithPoint:radius:];
```

## Instance methods

```
-[_UIHitTestContext initWithPoint:radius:event:];
-[_UIHitTestContext event];
-[_UIHitTestContext radius];
-[_UIHitTestContext point];
```
