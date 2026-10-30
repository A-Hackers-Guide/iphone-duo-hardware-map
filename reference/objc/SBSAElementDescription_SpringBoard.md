# `SBSAElementDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAElementDescribing`, `SAUIElementViewPreferencesProviding`, `SAUISnapshotReasonProviding`, `SAUIElementSubcomponentPreferencesProviding`, `NSCopying`, `SBSABlockMutating`
- 27 instance variables, 32 properties, 61 instance methods, 3 class methods

## Instance variables

```
B _displayedWithLimitedSize;
i _appearState;
@"NSUUID" _interfaceElementIdentifier;
Q _obstructionEdge;
Q _layoutDirection;
@"<SAElementIdentifying>" _associatedSystemApertureElementIdentity;
d _sensorObscuringShadowProgress;
d _leadingViewBlurProgress;
d _leadingViewAlpha;
d _leadingViewSquishProgress;
d _trailingViewBlurProgress;
d _trailingViewAlpha;
d _trailingViewSquishProgress;
d _minimalViewBlurProgress;
d _minimalViewAlpha;
d _minimalViewSquishProgress;
d _customContentBlurProgress;
d _customContentAlpha;
d _snapshotViewBlurProgress;
d _snapshotViewAlpha;
@"NSString" _snapshotReason;
{CGSize="width"d"height"d} _leadingViewScale;
{CGSize="width"d"height"d} _trailingViewScale;
{CGSize="width"d"height"d} _minimalViewScale;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _leadingViewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _trailingViewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _minimalViewTransform;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setInterfaceElementIdentifier:,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T@"<SAElementIdentifying>",C,N,S_setAssociatedSystemApertureElementIdentity:,V_associatedSystemApertureElementIdentity) associatedSystemApertureElementIdentity;
@property (Ti,N,S_setAppearState:,V_appearState) appearState;
@property (TQ,N,S_setObstructionEdge:,V_obstructionEdge) obstructionEdge;
@property (TQ,N,S_setLayoutDirection:,V_layoutDirection) layoutDirection;
@property (TB,N,GisDisplayedWithLimitedSize,S_setDisplayedWithLimitedSize:,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (Td,N,S_setSensorObscuringShadowProgress:,V_sensorObscuringShadowProgress) sensorObscuringShadowProgress;
@property (Td,N,S_setLeadingViewBlurProgress:,V_leadingViewBlurProgress) leadingViewBlurProgress;
@property (Td,N,S_setLeadingViewAlpha:,V_leadingViewAlpha) leadingViewAlpha;
@property (Td,N,S_setLeadingViewSquishProgress:,V_leadingViewSquishProgress) leadingViewSquishProgress;
@property (T{CGSize=dd},N,S_setLeadingViewScale:,V_leadingViewScale) leadingViewScale;
@property (T{CGAffineTransform=dddddd},N,S_setLeadingViewTransform:,V_leadingViewTransform) leadingViewTransform;
@property (Td,N,S_setTrailingViewBlurProgress:,V_trailingViewBlurProgress) trailingViewBlurProgress;
@property (Td,N,S_setTrailingViewAlpha:,V_trailingViewAlpha) trailingViewAlpha;
@property (Td,N,S_setTrailingViewSquishProgress:,V_trailingViewSquishProgress) trailingViewSquishProgress;
@property (T{CGSize=dd},N,S_setTrailingViewScale:,V_trailingViewScale) trailingViewScale;
@property (T{CGAffineTransform=dddddd},N,S_setTrailingViewTransform:,V_trailingViewTransform) trailingViewTransform;
@property (Td,N,S_setMinimalViewBlurProgress:,V_minimalViewBlurProgress) minimalViewBlurProgress;
@property (Td,N,S_setMinimalViewAlpha:,V_minimalViewAlpha) minimalViewAlpha;
@property (Td,N,S_setMinimalViewSquishProgress:,V_minimalViewSquishProgress) minimalViewSquishProgress;
@property (T{CGSize=dd},N,S_setMinimalViewScale:,V_minimalViewScale) minimalViewScale;
@property (T{CGAffineTransform=dddddd},N,S_setMinimalViewTransform:,V_minimalViewTransform) minimalViewTransform;
@property (Td,N,S_setCustomContentBlurProgress:,V_customContentBlurProgress) customContentBlurProgress;
@property (Td,N,S_setCustomContentAlpha:,V_customContentAlpha) customContentAlpha;
@property (Td,N,S_setSnapshotViewBlurProgress:,V_snapshotViewBlurProgress) snapshotViewBlurProgress;
@property (Td,N,S_setSnapshotViewAlpha:,V_snapshotViewAlpha) snapshotViewAlpha;
@property (T@"NSString",C,N,S_setSnapshotReason:,V_snapshotReason) snapshotReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGAffineTransform=dddddd},?,R,N) customViewTransform;
```

