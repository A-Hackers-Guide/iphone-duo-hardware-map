# `SBSwitcherCoordinatedLayoutStateTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 11 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _displayItems;
@"SBSwitcherController" _fromSwitcherController;
@"SBSwitcherController" _toSwitcherController;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
q _fromFloatingConfiguration;
q _fromCenterConfiguration;
```

## Properties

```
@property (Tq,R,N,V_fromFloatingConfiguration) fromFloatingConfiguration;
@property (Tq,R,N,V_fromCenterConfiguration) fromCenterConfiguration;
@property (T@"NSSet",R,C,N,V_displayItems) displayItems;
@property (T@"SBSwitcherController",R,N,V_fromSwitcherController) fromSwitcherController;
@property (T@"SBSwitcherController",R,N,V_toSwitcherController) toSwitcherController;
@property (T@"SBAppLayout",R,N,V_fromAppLayout) fromAppLayout;
@property (T@"SBAppLayout",R,N,V_toAppLayout) toAppLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:fromSwitcherController:toSwitcherController:fromAppLayout:toAppLayout:withApplicationController:];
```

## Instance methods

```
-[SBSwitcherCoordinatedLayoutStateTransitionContext displayItems];
-[SBSwitcherCoordinatedLayoutStateTransitionContext succinctDescriptionBuilder];
-[SBSwitcherCoordinatedLayoutStateTransitionContext descriptionWithMultilinePrefix:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromAppLayout];
-[SBSwitcherCoordinatedLayoutStateTransitionContext succinctDescription];
-[SBSwitcherCoordinatedLayoutStateTransitionContext hash];
-[SBSwitcherCoordinatedLayoutStateTransitionContext description];
-[SBSwitcherCoordinatedLayoutStateTransitionContext toAppLayout];
-[SBSwitcherCoordinatedLayoutStateTransitionContext isEqual:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext descriptionBuilderWithMultilinePrefix:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromCenterConfiguration];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromFloatingConfiguration];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromFrameInFromSwitcherForDisplayItem:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromFrameInToSwitcherForDisplayItem:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext fromSwitcherController];
-[SBSwitcherCoordinatedLayoutStateTransitionContext hasTransitioningDisplayItemsForAppLayout:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext hasTransitioningDisplayItemsForSwitcherController:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext initWithDisplayItems:fromSwitcherController:toSwitcherController:fromAppLayout:toAppLayout:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext isDisplayItemTransitioning:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext toFrameInFromSwitcherForDisplayItem:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext toFrameInToSwitcherForDisplayItem:];
-[SBSwitcherCoordinatedLayoutStateTransitionContext toSwitcherController];
```
