# `SBButterflyDeckToAppExposeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 9 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBWindowingModifier" _deckModifier;
@"SBDeckRegionModel" _fromDeckRegionModel;
@"SBDeckRegionModel" _toDeckRegionModel;
@"NSSet" _fromVisibleItems;
@"NSArray" _fromTopMostItems;
@"NSMapTable" _fromFrames;
@"SBAppLayout" _steadyAppLayout;
@"NSString" _bundleID;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
```

## Instance methods

```
-[SBButterflyDeckToAppExposeWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyDeckToAppExposeWindowingModifier transitionDidUpdate:];
-[SBButterflyDeckToAppExposeWindowingModifier transitionWillBegin:];
-[SBButterflyDeckToAppExposeWindowingModifier visibleItems];
-[SBButterflyDeckToAppExposeWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyDeckToAppExposeWindowingModifier animationAttributesForItem:];
-[SBButterflyDeckToAppExposeWindowingModifier opacityForItem:];
-[SBButterflyDeckToAppExposeWindowingModifier bundleID];
-[SBButterflyDeckToAppExposeWindowingModifier topMostItems];
-[SBButterflyDeckToAppExposeWindowingModifier frameForItem:];
-[SBButterflyDeckToAppExposeWindowingModifier deckRegionModel];
-[SBButterflyDeckToAppExposeWindowingModifier initWithBundleID:deckModifier:];
-[SBButterflyDeckToAppExposeWindowingModifier shouldInterruptForActivity:];
-[SBButterflyDeckToAppExposeWindowingModifier transitionDidComplete:];
```
