# `SBMixedGridToFullScreenSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBAppLayout" _fullScreenAppLayout;
@"SBAppLayout" _floatingAppLayout;
@"SBSwitcherModifier<SBMixedGridSwitcherProviding>" _mixedGridModifier;
@"SBSwitcherModifier" _fullscreenModifier;
@"SBRouteToMixedGridSwitcherModifier" _routeToMixedGridModifier;
@"NSArray" _appLayoutsBeforeTransition;
```

## Instance methods

```
-[SBMixedGridToFullScreenSwitcherModifier scaleForIndex:];
-[SBMixedGridToFullScreenSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBMixedGridToFullScreenSwitcherModifier topMostLayoutElements];
-[SBMixedGridToFullScreenSwitcherModifier visibleAppLayouts];
-[SBMixedGridToFullScreenSwitcherModifier transitionDidEnd];
-[SBMixedGridToFullScreenSwitcherModifier frameForIndex:];
-[SBMixedGridToFullScreenSwitcherModifier transitionWillBegin];
-[SBMixedGridToFullScreenSwitcherModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:];
-[SBMixedGridToFullScreenSwitcherModifier blurViewIconScaleForIndex:];
-[SBMixedGridToFullScreenSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBMixedGridToFullScreenSwitcherModifier _isEffectivelyFullScreen];
-[SBMixedGridToFullScreenSwitcherModifier appLayoutToScrollToBeforeTransitioning];
-[SBMixedGridToFullScreenSwitcherModifier isLayoutRoleDraggable:inAppLayout:];
-[SBMixedGridToFullScreenSwitcherModifier _isIndexActive:];
-[SBMixedGridToFullScreenSwitcherModifier _appLayoutToScrollTo];
-[SBMixedGridToFullScreenSwitcherModifier _firstFloatingAppLayout:];
-[SBMixedGridToFullScreenSwitcherModifier _newMixedGridModifier];
-[SBMixedGridToFullScreenSwitcherModifier _performBlockWhileSimulatingPostPresentationScrollViewContentOffset:];
-[SBMixedGridToFullScreenSwitcherModifier initWithTransitionID:direction:fullScreenAppLayout:gridModifier:fullScreenModifier:];
```
