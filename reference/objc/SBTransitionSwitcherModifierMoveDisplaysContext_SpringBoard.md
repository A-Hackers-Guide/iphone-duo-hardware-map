# `SBTransitionSwitcherModifierMoveDisplaysContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"SBSwitcherCoordinatedLayoutStateTransitionContext" _coordinatedLayoutStateTransitionContext;
@"SBSwitcherController" _switcherController;
```

## Properties

```
@property (T@"SBSwitcherCoordinatedLayoutStateTransitionContext",R,W,N,V_coordinatedLayoutStateTransitionContext) coordinatedLayoutStateTransitionContext;
@property (T@"SBSwitcherController",R,W,N,V_switcherController) switcherController;
@property (T@"NSSet",R,C,N) movingDisplayItems;
```

## Class methods

```
+[SBTransitionSwitcherModifierMoveDisplaysContext moveDisplaysContextWithCoordinatedLayoutStateTransitionContext:relativeToSwitcherController:];
```

## Instance methods

```
-[SBTransitionSwitcherModifierMoveDisplaysContext switcherController];
-[SBTransitionSwitcherModifierMoveDisplaysContext coordinatedLayoutStateTransitionContext];
-[SBTransitionSwitcherModifierMoveDisplaysContext fromFrameForDisplayItem:];
-[SBTransitionSwitcherModifierMoveDisplaysContext initWithCoordinatedLayoutStateTransitionContext:switcherController:];
-[SBTransitionSwitcherModifierMoveDisplaysContext movingDisplayItems];
-[SBTransitionSwitcherModifierMoveDisplaysContext pertainsToAppLayout:];
-[SBTransitionSwitcherModifierMoveDisplaysContext pertainsToDisplayItem:];
-[SBTransitionSwitcherModifierMoveDisplaysContext toFrameForDisplayItem:];
```
