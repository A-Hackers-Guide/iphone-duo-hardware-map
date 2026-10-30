# `_UIContentPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIMorphPlatterViewBase`
- 11 instance variables, 17 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" shapeLayer;
$__lazy_storage_$_morphPlatformContext;
$__lazy_storage_$_morphLayer;
@"_UIPortalView" collapsedPortalView;
@"<_UIAssertion>" collapsedPreviewBackgroundSuppression;
B isFrozen;
B didTearOffPreviewForDrag;
backgroundCapture;
shadowPath;
morphLayerTransform;
@"_UIShadowProperties" _shadowProperties;
```

## Properties

```
@property (T@"UITargetedPreview",N,&) collapsedPreview;
@property (T@"UITargetedPreview",N,&) expandedPreview;
@property (TB,N) expanded;
@property (TB,N) wantsEdgeAntialiasing;
@property (TQ,N) preferredMorphingAxis;
@property (Tq,N) collapsedShadowStyle;
@property (Tq,N) expandedShadowStyle;
@property (Td,N) collapsedShadowIntensity;
@property (Td,N) expandedShadowIntensity;
@property (TB,N) hidesCollapsedSourceView;
@property (T@"CAShapeLayer",N,R,VshapeLayer) shapeLayer;
@property (T@"_UIPortalView",N,&,VcollapsedPortalView) collapsedPortalView;
@property (T@"<_UIAssertion>",N,&,VcollapsedPreviewBackgroundSuppression) collapsedPreviewBackgroundSuppression;
@property (TB,N,VisFrozen) isFrozen;
@property (TB,N,VdidTearOffPreviewForDrag) didTearOffPreviewForDrag;
@property (T@"_UIShadowProperties",N,&,V_shadowProperties) _shadowProperties;
@property (T@"UITargetedPreview",N,R) _destinationPreview;
```

## Instance methods

```
-[_UIContentPlatterView isFrozen];
-[_UIContentPlatterView didMoveToWindow];
-[_UIContentPlatterView setExpanded:];
-[_UIContentPlatterView shapeLayer];
-[_UIContentPlatterView layoutSubviews];
-[_UIContentPlatterView _updateCornerRadii];
-[_UIContentPlatterView setIsFrozen:];
-[_UIContentPlatterView updateProperties];
-[_UIContentPlatterView _morphPreviewFromCurrentState:fallbackBackgroundColor:contentScale:];
-[_UIContentPlatterView initWithCoder:];
-[_UIContentPlatterView _shadowProperties];
-[_UIContentPlatterView initWithFrame:];
-[_UIContentPlatterView teardown];
-[_UIContentPlatterView updateContentSize];
-[_UIContentPlatterView expanded];
-[_UIContentPlatterView expandedPreview];
-[_UIContentPlatterView _allowsUserInteractionForCompactPreview:];
-[_UIContentPlatterView _destinationPreview];
-[_UIContentPlatterView _resolveLayerShadow];
-[_UIContentPlatterView _updateBackgroundCaptureFor:];
-[_UIContentPlatterView _updateCollapsedPortalViewWithShouldHide:];
-[_UIContentPlatterView _updateGlassAppearanceIfNeeded];
-[_UIContentPlatterView _updateMorphLayerTransform];
-[_UIContentPlatterView _updateShadowPath];
-[_UIContentPlatterView _updateShapeView];
-[_UIContentPlatterView collapsedPortalView];
-[_UIContentPlatterView collapsedPreview];
-[_UIContentPlatterView collapsedPreviewBackgroundSuppression];
-[_UIContentPlatterView collapsedShadowIntensity];
-[_UIContentPlatterView collapsedShadowStyle];
-[_UIContentPlatterView didTearOffForDrag];
-[_UIContentPlatterView didTearOffPreviewForDrag];
-[_UIContentPlatterView expandedShadowIntensity];
-[_UIContentPlatterView expandedShadowStyle];
-[_UIContentPlatterView freezeExpandedPreview];
-[_UIContentPlatterView hidesCollapsedSourceView];
-[_UIContentPlatterView preferredMorphingAxis];
-[_UIContentPlatterView setCollapsedPortalView:];
-[_UIContentPlatterView setCollapsedPreview:];
-[_UIContentPlatterView setCollapsedPreviewBackgroundSuppression:];
-[_UIContentPlatterView setCollapsedShadowIntensity:];
-[_UIContentPlatterView setCollapsedShadowStyle:];
-[_UIContentPlatterView setDidTearOffPreviewForDrag:];
-[_UIContentPlatterView setExpandedPreview:];
-[_UIContentPlatterView setExpandedShadowIntensity:];
-[_UIContentPlatterView setExpandedShadowStyle:];
-[_UIContentPlatterView setHidesCollapsedSourceView:];
-[_UIContentPlatterView setPreferredMorphingAxis:];
-[_UIContentPlatterView setWantsEdgeAntialiasing:];
-[_UIContentPlatterView set_shadowProperties:];
-[_UIContentPlatterView wantsEdgeAntialiasing];
```
