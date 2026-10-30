# `SBSAIndicatorElementContextMutator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBSAIndicatorElementContext" _systemApertureElementContext;
```

## Properties

```
@property (T@"SBSAIndicatorElementContext",R,N,V_systemApertureElementContext) systemApertureElementContext;
@property (T@"NSString",C,N) clientIdentifier;
@property (T@"NSString",C,N) elementIdentifier;
@property (TB,N) indicatorNeedsDisplayWellKnownLocation;
@property (TB,N) indicatorWantsCornerPosition;
@property (TB,N) indicatorRotationChangesShouldBeUnanimated;
@property (TB,N) indicatorAwaitsSteady;
@property (TB,N) indicatorContentRendersAsSquare;
@property (T{CGSize=dd},N) indicatorSize;
@property (T{NSDirectionalEdgeInsets=dddd},N) preferredEdgeOutsets;
@property (TB,N,GisFixedInPortraitOrientation) fixedInPortraitOrientation;
@property (TB,N,GisTransparentToTouches) transparentToTouches;
@property (T@"NSString",C,N) associatedBlankingRegionIdentifier;
@property (Td,N) preferredSystemClipPadding;
```

## Instance methods

```
-[SBSAIndicatorElementContextMutator setElementIdentifier:];
-[SBSAIndicatorElementContextMutator setPreferredSystemClipPadding:];
-[SBSAIndicatorElementContextMutator indicatorNeedsDisplayWellKnownLocation];
-[SBSAIndicatorElementContextMutator clientIdentifier];
-[SBSAIndicatorElementContextMutator preferredEdgeOutsets];
-[SBSAIndicatorElementContextMutator indicatorRotationChangesShouldBeUnanimated];
-[SBSAIndicatorElementContextMutator preferredSystemClipPadding];
-[SBSAIndicatorElementContextMutator setFixedInPortraitOrientation:];
-[SBSAIndicatorElementContextMutator elementIdentifier];
-[SBSAIndicatorElementContextMutator setPreferredEdgeOutsets:];
-[SBSAIndicatorElementContextMutator indicatorSize];
-[SBSAIndicatorElementContextMutator systemApertureElementContext];
-[SBSAIndicatorElementContextMutator indicatorAwaitsSteady];
-[SBSAIndicatorElementContextMutator setClientIdentifier:];
-[SBSAIndicatorElementContextMutator isTransparentToTouches];
-[SBSAIndicatorElementContextMutator description];
-[SBSAIndicatorElementContextMutator setIndicatorAwaitsSteady:];
-[SBSAIndicatorElementContextMutator setIndicatorSize:];
-[SBSAIndicatorElementContextMutator associatedBlankingRegionIdentifier];
-[SBSAIndicatorElementContextMutator initWithSystemApertureElementContext:];
-[SBSAIndicatorElementContextMutator indicatorWantsCornerPosition];
-[SBSAIndicatorElementContextMutator indicatorContentRendersAsSquare];
-[SBSAIndicatorElementContextMutator setAssociatedBlankingRegionIdentifier:];
-[SBSAIndicatorElementContextMutator isFixedInPortraitOrientation];
-[SBSAIndicatorElementContextMutator setTransparentToTouches:];
-[SBSAIndicatorElementContextMutator setIndicatorContentRendersAsSquare:];
-[SBSAIndicatorElementContextMutator setIndicatorNeedsDisplayWellKnownLocation:];
-[SBSAIndicatorElementContextMutator setIndicatorRotationChangesShouldBeUnanimated:];
-[SBSAIndicatorElementContextMutator setIndicatorWantsCornerPosition:];
```
