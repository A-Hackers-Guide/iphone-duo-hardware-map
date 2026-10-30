# `SBCoplanarSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 5 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _usesContainerViewBoundsAsActiveFrame;
d _scale;
q _spacingType;
@"SBAppLayout" _ignoredAppLayout;
@"SBAppLayout" _activeAppLayout;
```

## Properties

```
@property (Td,N,V_scale) scale;
@property (TB,N,V_usesContainerViewBoundsAsActiveFrame) usesContainerViewBoundsAsActiveFrame;
@property (Tq,N,V_spacingType) spacingType;
@property (T@"SBAppLayout",&,N,V_ignoredAppLayout) ignoredAppLayout;
```

## Instance methods

```
-[SBCoplanarSwitcherModifier scaleForIndex:];
-[SBCoplanarSwitcherModifier initWithActiveAppLayout:];
-[SBCoplanarSwitcherModifier frameForIndex:];
-[SBCoplanarSwitcherModifier setSpacingType:];
-[SBCoplanarSwitcherModifier setScale:];
-[SBCoplanarSwitcherModifier ignoredAppLayout];
-[SBCoplanarSwitcherModifier scale];
-[SBCoplanarSwitcherModifier _indexOfActiveAppLayout];
-[SBCoplanarSwitcherModifier _offscreenSpacing];
-[SBCoplanarSwitcherModifier spacingType];
-[SBCoplanarSwitcherModifier usesContainerViewBoundsAsActiveFrame];
-[SBCoplanarSwitcherModifier setUsesContainerViewBoundsAsActiveFrame:];
-[SBCoplanarSwitcherModifier setIgnoredAppLayout:];
```
