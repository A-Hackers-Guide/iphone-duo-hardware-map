# `SBFSwitcherIconZooming` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 15 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) iconContentScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) iconImageFrame;
@property (TB,R,N) iconImageSizeMatchesBoundsSize;
@property (T{CGSize=dd},R,N) iconImageSize;
```

## Instance methods

```
-[SBFSwitcherIconZooming iconImageAlignment];
-[SBFSwitcherIconZooming iconContentScale];
-[SBFSwitcherIconZooming setMorphFraction:];
-[SBFSwitcherIconZooming iconImageSize];
-[SBFSwitcherIconZooming adjustedCrossfadeProgressForCrossfadeProgress:];
-[SBFSwitcherIconZooming shouldClipToBoundsWhenSizeChanges];
-[SBFSwitcherIconZooming scaleForFadeValue:originalSize:containerSize:];
-[SBFSwitcherIconZooming setIconContentHidden:];
-[SBFSwitcherIconZooming matchingIconZoomingViewOverlay];
-[SBFSwitcherIconZooming cleanUpAfterCrossfadeCompletion];
-[SBFSwitcherIconZooming iconImageSizeMatchesBoundsSize];
-[SBFSwitcherIconZooming prepareToCrossfadeImageWithView:];
-[SBFSwitcherIconZooming setCrossfadeCornerRadius:];
-[SBFSwitcherIconZooming hasSameOriginatingIconAsForIconZoomingView:];
-[SBFSwitcherIconZooming iconImageFrame];
```
