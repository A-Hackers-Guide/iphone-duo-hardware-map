# `SBWindowDeclineSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
q _layoutRole;
@"SBAppLayout" _centerWindowAppLayout;
@"SBAppLayout" _fullScreenAppLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _initialCornerRadii;
```

## Instance methods

```
-[SBWindowDeclineSwitcherModifier scaleForIndex:];
-[SBWindowDeclineSwitcherModifier anchorPointForIndex:];
-[SBWindowDeclineSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBWindowDeclineSwitcherModifier cornerRadiiForIndex:];
-[SBWindowDeclineSwitcherModifier animationAttributesForLayoutElement:];
-[SBWindowDeclineSwitcherModifier topMostLayoutElements];
-[SBWindowDeclineSwitcherModifier titleAndIconOpacityForIndex:];
-[SBWindowDeclineSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBWindowDeclineSwitcherModifier visibleAppLayouts];
-[SBWindowDeclineSwitcherModifier perspectiveAngleForIndex:];
-[SBWindowDeclineSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBWindowDeclineSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBWindowDeclineSwitcherModifier frameForIndex:];
-[SBWindowDeclineSwitcherModifier transitionWillBegin];
-[SBWindowDeclineSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBWindowDeclineSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBWindowDeclineSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBWindowDeclineSwitcherModifier appLayoutContainingAppLayout:];
-[SBWindowDeclineSwitcherModifier initWithTransitionID:fromAppLayout:layoutRole:];
```
