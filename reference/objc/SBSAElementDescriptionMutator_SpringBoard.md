# `SBSAElementDescriptionMutator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAUIElementViewPreferencesAccepting`, `SAUIElementSubcomponentPreferencesAccepting`
- 1 instance variables, 32 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"SBSAElementDescription" _elementDescription;
```

## Properties

```
@property (T@"NSUUID",C,N) interfaceElementIdentifier;
@property (T@"<SAElementIdentifying>",C,N) associatedSystemApertureElementIdentity;
@property (Ti,N) appearState;
@property (TQ,N) obstructionEdge;
@property (TQ,N) layoutDirection;
@property (TB,N,GisDisplayedWithLimitedSize) displayedWithLimitedSize;
@property (T@"NSString",C,N) snapshotReason;
@property (Td,N) sensorObscuringShadowProgress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N) leadingViewBlurProgress;
@property (Td,N) leadingViewAlpha;
@property (Td,N) leadingViewSquishProgress;
@property (T{CGSize=dd},N) leadingViewScale;
@property (Td,N) trailingViewBlurProgress;
@property (Td,N) trailingViewAlpha;
@property (Td,N) trailingViewSquishProgress;
@property (T{CGSize=dd},N) trailingViewScale;
@property (Td,N) minimalViewBlurProgress;
@property (Td,N) minimalViewAlpha;
@property (Td,N) minimalViewSquishProgress;
@property (T{CGSize=dd},N) minimalViewScale;
@property (Td,N) customContentBlurProgress;
@property (Td,N) customContentAlpha;
@property (Td,N) snapshotViewBlurProgress;
@property (Td,N) snapshotViewAlpha;
@property (T{CGAffineTransform=dddddd},?,N) leadingViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) trailingViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) minimalViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) customViewTransform;
```

## Instance methods

```
-[SBSAElementDescriptionMutator setDisplayedWithLimitedSize:];
-[SBSAElementDescriptionMutator associatedSystemApertureElementIdentity];
-[SBSAElementDescriptionMutator minimalViewSquishProgress];
-[SBSAElementDescriptionMutator snapshotReason];
-[SBSAElementDescriptionMutator leadingViewScale];
-[SBSAElementDescriptionMutator obstructionEdge];
-[SBSAElementDescriptionMutator isDisplayedWithLimitedSize];
-[SBSAElementDescriptionMutator setSnapshotReason:];
-[SBSAElementDescriptionMutator leadingViewBlurProgress];
-[SBSAElementDescriptionMutator setSnapshotViewBlurProgress:];
-[SBSAElementDescriptionMutator setTrailingViewScale:];
-[SBSAElementDescriptionMutator setMinimalViewTransform:];
-[SBSAElementDescriptionMutator setLayoutDirection:];
-[SBSAElementDescriptionMutator trailingViewAlpha];
-[SBSAElementDescriptionMutator setMinimalViewSquishProgress:];
-[SBSAElementDescriptionMutator customContentBlurProgress];
-[SBSAElementDescriptionMutator setTrailingViewBlurProgress:];
-[SBSAElementDescriptionMutator setObstructionEdge:];
-[SBSAElementDescriptionMutator layoutDirection];
-[SBSAElementDescriptionMutator leadingViewAlpha];
-[SBSAElementDescriptionMutator trailingViewSquishProgress];
-[SBSAElementDescriptionMutator setAppearState:];
-[SBSAElementDescriptionMutator leadingViewTransform];
-[SBSAElementDescriptionMutator snapshotViewAlpha];
-[SBSAElementDescriptionMutator setSnapshotViewAlpha:];
-[SBSAElementDescriptionMutator setLeadingViewBlurProgress:];
-[SBSAElementDescriptionMutator setLeadingViewTransform:];
-[SBSAElementDescriptionMutator setLeadingViewAlpha:];
-[SBSAElementDescriptionMutator setLeadingViewScale:];
-[SBSAElementDescriptionMutator minimalViewAlpha];
-[SBSAElementDescriptionMutator sensorObscuringShadowProgress];
-[SBSAElementDescriptionMutator setTrailingViewTransform:];
-[SBSAElementDescriptionMutator minimalViewScale];
-[SBSAElementDescriptionMutator setTrailingViewSquishProgress:];
-[SBSAElementDescriptionMutator setSensorObscuringShadowProgress:];
-[SBSAElementDescriptionMutator setAssociatedSystemApertureElementIdentity:];
-[SBSAElementDescriptionMutator setLeadingViewSquishProgress:];
-[SBSAElementDescriptionMutator snapshotViewBlurProgress];
-[SBSAElementDescriptionMutator customContentAlpha];
-[SBSAElementDescriptionMutator interfaceElementIdentifier];
-[SBSAElementDescriptionMutator setCustomContentBlurProgress:];
-[SBSAElementDescriptionMutator description];
-[SBSAElementDescriptionMutator setInterfaceElementIdentifier:];
-[SBSAElementDescriptionMutator setTrailingViewAlpha:];
-[SBSAElementDescriptionMutator setMinimalViewBlurProgress:];
-[SBSAElementDescriptionMutator appearState];
-[SBSAElementDescriptionMutator setCustomContentAlpha:];
-[SBSAElementDescriptionMutator setMinimalViewAlpha:];
-[SBSAElementDescriptionMutator trailingViewBlurProgress];
-[SBSAElementDescriptionMutator trailingViewScale];
-[SBSAElementDescriptionMutator minimalViewTransform];
-[SBSAElementDescriptionMutator initWithElementDescription:];
-[SBSAElementDescriptionMutator setMinimalViewScale:];
-[SBSAElementDescriptionMutator minimalViewBlurProgress];
-[SBSAElementDescriptionMutator trailingViewTransform];
-[SBSAElementDescriptionMutator leadingViewSquishProgress];
```
