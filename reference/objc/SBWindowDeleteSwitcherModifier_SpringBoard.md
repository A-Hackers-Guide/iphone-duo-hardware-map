# `SBWindowDeleteSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 8 instance variables, 1 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
q _layoutRole;
@"SBAppLayout" _centerWindowAppLayout;
@"SBAppLayout" _fullScreenAppLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _initialCornerRadii;
B _supportsGroupOpacity;
B _usePageFullScreenCenterWindowDeletion;
```

## Properties

```
@property (TB,N,V_usePageFullScreenCenterWindowDeletion) usePageFullScreenCenterWindowDeletion;
```

## Instance methods

```
-[SBWindowDeleteSwitcherModifier scaleForIndex:];
-[SBWindowDeleteSwitcherModifier anchorPointForIndex:];
-[SBWindowDeleteSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBWindowDeleteSwitcherModifier cornerRadiiForIndex:];
-[SBWindowDeleteSwitcherModifier animationAttributesForLayoutElement:];
-[SBWindowDeleteSwitcherModifier topMostLayoutElements];
-[SBWindowDeleteSwitcherModifier isSwitcherWindowVisible];
-[SBWindowDeleteSwitcherModifier titleAndIconOpacityForIndex:];
-[SBWindowDeleteSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBWindowDeleteSwitcherModifier transitionWillUpdate];
-[SBWindowDeleteSwitcherModifier visibleAppLayouts];
-[SBWindowDeleteSwitcherModifier perspectiveAngleForIndex:];
-[SBWindowDeleteSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBWindowDeleteSwitcherModifier transitionDidEnd];
-[SBWindowDeleteSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBWindowDeleteSwitcherModifier frameForIndex:];
-[SBWindowDeleteSwitcherModifier transitionWillBegin];
-[SBWindowDeleteSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBWindowDeleteSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBWindowDeleteSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBWindowDeleteSwitcherModifier shouldAllowGroupOpacityForAppLayout:];
-[SBWindowDeleteSwitcherModifier _centerOfCenterPageFullScreenAssociatedSourceDisplayItem:appLayout:];
-[SBWindowDeleteSwitcherModifier appLayoutContainingAppLayout:];
-[SBWindowDeleteSwitcherModifier initWithTransitionID:fromAppLayout:layoutRole:];
-[SBWindowDeleteSwitcherModifier setUsePageFullScreenCenterWindowDeletion:];
-[SBWindowDeleteSwitcherModifier usePageFullScreenCenterWindowDeletion];
```
