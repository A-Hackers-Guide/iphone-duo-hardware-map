# `_UITextInputSessionDynamicAccumulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextInputSessionAccumulator`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _lastResults;
@? _dynamicAccumulatorIncreaseBlock;
```

## Properties

```
@property (T@?,C,N,V_dynamicAccumulatorIncreaseBlock) dynamicAccumulatorIncreaseBlock;
@property (T@"NSArray",R,N,V_lastResults) lastResults;
```

## Class methods

```
+[_UITextInputSessionDynamicAccumulator accumulatorWithName:depthRange:block:];
```

## Instance methods

```
-[_UITextInputSessionDynamicAccumulator lastResults];
-[_UITextInputSessionDynamicAccumulator setDynamicAccumulatorIncreaseBlock:];
-[_UITextInputSessionDynamicAccumulator increaseWithActions:];
-[_UITextInputSessionDynamicAccumulator enumerateAnalytics:];
-[_UITextInputSessionDynamicAccumulator dynamicAccumulatorIncreaseBlock];
```
