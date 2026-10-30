# `_UIKBRTDecayingOffset`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKBRTDecayingObject`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _limitMovement;
{CGPoint="x"d"y"d} _offset;
```

## Properties

```
@property (T{CGPoint=dd},R,N) offset;
@property (T{CGPoint=dd},R,N) originalOffset;
```

## Instance methods

```
-[_UIKBRTDecayingOffset reset];
-[_UIKBRTDecayingOffset offset];
-[_UIKBRTDecayingOffset updateOffsetTo:];
-[_UIKBRTDecayingOffset initWithTimeoutDuration:limitMovement:];
-[_UIKBRTDecayingOffset originalOffset];
```
