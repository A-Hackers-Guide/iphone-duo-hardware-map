# `SBSAIndicatorElementContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SAElementIdentifying`, `SBSABlockMutating`, `SBSAElementContextProviding`, `SBSATouchTransparency`
- 13 instance variables, 17 properties, 33 instance methods, 3 class methods

## Instance variables

```
B _indicatorNeedsDisplayWellKnownLocation;
B _indicatorWantsCornerPosition;
B _indicatorRotationChangesShouldBeUnanimated;
B _indicatorAwaitsSteady;
B _indicatorContentRendersAsSquare;
B _fixedInPortraitOrientation;
B _transparentToTouches;
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
@"NSString" _associatedBlankingRegionIdentifier;
d _preferredSystemClipPadding;
{CGSize="width"d"height"d} _indicatorSize;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _preferredEdgeOutsets;
```

## Properties

```
@property (T@"NSString",C,N,S_setClientIdentifier:,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,S_setElementIdentifier:,V_elementIdentifier) elementIdentifier;
@property (T{CGSize=dd},N,S_setIndicatorSize:,V_indicatorSize) indicatorSize;
@property (T{NSDirectionalEdgeInsets=dddd},N,S_setPreferredEdgeOutsets:,V_preferredEdgeOutsets) preferredEdgeOutsets;
@property (TB,N,S_setIndicatorNeedsDisplayWellKnownLocation:,V_indicatorNeedsDisplayWellKnownLocation) indicatorNeedsDisplayWellKnownLocation;
@property (TB,N,S_setIndicatorWantsCornerPosition:,V_indicatorWantsCornerPosition) indicatorWantsCornerPosition;
@property (TB,N,S_setIndicatorRotationChangesShouldBeUnanimated:,V_indicatorRotationChangesShouldBeUnanimated) indicatorRotationChangesShouldBeUnanimated;
@property (TB,N,S_setIndicatorAwaitsSteady:,V_indicatorAwaitsSteady) indicatorAwaitsSteady;
@property (TB,N,S_setIndicatorContentRendersAsSquare:,V_indicatorContentRendersAsSquare) indicatorContentRendersAsSquare;
@property (TB,N,GisFixedInPortraitOrientation,S_setFixedInPortraitOrientation:,V_fixedInPortraitOrientation) fixedInPortraitOrientation;
@property (TB,N,GisTransparentToTouches,S_setTransparentToTouches:,V_transparentToTouches) transparentToTouches;
@property (T@"NSString",C,N,S_setAssociatedBlankingRegionIdentifier:,V_associatedBlankingRegionIdentifier) associatedBlankingRegionIdentifier;
@property (Td,N,S_setPreferredSystemClipPadding:,V_preferredSystemClipPadding) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAIndicatorElementContext initialize];
+[SBSAIndicatorElementContext instanceWithBlock:];
+[SBSAIndicatorElementContext mutatorClass];
```

## Instance methods

```
-[SBSAIndicatorElementContext indicatorNeedsDisplayWellKnownLocation];
-[SBSAIndicatorElementContext clientIdentifier];
-[SBSAIndicatorElementContext preferredEdgeOutsets];
-[SBSAIndicatorElementContext indicatorRotationChangesShouldBeUnanimated];
-[SBSAIndicatorElementContext preferredSystemClipPadding];
-[SBSAIndicatorElementContext elementIdentifier];
-[SBSAIndicatorElementContext indicatorSize];
-[SBSAIndicatorElementContext indicatorAwaitsSteady];
-[SBSAIndicatorElementContext isTransparentToTouches];
-[SBSAIndicatorElementContext hash];
-[SBSAIndicatorElementContext description];
-[SBSAIndicatorElementContext associatedBlankingRegionIdentifier];
-[SBSAIndicatorElementContext initWithSystemApertureElementContext:];
-[SBSAIndicatorElementContext indicatorWantsCornerPosition];
-[SBSAIndicatorElementContext copyWithZone:];
-[SBSAIndicatorElementContext indicatorContentRendersAsSquare];
-[SBSAIndicatorElementContext isFixedInPortraitOrientation];
-[SBSAIndicatorElementContext isEqual:];
-[SBSAIndicatorElementContext copyWithBlock:];
-[SBSAIndicatorElementContext membersForCoder];
-[SBSAIndicatorElementContext _setPreferredSystemClipPadding:];
-[SBSAIndicatorElementContext _setFixedInPortraitOrientation:];
-[SBSAIndicatorElementContext _setAssociatedBlankingRegionIdentifier:];
-[SBSAIndicatorElementContext _setClientIdentifier:];
-[SBSAIndicatorElementContext _setElementIdentifier:];
-[SBSAIndicatorElementContext _setIndicatorAwaitsSteady:];
-[SBSAIndicatorElementContext _setIndicatorContentRendersAsSquare:];
-[SBSAIndicatorElementContext _setIndicatorNeedsDisplayWellKnownLocation:];
-[SBSAIndicatorElementContext _setIndicatorRotationChangesShouldBeUnanimated:];
-[SBSAIndicatorElementContext _setIndicatorSize:];
-[SBSAIndicatorElementContext _setIndicatorWantsCornerPosition:];
-[SBSAIndicatorElementContext _setPreferredEdgeOutsets:];
-[SBSAIndicatorElementContext _setTransparentToTouches:];
```
