# `_UISheetPresentationMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 27 properties, 37 instance methods, 1 class methods

## Instance variables

```
@"UIScene" _scene;
```

## Properties

```
@property (Tq,R,N) defaultMode;
@property (T{UIEdgeInsets=dddd},R,N) minimumEdgeAttachedInsets;
@property (T{UIEdgeInsets=dddd},R,N) minimumFloatingInsets;
@property (T{UIRectCornerRadii=dddd},R,N) minimumEdgeAttachedCornerRadii;
@property (T{UIRectCornerRadii=dddd},R,N) minimumMaximumDetentEdgeAttachedCornerRadii;
@property (T{UIRectCornerRadii=dddd},R,N) minimumFloatingCornerRadii;
@property (T{UIRectCornerRadii=dddd},R,N) minimumMaximumDetentFloatingCornerRadii;
@property (Td,R,N) minimumMarginWhenTuckingIntoUnsafeAreaInCompactHeight;
@property (Td,R,N) minimumMarginWhenTuckingIntoUnsafeAreaInRegularWidthRegularHeight;
@property (Td,R,N) perspectiveRatio;
@property (Td,R,N) capsuleSheetInset;
@property (Td,R,N) mediumSheetInset;
@property (Td,R,N) capsuleHeightThreshold;
@property (TB,R,N) wantsEdgeAttachedInCompactHeight;
@property (TQ,R,N) edgesTuckingIntoSceneAlignedSafeArea;
@property (Td,R,N) minimumSidePadding;
@property (Td,R,N) cornerRadius;
@property (Td,R,N) maximumSheetDepthLevel;
@property (Td,R,N) preferredShadowOpacity;
@property (Td,R,N) shadowRadius;
@property (TB,R,N) exclusivelyUsesZPositionForTransform;
@property (TB,R,N) alwaysStacksWithChild;
@property (TB,R,N) fadeOutIfAnyDescendantWantsFullScreen;
@property (Td,R,N) topOffset;
@property (Td,R,N) topOffsetInCompactHeight;
@property (TB,R,N) wantsDimming;
@property (Td,R,N) transitionDuration;
```

## Class methods

```
+[_UISheetPresentationMetrics _defaultMetrics];
```

## Instance methods

```
-[_UISheetPresentationMetrics topOffset];
-[_UISheetPresentationMetrics minimumEdgeAttachedInsets];
-[_UISheetPresentationMetrics formSheetSizeForViewController:windowSize:screenSize:];
-[_UISheetPresentationMetrics topOffsetInCompactHeight];
-[_UISheetPresentationMetrics capsuleHeightThreshold];
-[_UISheetPresentationMetrics maximumSheetDepthLevel];
-[_UISheetPresentationMetrics minimumMarginWhenTuckingIntoUnsafeAreaInCompactHeight];
-[_UISheetPresentationMetrics transitionDuration];
-[_UISheetPresentationMetrics minimumMaximumDetentEdgeAttachedCornerRadii];
-[_UISheetPresentationMetrics maximumEdgeAttachedWidthForTraitCollection:];
-[_UISheetPresentationMetrics capsuleSheetInset];
-[_UISheetPresentationMetrics _init];
-[_UISheetPresentationMetrics minimumMarginWhenTuckingIntoUnsafeAreaInRegularWidthRegularHeight];
-[_UISheetPresentationMetrics configureDropShadowView:state:presentationController:];
-[_UISheetPresentationMetrics minimumMaximumDetentFloatingCornerRadii];
-[_UISheetPresentationMetrics minimumFloatingInsets];
-[_UISheetPresentationMetrics edgesTuckingIntoSceneAlignedSafeArea];
-[_UISheetPresentationMetrics supportsEdgeAttachedForTraitCollection:];
-[_UISheetPresentationMetrics wantsDimming];
-[_UISheetPresentationMetrics cornerRadius];
-[_UISheetPresentationMetrics wantsEdgeAttachedInCompactHeight];
-[_UISheetPresentationMetrics exclusivelyUsesZPositionForTransform];
-[_UISheetPresentationMetrics defaultMode];
-[_UISheetPresentationMetrics alwaysStacksWithChild];
-[_UISheetPresentationMetrics mediumSheetInset];
-[_UISheetPresentationMetrics transitionSpringParametersHighSpeed:];
-[_UISheetPresentationMetrics minimumFloatingCornerRadii];
-[_UISheetPresentationMetrics _metricsResolvedForScene:];
-[_UISheetPresentationMetrics minimumSidePadding];
-[_UISheetPresentationMetrics fadeOutIfAnyDescendantWantsFullScreen];
-[_UISheetPresentationMetrics minimumEdgeAttachedCornerRadii];
-[_UISheetPresentationMetrics addAlongsideAnimations:forSheetTransition:context:];
-[_UISheetPresentationMetrics defaultFormSheetSizeForScreenSize:];
-[_UISheetPresentationMetrics preferredShadowOpacity];
-[_UISheetPresentationMetrics shouldScaleDownBehindDescendantsForContainer:withBounds:];
-[_UISheetPresentationMetrics shadowRadius];
-[_UISheetPresentationMetrics perspectiveRatio];
```