## Class methods

```
+[SBSAElementDescription initialize];
+[SBSAElementDescription instanceWithBlock:];
+[SBSAElementDescription mutatorClass];
```

## Instance methods

```
-[SBSAElementDescription associatedSystemApertureElementIdentity];
-[SBSAElementDescription minimalViewSquishProgress];
-[SBSAElementDescription snapshotReason];
-[SBSAElementDescription leadingViewScale];
-[SBSAElementDescription obstructionEdge];
-[SBSAElementDescription isDisplayedWithLimitedSize];
-[SBSAElementDescription leadingViewBlurProgress];
-[SBSAElementDescription trailingViewAlpha];
-[SBSAElementDescription customContentBlurProgress];
-[SBSAElementDescription layoutDirection];
-[SBSAElementDescription leadingViewAlpha];
-[SBSAElementDescription trailingViewSquishProgress];
-[SBSAElementDescription leadingViewTransform];
-[SBSAElementDescription snapshotViewAlpha];
-[SBSAElementDescription minimalViewAlpha];
-[SBSAElementDescription sensorObscuringShadowProgress];
-[SBSAElementDescription minimalViewScale];
-[SBSAElementDescription encodeWithCoder:];
-[SBSAElementDescription snapshotViewBlurProgress];
-[SBSAElementDescription customContentAlpha];
-[SBSAElementDescription interfaceElementIdentifier];
-[SBSAElementDescription hash];
-[SBSAElementDescription description];
-[SBSAElementDescription appearState];
-[SBSAElementDescription trailingViewBlurProgress];
-[SBSAElementDescription copyWithZone:];
-[SBSAElementDescription trailingViewScale];
-[SBSAElementDescription isEqual:];
-[SBSAElementDescription minimalViewTransform];
-[SBSAElementDescription minimalViewBlurProgress];
-[SBSAElementDescription copyWithBlock:];
-[SBSAElementDescription trailingViewTransform];
-[SBSAElementDescription leadingViewSquishProgress];
-[SBSAElementDescription membersForCoder];
-[SBSAElementDescription _setLayoutDirection:];
-[SBSAElementDescription _setTrailingViewSquishProgress:];
-[SBSAElementDescription _setInterfaceElementIdentifier:];
-[SBSAElementDescription _setAppearState:];
-[SBSAElementDescription _setAssociatedSystemApertureElementIdentity:];
-[SBSAElementDescription _setCustomContentAlpha:];
-[SBSAElementDescription _setCustomContentBlurProgress:];
-[SBSAElementDescription _setDisplayedWithLimitedSize:];
-[SBSAElementDescription _setLeadingViewAlpha:];
-[SBSAElementDescription _setLeadingViewBlurProgress:];
-[SBSAElementDescription _setLeadingViewScale:];
-[SBSAElementDescription _setLeadingViewSquishProgress:];
-[SBSAElementDescription _setLeadingViewTransform:];
-[SBSAElementDescription _setMinimalViewAlpha:];
-[SBSAElementDescription _setMinimalViewBlurProgress:];
-[SBSAElementDescription _setMinimalViewScale:];
-[SBSAElementDescription _setMinimalViewSquishProgress:];
-[SBSAElementDescription _setMinimalViewTransform:];
-[SBSAElementDescription _setObstructionEdge:];
-[SBSAElementDescription _setSensorObscuringShadowProgress:];
-[SBSAElementDescription _setSnapshotReason:];
-[SBSAElementDescription _setSnapshotViewAlpha:];
-[SBSAElementDescription _setSnapshotViewBlurProgress:];
-[SBSAElementDescription _setTrailingViewAlpha:];
-[SBSAElementDescription _setTrailingViewBlurProgress:];
-[SBSAElementDescription _setTrailingViewScale:];
-[SBSAElementDescription _setTrailingViewTransform:];
```
