# `SBSAIndicatorElementDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAElementDescribing`, `NSCopying`, `SBSABlockMutating`, `SAUIIndicatorElementViewPreferencesProviding`
- 12 instance variables, 16 properties, 31 instance methods, 3 class methods

## Instance variables

```
B _needsMatchMoveAnimationBetweenCurtainAndJindoViews;
B _suppressesMicroIndicatorContainerRendering;
i _appearState;
@"NSUUID" _interfaceElementIdentifier;
@"NSString" _associatedBlankingRegionIdentifier;
@"<SAElementIdentifying>" _associatedSystemApertureElementIdentity;
d _indicatorViewBlurProgress;
d _indicatorViewAlpha;
d _fixedIndicatorViewBlurProgress;
d _fixedIndicatorViewAlpha;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _indicatorViewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _fixedIndicatorViewTransform;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setInterfaceElementIdentifier:,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T@"<SAElementIdentifying>",C,N,S_setAssociatedSystemApertureElementIdentity:,V_associatedSystemApertureElementIdentity) associatedSystemApertureElementIdentity;
@property (Ti,N,S_setAppearState:,V_appearState) appearState;
@property (Td,N,S_setIndicatorViewBlurProgress:,V_indicatorViewBlurProgress) indicatorViewBlurProgress;
@property (Td,N,S_setIndicatorViewAlpha:,V_indicatorViewAlpha) indicatorViewAlpha;
@property (T{CGAffineTransform=dddddd},N,S_setIndicatorViewTransform:,V_indicatorViewTransform) indicatorViewTransform;
@property (Td,N,S_setFixedIndicatorViewBlurProgress:,V_fixedIndicatorViewBlurProgress) fixedIndicatorViewBlurProgress;
@property (Td,N,S_setFixedIndicatorViewAlpha:,V_fixedIndicatorViewAlpha) fixedIndicatorViewAlpha;
@property (T{CGAffineTransform=dddddd},N,S_setFixedIndicatorViewTransform:,V_fixedIndicatorViewTransform) fixedIndicatorViewTransform;
@property (TB,N,S_setNeedsMatchMoveAnimationBetweenCurtainAndJindoViews:,V_needsMatchMoveAnimationBetweenCurtainAndJindoViews) needsMatchMoveAnimationBetweenCurtainAndJindoViews;
@property (T@"NSString",C,N,S_setAssociatedBlankingRegionIdentifier:,V_associatedBlankingRegionIdentifier) associatedBlankingRegionIdentifier;
@property (TB,N,S_setSuppressesMicroIndicatorContainerRendering:,V_suppressesMicroIndicatorContainerRendering) suppressesMicroIndicatorContainerRendering;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAIndicatorElementDescription initialize];
+[SBSAIndicatorElementDescription instanceWithBlock:];
+[SBSAIndicatorElementDescription mutatorClass];
```

## Instance methods

```
-[SBSAIndicatorElementDescription associatedSystemApertureElementIdentity];
-[SBSAIndicatorElementDescription fixedIndicatorViewAlpha];
-[SBSAIndicatorElementDescription indicatorViewAlpha];
-[SBSAIndicatorElementDescription suppressesMicroIndicatorContainerRendering];
-[SBSAIndicatorElementDescription indicatorViewTransform];
-[SBSAIndicatorElementDescription fixedIndicatorViewTransform];
-[SBSAIndicatorElementDescription encodeWithCoder:];
-[SBSAIndicatorElementDescription interfaceElementIdentifier];
-[SBSAIndicatorElementDescription hash];
-[SBSAIndicatorElementDescription fixedIndicatorViewBlurProgress];
-[SBSAIndicatorElementDescription description];
-[SBSAIndicatorElementDescription associatedBlankingRegionIdentifier];
-[SBSAIndicatorElementDescription appearState];
-[SBSAIndicatorElementDescription copyWithZone:];
-[SBSAIndicatorElementDescription needsMatchMoveAnimationBetweenCurtainAndJindoViews];
-[SBSAIndicatorElementDescription isEqual:];
-[SBSAIndicatorElementDescription indicatorViewBlurProgress];
-[SBSAIndicatorElementDescription copyWithBlock:];
-[SBSAIndicatorElementDescription membersForCoder];
-[SBSAIndicatorElementDescription _setInterfaceElementIdentifier:];
-[SBSAIndicatorElementDescription _setAppearState:];
-[SBSAIndicatorElementDescription _setAssociatedBlankingRegionIdentifier:];
-[SBSAIndicatorElementDescription _setAssociatedSystemApertureElementIdentity:];
-[SBSAIndicatorElementDescription _setFixedIndicatorViewAlpha:];
-[SBSAIndicatorElementDescription _setFixedIndicatorViewBlurProgress:];
-[SBSAIndicatorElementDescription _setFixedIndicatorViewTransform:];
-[SBSAIndicatorElementDescription _setIndicatorViewAlpha:];
-[SBSAIndicatorElementDescription _setIndicatorViewBlurProgress:];
-[SBSAIndicatorElementDescription _setIndicatorViewTransform:];
-[SBSAIndicatorElementDescription _setNeedsMatchMoveAnimationBetweenCurtainAndJindoViews:];
-[SBSAIndicatorElementDescription _setSuppressesMicroIndicatorContainerRendering:];
```
