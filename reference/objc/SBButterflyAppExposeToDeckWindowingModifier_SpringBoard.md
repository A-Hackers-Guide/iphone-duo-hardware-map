# `SBButterflyAppExposeToDeckWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 8 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBDeckRegionModel" _fromDeckRegionModel;
@"NSSet" _fromVisibleItems;
@"NSSet" _toVisibleItems;
@"NSMapTable" _toVisibleItemFrames;
@"NSMutableArray" _toTopMostItems;
{CGPoint="x"d"y"d} _toDeckScrollOffset;
B _shouldOverrideScrollOffset;
```

## Instance methods

```
-[SBButterflyAppExposeToDeckWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyAppExposeToDeckWindowingModifier transitionDidUpdate:];
-[SBButterflyAppExposeToDeckWindowingModifier transitionWillBegin:];
-[SBButterflyAppExposeToDeckWindowingModifier visibleItems];
-[SBButterflyAppExposeToDeckWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyAppExposeToDeckWindowingModifier animationAttributesForItem:];
-[SBButterflyAppExposeToDeckWindowingModifier opacityForItem:];
-[SBButterflyAppExposeToDeckWindowingModifier topMostItems];
-[SBButterflyAppExposeToDeckWindowingModifier frameForItem:];
-[SBButterflyAppExposeToDeckWindowingModifier scrollViewContentOffset];
-[SBButterflyAppExposeToDeckWindowingModifier shouldInterruptForActivity:];
-[SBButterflyAppExposeToDeckWindowingModifier transitionDidComplete:];
```
