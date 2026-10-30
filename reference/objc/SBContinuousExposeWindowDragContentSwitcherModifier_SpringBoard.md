# `SBContinuousExposeWindowDragContentSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 7 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _initialAppLayout;
@"NSUUID" _gestureID;
B _wantsSlideOverTongue;
Q _slideOverTongueState;
Q _slideOverTongueDirection;
@"SBFlexibleWindowingWindowDragSwitcherModifier" _gestureModifier;
@"SBDisplayItem" _selectedDisplayItem;
```

## Properties

```
@property (T@"SBDisplayItem",R,N,V_selectedDisplayItem) selectedDisplayItem;
@property (TB,R,N,V_wantsSlideOverTongue) wantsSlideOverTongue;
@property (TQ,R,N,V_slideOverTongueState) slideOverTongueState;
@property (TQ,R,N,V_slideOverTongueDirection) slideOverTongueDirection;
@property (T@"SBFlexibleWindowingWindowDragSwitcherModifier",R,N,V_gestureModifier) gestureModifier;
```

## Instance methods

```
-[SBContinuousExposeWindowDragContentSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBContinuousExposeWindowDragContentSwitcherModifier wantsSlideOverTongue];
-[SBContinuousExposeWindowDragContentSwitcherModifier setDelegate:];
-[SBContinuousExposeWindowDragContentSwitcherModifier slideOverTongueDirection];
-[SBContinuousExposeWindowDragContentSwitcherModifier slideOverTongueState];
-[SBContinuousExposeWindowDragContentSwitcherModifier gestureModifier];
-[SBContinuousExposeWindowDragContentSwitcherModifier _createFloorAndMultitaskingModifiersWithAppLayout:];
-[SBContinuousExposeWindowDragContentSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:];
-[SBContinuousExposeWindowDragContentSwitcherModifier selectedDisplayItem];
-[SBContinuousExposeWindowDragContentSwitcherModifier updateFloorModifiersWithAppLayout:];
```
