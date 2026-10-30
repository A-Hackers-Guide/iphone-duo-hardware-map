# `_UIVisualEffectDifferenceEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
q _sourceCount;
q _destinationCount;
q _prefixCount;
q _suffixCount;
q _innerSourceCount;
q _innerDestinationCount;
^q _mergeTable;
@"NSArray" _merged;
@"NSArray" _source;
@"NSArray" _destination;
```

## Properties

```
@property (T@"NSArray",C,N,V_source) source;
@property (T@"NSArray",C,N,V_destination) destination;
@property (T@"NSArray",R,C,N) merged;
```

## Instance methods

```
-[_UIVisualEffectDifferenceEngine _reset];
-[_UIVisualEffectDifferenceEngine destination];
-[_UIVisualEffectDifferenceEngine _calculatePrefixAndSuffix];
-[_UIVisualEffectDifferenceEngine dealloc];
-[_UIVisualEffectDifferenceEngine _calculateMerge];
-[_UIVisualEffectDifferenceEngine setSource:];
-[_UIVisualEffectDifferenceEngine setDestination:];
-[_UIVisualEffectDifferenceEngine merged];
-[_UIVisualEffectDifferenceEngine description];
-[_UIVisualEffectDifferenceEngine _calculate];
-[_UIVisualEffectDifferenceEngine mergeSource:andDestination:];
-[_UIVisualEffectDifferenceEngine source];
-[_UIVisualEffectDifferenceEngine _calculateLCSSTable];
-[_UIVisualEffectDifferenceEngine describeMergeTable];
```
