# `SBContinuousExposeIdentifiersChangedModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _gestureInitiated;
@"NSArray" _previousContinuousExposeIdentifiersInSwitcher;
@"NSArray" _previousContinuousExposeIdentifiersInStrip;
@"SBAppLayout" _transitioningFromAppLayout;
@"SBAppLayout" _transitioningToAppLayout;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_previousContinuousExposeIdentifiersInSwitcher) previousContinuousExposeIdentifiersInSwitcher;
@property (T@"NSArray",R,C,N,V_previousContinuousExposeIdentifiersInStrip) previousContinuousExposeIdentifiersInStrip;
@property (T@"SBAppLayout",R,N,V_transitioningFromAppLayout) transitioningFromAppLayout;
@property (T@"SBAppLayout",R,N,V_transitioningToAppLayout) transitioningToAppLayout;
@property (TB,R,N,GisAnimated,V_animated) animated;
@property (TB,R,N,GisGestureInitiated,V_gestureInitiated) gestureInitiated;
```

## Instance methods

```
-[SBContinuousExposeIdentifiersChangedModifierEvent transitioningToAppLayout];
-[SBContinuousExposeIdentifiersChangedModifierEvent isAnimated];
-[SBContinuousExposeIdentifiersChangedModifierEvent transitioningFromAppLayout];
-[SBContinuousExposeIdentifiersChangedModifierEvent isGestureInitiated];
-[SBContinuousExposeIdentifiersChangedModifierEvent type];
-[SBContinuousExposeIdentifiersChangedModifierEvent copyWithZone:];
-[SBContinuousExposeIdentifiersChangedModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBContinuousExposeIdentifiersChangedModifierEvent initWithPreviousContinuousExposeIdentifiersInSwitcher:previousContinuousExposeIdentifiersInStrip:transitioningFromAppLayout:transitioningToAppLayout:animated:gestureInitiated:];
-[SBContinuousExposeIdentifiersChangedModifierEvent previousContinuousExposeIdentifiersInStrip];
-[SBContinuousExposeIdentifiersChangedModifierEvent previousContinuousExposeIdentifiersInSwitcher];
```
