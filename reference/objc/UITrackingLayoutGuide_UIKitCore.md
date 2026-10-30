# `UITrackingLayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- 14 instance variables, 16 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _constrainedToWindowGuide;
B _animatingConstraintsChange;
B _animatesChanges;
B _skipAnimationOnNextPassOnly;
@"NSMutableDictionary" _nearEdgeConstraintsByEdge;
@"NSMutableDictionary" _awayFromConstraintsByEdge;
Q _overlappingEdges;
Q _pausedEdges;
d _animationDuration;
Q _animationOptions;
q _owningViewInterfaceLayoutDirection;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _triggerInsetsForPortrait;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _triggerInsetsForLandscape;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _triggerProportions;
```

## Properties

```
@property (TB,N) constrainedToWindowGuide;
@property (T@"NSDictionary",R,N) edgeConstraints;
@property (T@"NSMutableDictionary",&,N,V_nearEdgeConstraintsByEdge) nearEdgeConstraintsByEdge;
@property (T@"NSMutableDictionary",&,N,V_awayFromConstraintsByEdge) awayFromConstraintsByEdge;
@property (TB,N,V_constrainedToWindowGuide) constrainedToWindowGuide;
@property (T{UIEdgeInsets=dddd},N,V_triggerInsetsForPortrait) triggerInsetsForPortrait;
@property (T{UIEdgeInsets=dddd},N,V_triggerInsetsForLandscape) triggerInsetsForLandscape;
@property (T{UIEdgeInsets=dddd},N,V_triggerProportions) triggerProportions;
@property (TQ,N,V_overlappingEdges) overlappingEdges;
@property (TQ,N,V_pausedEdges) pausedEdges;
@property (Td,N,V_animationDuration) animationDuration;
@property (TQ,N,V_animationOptions) animationOptions;
@property (TB,N,V_animatingConstraintsChange) animatingConstraintsChange;
@property (TB,N,V_animatesChanges) animatesChanges;
@property (TB,N,V_skipAnimationOnNextPassOnly) skipAnimationOnNextPassOnly;
@property (Tq,N,V_owningViewInterfaceLayoutDirection) owningViewInterfaceLayoutDirection;
```

## Instance methods

```
-[UITrackingLayoutGuide _layoutOwningViewAnimated:];
-[UITrackingLayoutGuide pauseUpdatingConstraintsForEdges:];
-[UITrackingLayoutGuide setAnimatingConstraintsChange:];
-[UITrackingLayoutGuide enableAnimations:];
-[UITrackingLayoutGuide updateConstraintsForActiveEdges];
-[UITrackingLayoutGuide setTriggerInsetsForLandscape:];
-[UITrackingLayoutGuide constraintsActiveWhenNearEdge:];
-[UITrackingLayoutGuide setConstraints:activeWhenNearEdge:];
-[UITrackingLayoutGuide setEdgeThresholds:forOrientation:];
-[UITrackingLayoutGuide trackConstraintsFromViewBasedGuide:];
-[UITrackingLayoutGuide triggerInsetsForPortrait];
-[UITrackingLayoutGuide pausedEdges];
-[UITrackingLayoutGuide startUpdatingConstraintsForEdges:];
-[UITrackingLayoutGuide setNearEdgeConstraintsByEdge:];
-[UITrackingLayoutGuide _awayFromCombinedTrackedConstraintsForEdgeKey:];
-[UITrackingLayoutGuide constrainedToWindowGuide];
-[UITrackingLayoutGuide setTriggerInsetsForPortrait:];
-[UITrackingLayoutGuide overlappingEdges];
-[UITrackingLayoutGuide _keysFromEdges:];
-[UITrackingLayoutGuide owningViewInterfaceLayoutDirection];
-[UITrackingLayoutGuide animationOptions];
-[UITrackingLayoutGuide triggerInsetsForLandscape];
-[UITrackingLayoutGuide _isRTL];
-[UITrackingLayoutGuide skipAnimationOnNextPassOnly];
-[UITrackingLayoutGuide updateAnimationDuration:options:];
-[UITrackingLayoutGuide nearEdgeConstraintsByEdge];
-[UITrackingLayoutGuide _thresholdCheckForGuide:inContext:];
-[UITrackingLayoutGuide removeTrackedConstraintsFromViewBasedGuide:];
-[UITrackingLayoutGuide setAnimationOptions:];
-[UITrackingLayoutGuide setAnimationDuration:];
-[UITrackingLayoutGuide animatingConstraintsChange];
-[UITrackingLayoutGuide awayFromConstraintsByEdge];
-[UITrackingLayoutGuide validatedOverlappingEdges:];
-[UITrackingLayoutGuide changeSizingConstants:];
-[UITrackingLayoutGuide setAnimatesChanges:];
-[UITrackingLayoutGuide setOverlappingEdges:];
-[UITrackingLayoutGuide _createThresholdsFromProportions];
-[UITrackingLayoutGuide animatesChanges];
-[UITrackingLayoutGuide changeOffsetConstants:];
-[UITrackingLayoutGuide setOwningViewInterfaceLayoutDirection:];
-[UITrackingLayoutGuide removeAllTrackedConstraints];
-[UITrackingLayoutGuide setProportionalEdgeThresholds:];
-[UITrackingLayoutGuide triggerProportions];
-[UITrackingLayoutGuide setConstraints:activeWhenAwayFromEdge:];
-[UITrackingLayoutGuide setAwayFromConstraintsByEdge:];
-[UITrackingLayoutGuide setSkipAnimationOnNextPassOnly:];
-[UITrackingLayoutGuide resetAnimationOptions];
-[UITrackingLayoutGuide setConstrainedToWindowGuide:];
-[UITrackingLayoutGuide edgeConstraints];
-[UITrackingLayoutGuide setTriggerProportions:];
-[UITrackingLayoutGuide constraintsActiveWhenAwayFromEdge:];
-[UITrackingLayoutGuide _nearEdgeCombinedTrackedConstraintsForEdgeKey:];
-[UITrackingLayoutGuide _setOwningView:];
-[UITrackingLayoutGuide _keysInvolvingEdges:];
-[UITrackingLayoutGuide _updateForOverlappingEdges:];
-[UITrackingLayoutGuide setPausedEdges:];
-[UITrackingLayoutGuide _thresholdCheck];
-[UITrackingLayoutGuide stopTrackingConstraintsForEdge:];
-[UITrackingLayoutGuide animationDuration];
-[UITrackingLayoutGuide init];
```
