# `SBGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 3 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
Q _gesturePhase;
@"NSUUID" _gestureID;
```

## Properties

```
@property (TQ,R,N,V_gesturePhase) gesturePhase;
@property (T@"NSUUID",R,N,V_gestureID) gestureID;
```

## Instance methods

```
-[SBGestureSwitcherModifier handleGestureEvent:];
-[SBGestureSwitcherModifier handleEvent:];
-[SBGestureSwitcherModifier maskedCornersForIndex:];
-[SBGestureSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBGestureSwitcherModifier handleTransitionEvent:];
-[SBGestureSwitcherModifier visibleMarginForItemContainerAtIndex:];
-[SBGestureSwitcherModifier isItemResizingAllowedForLayoutRole:inAppLayout:];
-[SBGestureSwitcherModifier isHitTestBlockingViewVisible];
-[SBGestureSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBGestureSwitcherModifier descriptionBuilderWithMultilinePrefix:];
-[SBGestureSwitcherModifier gestureID];
-[SBGestureSwitcherModifier gesturePhase];
-[SBGestureSwitcherModifier initWithGestureID:];
-[SBGestureSwitcherModifier isPreparingLayout];
-[SBGestureSwitcherModifier isUpdatingLayout];
-[SBGestureSwitcherModifier requireStripContentsInViewHierarchy];
```
