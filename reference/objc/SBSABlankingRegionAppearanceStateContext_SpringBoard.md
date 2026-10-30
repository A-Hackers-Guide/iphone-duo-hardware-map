# `SBSABlankingRegionAppearanceStateContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SBSABlockMutating`
- 4 instance variables, 8 properties, 16 instance methods, 3 class methods

## Instance variables

```
B _admitsAssociatedIndicator;
@"NSString" _regionIdentifier;
@"SBSABlankingRegionElementContext" _blankingRegionElementContext;
q _appearancePhase;
```

## Properties

```
@property (T@"NSString",C,N,S_setRegionIdentifier:,V_regionIdentifier) regionIdentifier;
@property (T@"SBSABlankingRegionElementContext",&,N,S_setBlankingRegionElementContext:,V_blankingRegionElementContext) blankingRegionElementContext;
@property (Tq,N,S_setAppearancePhase:,V_appearancePhase) appearancePhase;
@property (TB,N,S_setAdmitsAssociatedIndicator:,V_admitsAssociatedIndicator) admitsAssociatedIndicator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSABlankingRegionAppearanceStateContext initialize];
+[SBSABlankingRegionAppearanceStateContext instanceWithBlock:];
+[SBSABlankingRegionAppearanceStateContext mutatorClass];
```

## Instance methods

```
-[SBSABlankingRegionAppearanceStateContext isSettled];
-[SBSABlankingRegionAppearanceStateContext hash];
-[SBSABlankingRegionAppearanceStateContext description];
-[SBSABlankingRegionAppearanceStateContext copyWithZone:];
-[SBSABlankingRegionAppearanceStateContext regionIdentifier];
-[SBSABlankingRegionAppearanceStateContext isEqual:];
-[SBSABlankingRegionAppearanceStateContext copyWithBlock:];
-[SBSABlankingRegionAppearanceStateContext membersForCoder];
-[SBSABlankingRegionAppearanceStateContext isDisappeared];
-[SBSABlankingRegionAppearanceStateContext appearancePhase];
-[SBSABlankingRegionAppearanceStateContext _setAdmitsAssociatedIndicator:];
-[SBSABlankingRegionAppearanceStateContext _setAppearancePhase:];
-[SBSABlankingRegionAppearanceStateContext _setBlankingRegionElementContext:];
-[SBSABlankingRegionAppearanceStateContext _setRegionIdentifier:];
-[SBSABlankingRegionAppearanceStateContext admitsAssociatedIndicator];
-[SBSABlankingRegionAppearanceStateContext blankingRegionElementContext];
```
