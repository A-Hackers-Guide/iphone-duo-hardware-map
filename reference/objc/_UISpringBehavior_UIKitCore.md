# `_UISpringBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 7 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIAttachmentBehavior" _topLeft;
@"UIAttachmentBehavior" _topRight;
@"UIAttachmentBehavior" _bottomRight;
@"UIAttachmentBehavior" _bottomLeft;
d _damping;
d _frequency;
{CGPoint="x"d"y"d} _anchorPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_anchorPoint) anchorPoint;
@property (Td,N,V_damping) damping;
@property (Td,N,V_frequency) frequency;
```

## Instance methods

```
-[_UISpringBehavior setDamping:];
-[_UISpringBehavior frequency];
-[_UISpringBehavior init];
-[_UISpringBehavior anchorPoint];
-[_UISpringBehavior damping];
-[_UISpringBehavior setFrequency:];
-[_UISpringBehavior setAnchorPoint:];
-[_UISpringBehavior initWithItem:anchorPoint:];
```
