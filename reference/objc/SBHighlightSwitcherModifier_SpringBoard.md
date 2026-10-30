# `SBHighlightSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 6 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _layoutRole;
@"SBAppLayout" _appLayout;
@"SBAppLayout" _leafAppLayout;
Q _phase;
B _listensForHighlightEvents;
B _stylesCornerRadii;
```

## Properties

```
@property (TB,N,V_stylesCornerRadii) stylesCornerRadii;
```

## Instance methods

```
-[SBHighlightSwitcherModifier animationAttributesForLayoutElement:];
-[SBHighlightSwitcherModifier topMostLayoutElements];
-[SBHighlightSwitcherModifier shouldAccessoryDrawShadowForAppLayout:];
-[SBHighlightSwitcherModifier topMostLayoutRolesForAppLayout:];
-[SBHighlightSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBHighlightSwitcherModifier handleHighlightEvent:];
-[SBHighlightSwitcherModifier initWithLayoutRole:inAppLayout:listensForHighlightEvents:];
-[SBHighlightSwitcherModifier setStylesCornerRadii:];
-[SBHighlightSwitcherModifier stylesCornerRadii];
```
