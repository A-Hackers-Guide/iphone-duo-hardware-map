# `SBAppExposeGridSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 10 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _previousContentOffset;
B _isScrollingForward;
@"SBMixedGridSwitcherModifier" _mixedGridModifier;
Q _numberOfHiddenAppLayouts;
B _isShowingReopenClosedWindowsButton;
B _reversesFloatingCardDirection;
B _disableFullScreenCardScaleRounding;
@"NSString" _bundleIdentifier;
{CGSize="width"d"height"d} _fullScreenCardSize;
{CGSize="width"d"height"d} _floatingCardSize;
```

## Properties

```
@property (TB,N,V_disableFullScreenCardScaleRounding) disableFullScreenCardScaleRounding;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T{CGSize=dd},R,N,V_fullScreenCardSize) fullScreenCardSize;
@property (T{CGSize=dd},R,N,V_floatingCardSize) floatingCardSize;
@property (TB,N,V_reversesFloatingCardDirection) reversesFloatingCardDirection;
```

## Instance methods

```
-[SBAppExposeGridSwitcherModifier didMoveToParentModifier:];
-[SBAppExposeGridSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBAppExposeGridSwitcherModifier handleTransitionEvent:];
-[SBAppExposeGridSwitcherModifier handleTimerEvent:];
-[SBAppExposeGridSwitcherModifier reopenClosedWindowsButtonAlpha];
-[SBAppExposeGridSwitcherModifier plusButtonStyle];
-[SBAppExposeGridSwitcherModifier bundleIdentifier];
-[SBAppExposeGridSwitcherModifier appLayoutToScrollToBeforeReopeningClosedWindows];
-[SBAppExposeGridSwitcherModifier appExposeAccessoryButtonsBundleIdentifier];
-[SBAppExposeGridSwitcherModifier handleRemovalEvent:];
-[SBAppExposeGridSwitcherModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:];
-[SBAppExposeGridSwitcherModifier reopenClosedWindowsButtonScale];
-[SBAppExposeGridSwitcherModifier copyWithZone:];
-[SBAppExposeGridSwitcherModifier plusButtonAlpha];
-[SBAppExposeGridSwitcherModifier appExposeAccessoryButtonsOverrideUserInterfaceStyle];
-[SBAppExposeGridSwitcherModifier isLayoutRoleDraggable:inAppLayout:];
-[SBAppExposeGridSwitcherModifier _canShowReopenClosedWindowsButton];
-[SBAppExposeGridSwitcherModifier _updateReopenClosedWindowsButtonPresence];
-[SBAppExposeGridSwitcherModifier disableFullScreenCardScaleRounding];
-[SBAppExposeGridSwitcherModifier floatingCardSize];
-[SBAppExposeGridSwitcherModifier fullScreenCardSize];
-[SBAppExposeGridSwitcherModifier handleInsertionEvent:];
-[SBAppExposeGridSwitcherModifier initWithBundleIdentifier:fullScreenCardSize:floatingCardSize:];
-[SBAppExposeGridSwitcherModifier reversesFloatingCardDirection];
-[SBAppExposeGridSwitcherModifier setDisableFullScreenCardScaleRounding:];
-[SBAppExposeGridSwitcherModifier setReversesFloatingCardDirection:];
```
