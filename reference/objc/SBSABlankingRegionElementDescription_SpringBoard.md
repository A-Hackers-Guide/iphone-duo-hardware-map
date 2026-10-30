# `SBSABlankingRegionElementDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAElementDescribing`, `NSCopying`, `SBSABlockMutating`
- 3 instance variables, 7 properties, 13 instance methods, 3 class methods

## Instance variables

```
i _appearState;
@"NSUUID" _interfaceElementIdentifier;
@"<SAElementIdentifying>" _associatedSystemApertureElementIdentity;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setInterfaceElementIdentifier:,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T@"<SAElementIdentifying>",C,N,S_setAssociatedSystemApertureElementIdentity:,V_associatedSystemApertureElementIdentity) associatedSystemApertureElementIdentity;
@property (Ti,N,S_setAppearState:,V_appearState) appearState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSABlankingRegionElementDescription initialize];
+[SBSABlankingRegionElementDescription instanceWithBlock:];
+[SBSABlankingRegionElementDescription mutatorClass];
```

## Instance methods

```
-[SBSABlankingRegionElementDescription associatedSystemApertureElementIdentity];
-[SBSABlankingRegionElementDescription encodeWithCoder:];
-[SBSABlankingRegionElementDescription interfaceElementIdentifier];
-[SBSABlankingRegionElementDescription hash];
-[SBSABlankingRegionElementDescription description];
-[SBSABlankingRegionElementDescription appearState];
-[SBSABlankingRegionElementDescription copyWithZone:];
-[SBSABlankingRegionElementDescription isEqual:];
-[SBSABlankingRegionElementDescription copyWithBlock:];
-[SBSABlankingRegionElementDescription membersForCoder];
-[SBSABlankingRegionElementDescription _setInterfaceElementIdentifier:];
-[SBSABlankingRegionElementDescription _setAppearState:];
-[SBSABlankingRegionElementDescription _setAssociatedSystemApertureElementIdentity:];
```
