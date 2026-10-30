# `SBAppExposeToFullScreenSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 8 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBAppLayout" _fullScreenAppLayout;
@"NSString" _bundleIdentifier;
@"SBAppExposeGridSwitcherModifier" _appExposeModifier;
@"SBSwitcherModifier" _fullscreenModifier;
@"SBRouteToAppExposeSwitcherModifier" _routeToAppExposeModifier;
B _isSimulatingPreTransitionState;
@"NSArray" _appLayoutsBeforeTransition;
```

## Instance methods

```
-[SBAppExposeToFullScreenSwitcherModifier scaleForIndex:];
-[SBAppExposeToFullScreenSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBAppExposeToFullScreenSwitcherModifier appLayouts];
-[SBAppExposeToFullScreenSwitcherModifier visibleAppLayouts];
-[SBAppExposeToFullScreenSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBAppExposeToFullScreenSwitcherModifier transitionDidEnd];
-[SBAppExposeToFullScreenSwitcherModifier frameForIndex:];
-[SBAppExposeToFullScreenSwitcherModifier transitionWillBegin];
-[SBAppExposeToFullScreenSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBAppExposeToFullScreenSwitcherModifier _isEffectivelyFullScreen];
-[SBAppExposeToFullScreenSwitcherModifier plusButtonAlpha];
-[SBAppExposeToFullScreenSwitcherModifier _isIndexActive:];
-[SBAppExposeToFullScreenSwitcherModifier _newAppExposeModifier];
-[SBAppExposeToFullScreenSwitcherModifier _performBlockBySimulatingPreTransitionState:];
-[SBAppExposeToFullScreenSwitcherModifier initWithTransitionID:direction:fullScreenAppLayout:bundleIdentifier:appExposeModifier:fullScreenModifier:];
```
