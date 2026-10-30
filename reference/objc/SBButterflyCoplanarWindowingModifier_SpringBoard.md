# `SBButterflyCoplanarWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 7 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _activeAppLayout;
B _usesContainerViewBoundsAsActiveFrame;
B _readsActiveAppLayoutFromContext;
d _scale;
q _spacingType;
q _screenRegion;
@"NSSet" _ignoredAppLayouts;
```

## Properties

```
@property (Td,N,V_scale) scale;
@property (TB,N,V_usesContainerViewBoundsAsActiveFrame) usesContainerViewBoundsAsActiveFrame;
@property (Tq,N,V_spacingType) spacingType;
@property (Tq,N,V_screenRegion) screenRegion;
@property (TB,N,V_readsActiveAppLayoutFromContext) readsActiveAppLayoutFromContext;
@property (T@"NSSet",&,N,V_ignoredAppLayouts) ignoredAppLayouts;
```

## Instance methods

```
-[SBButterflyCoplanarWindowingModifier initWithActiveAppLayout:];
-[SBButterflyCoplanarWindowingModifier setSpacingType:];
-[SBButterflyCoplanarWindowingModifier setScale:];
-[SBButterflyCoplanarWindowingModifier scale];
-[SBButterflyCoplanarWindowingModifier spacingType];
-[SBButterflyCoplanarWindowingModifier usesContainerViewBoundsAsActiveFrame];
-[SBButterflyCoplanarWindowingModifier setUsesContainerViewBoundsAsActiveFrame:];
-[SBButterflyCoplanarWindowingModifier frameForItem:];
-[SBButterflyCoplanarWindowingModifier readsActiveAppLayoutFromContext];
-[SBButterflyCoplanarWindowingModifier _effectiveActiveAppLayout];
-[SBButterflyCoplanarWindowingModifier _effectiveContainerViewBounds];
-[SBButterflyCoplanarWindowingModifier _offscreenSpacingInDirection:];
-[SBButterflyCoplanarWindowingModifier _outOfBoundsSpacing];
-[SBButterflyCoplanarWindowingModifier ignoredAppLayouts];
-[SBButterflyCoplanarWindowingModifier screenRegion];
-[SBButterflyCoplanarWindowingModifier setIgnoredAppLayouts:];
-[SBButterflyCoplanarWindowingModifier setReadsActiveAppLayoutFromContext:];
-[SBButterflyCoplanarWindowingModifier setScreenRegion:];
```
