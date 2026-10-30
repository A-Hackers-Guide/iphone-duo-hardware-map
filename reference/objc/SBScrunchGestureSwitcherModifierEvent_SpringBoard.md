# `SBScrunchGestureSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifierEvent`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _absoluteScale;
{CGPoint="x"d"y"d} _initialCentroid;
{CGPoint="x"d"y"d} _centroid;
{CGPoint="x"d"y"d} _translationWithoutScale;
```

## Properties

```
@property (T{CGPoint=dd},N,V_initialCentroid) initialCentroid;
@property (T{CGPoint=dd},N,V_centroid) centroid;
@property (Td,N,V_absoluteScale) absoluteScale;
@property (T{CGPoint=dd},N,V_translationWithoutScale) translationWithoutScale;
```

## Instance methods

```
-[SBScrunchGestureSwitcherModifierEvent centroid];
-[SBScrunchGestureSwitcherModifierEvent setAbsoluteScale:];
-[SBScrunchGestureSwitcherModifierEvent absoluteScale];
-[SBScrunchGestureSwitcherModifierEvent type];
-[SBScrunchGestureSwitcherModifierEvent setInitialCentroid:];
-[SBScrunchGestureSwitcherModifierEvent copyWithZone:];
-[SBScrunchGestureSwitcherModifierEvent initialCentroid];
-[SBScrunchGestureSwitcherModifierEvent setCentroid:];
-[SBScrunchGestureSwitcherModifierEvent setTranslationWithoutScale:];
-[SBScrunchGestureSwitcherModifierEvent translationWithoutScale];
```
