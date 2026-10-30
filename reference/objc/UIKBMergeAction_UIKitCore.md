# `UIKBMergeAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSString" _remainingKeyName;
@"NSString" _disappearingKeyName;
@"NSArray" _orderedKeyList;
@"UIKBGeometry" _factors;
```

## Properties

```
@property (T@"NSString",&,N,V_remainingKeyName) remainingKeyName;
@property (T@"NSString",&,N,V_disappearingKeyName) disappearingKeyName;
@property (T@"NSArray",&,N,V_orderedKeyList) orderedKeyList;
@property (T@"UIKBGeometry",&,N,V_factors) factors;
```

## Class methods

```
+[UIKBMergeAction mergeActionWithOrderedKeyList:factors:];
+[UIKBMergeAction mergeActionWithRemainingKeyName:disappearingKeyName:factors:];
```

## Instance methods

```
-[UIKBMergeAction factors];
-[UIKBMergeAction copyWithZone:];
-[UIKBMergeAction disappearingKeyName];
-[UIKBMergeAction orderedKeyList];
-[UIKBMergeAction remainingKeyName];
-[UIKBMergeAction setDisappearingKeyName:];
-[UIKBMergeAction setFactors:];
-[UIKBMergeAction setOrderedKeyList:];
-[UIKBMergeAction setRemainingKeyName:];
```
