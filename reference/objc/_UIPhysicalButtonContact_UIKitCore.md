# `_UIPhysicalButtonContact`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `BSDescriptionStreamable`
- 6 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _touching;
d _touchMajorRadius;
d _touchMinorRadius;
Q _touchPositionHints;
{CGPoint="x"d"y"d} _position;
{CGPoint="x"d"y"d} _positionDelta;
```

## Properties

```
@property (TB,R,N,GisTouching) touching;
@property (Td,R,N) touchMajorRadius;
@property (Td,R,N) touchMinorRadius;
@property (T{CGPoint=dd},R,N) position;
@property (T{CGPoint=dd},R,N) positionDelta;
@property (TQ,R,N) touchPositionHints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPhysicalButtonContact position];
-[_UIPhysicalButtonContact debugDescription];
-[_UIPhysicalButtonContact succinctDescriptionBuilder];
-[_UIPhysicalButtonContact init];
-[_UIPhysicalButtonContact appendDescriptionToFormatter:];
-[_UIPhysicalButtonContact descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonContact isTouching];
-[_UIPhysicalButtonContact succinctDescription];
-[_UIPhysicalButtonContact debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonContact description];
-[_UIPhysicalButtonContact descriptionBuilderWithMultilinePrefix:];
-[_UIPhysicalButtonContact positionDelta];
-[_UIPhysicalButtonContact touchMajorRadius];
-[_UIPhysicalButtonContact touchMinorRadius];
-[_UIPhysicalButtonContact touchPositionHints];
```
