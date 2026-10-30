# `SBWindowCommitSwitcherModifier`

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
-[SBWindowCommitSwitcherModifier scaleForIndex:];
-[SBWindowCommitSwitcherModifier anchorPointForIndex:];
-[SBWindowCommitSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBWindowCommitSwitcherModifier cornerRadiiForIndex:];
-[SBWindowCommitSwitcherModifier animationAttributesForLayoutElement:];
-[SBWindowCommitSwitcherModifier topMostLayoutElements];
-[SBWindowCommitSwitcherModifier titleAndIconOpacityForIndex:];
-[SBWindowCommitSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBWindowCommitSwitcherModifier visibleAppLayouts];
-[SBWindowCommitSwitcherModifier perspectiveAngleForIndex:];
-[SBWindowCommitSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBWindowCommitSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBWindowCommitSwitcherModifier frameForIndex:];
-[SBWindowCommitSwitcherModifier transitionWillBegin];
-[SBWindowCommitSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBWindowCommitSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBWindowCommitSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBWindowCommitSwitcherModifier appLayoutContainingAppLayout:];
-[SBWindowCommitSwitcherModifier initWithTransitionID:fromAppLayout:layoutRole:];
```
