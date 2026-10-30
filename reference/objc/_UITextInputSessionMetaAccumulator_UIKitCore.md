# `_UITextInputSessionMetaAccumulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextInputSessionAccumulator`
- 3 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _accumulators;
q _lastSuccessfulIndex;
Q _actionCountWithoutIncrease;
```

## Class methods

```
+[_UITextInputSessionMetaAccumulator accumulatorWithName:accumulators:];
```

## Instance methods

```
-[_UITextInputSessionMetaAccumulator reset];
-[_UITextInputSessionMetaAccumulator increaseWithActions:];
-[_UITextInputSessionMetaAccumulator copyWithZone:];
```
