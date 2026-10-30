# `_UIMorphPlatterViewBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 18 instance variables, 18 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _expanded;
B _hideChromeWhenCollapsed;
B _alwaysCompact;
B _allowsUserInteractionInExpandedPreview;
B _preventPreviewRasterization;
B _hidesCollapsedSourceView;
B _wantsEdgeAntialiasing;
B _shouldMorphContents;
@"UITargetedPreview" _collapsedPreview;
@"UITargetedPreview" _expandedPreview;
Q _preferredMorphingAxis;
d _collapsedShadowIntensity;
d _expandedShadowIntensity;
q _collapsedShadowStyle;
q _expandedShadowStyle;
@"_UIShadowProperties" _shadowSettings;
@"NSDictionary" _separatedOptions;
@? _shouldApplyClippingHandler;
```

## Properties

```
@property (T@"UITargetedPreview",&,N,V_collapsedPreview) collapsedPreview;
@property (T@"UITargetedPreview",&,N,V_expandedPreview) expandedPreview;
@property (TB,N,V_expanded) expanded;
@property (TB,N,V_hideChromeWhenCollapsed) hideChromeWhenCollapsed;
@property (TB,N,V_alwaysCompact) alwaysCompact;
@property (TB,N,V_allowsUserInteractionInExpandedPreview) allowsUserInteractionInExpandedPreview;
@property (TB,N,V_preventPreviewRasterization) preventPreviewRasterization;
@property (TB,N,V_hidesCollapsedSourceView) hidesCollapsedSourceView;
@property (TB,N,V_wantsEdgeAntialiasing) wantsEdgeAntialiasing;
@property (TB,N,V_shouldMorphContents) shouldMorphContents;
@property (TQ,N,V_preferredMorphingAxis) preferredMorphingAxis;
@property (Td,N,V_collapsedShadowIntensity) collapsedShadowIntensity;
@property (Td,N,V_expandedShadowIntensity) expandedShadowIntensity;
@property (Tq,N,V_collapsedShadowStyle) collapsedShadowStyle;
@property (Tq,N,V_expandedShadowStyle) expandedShadowStyle;
@property (T@"_UIShadowProperties",&,N,V_shadowSettings) shadowSettings;
@property (T@"NSDictionary",&,N,V_separatedOptions) separatedOptions;
@property (T@?,C,N,V_shouldApplyClippingHandler) shouldApplyClippingHandler;
```

## Instance methods

```
-[_UIMorphPlatterViewBase didMoveToWindow];
-[_UIMorphPlatterViewBase setExpanded:];
-[_UIMorphPlatterViewBase setPreventPreviewRasterization:];
-[_UIMorphPlatterViewBase initWithFrame:];
-[_UIMorphPlatterViewBase updateContentSize];
-[_UIMorphPlatterViewBase preventPreviewRasterization];
-[_UIMorphPlatterViewBase expanded];
-[_UIMorphPlatterViewBase separatedOptions];
-[_UIMorphPlatterViewBase setSeparatedOptions:];
-[_UIMorphPlatterViewBase expandedPreview];
-[_UIMorphPlatterViewBase allowsUserInteractionInExpandedPreview];
-[_UIMorphPlatterViewBase alwaysCompact];
-[_UIMorphPlatterViewBase collapsedPreview];
-[_UIMorphPlatterViewBase collapsedShadowIntensity];
-[_UIMorphPlatterViewBase collapsedShadowStyle];
-[_UIMorphPlatterViewBase didTearOffForDrag];
-[_UIMorphPlatterViewBase expandedShadowIntensity];
-[_UIMorphPlatterViewBase expandedShadowStyle];
-[_UIMorphPlatterViewBase freezeExpandedPreview];
-[_UIMorphPlatterViewBase hideChromeWhenCollapsed];
-[_UIMorphPlatterViewBase hidesCollapsedSourceView];
-[_UIMorphPlatterViewBase preferredMorphingAxis];
-[_UIMorphPlatterViewBase setAllowsUserInteractionInExpandedPreview:];
-[_UIMorphPlatterViewBase setAlwaysCompact:];
-[_UIMorphPlatterViewBase setCollapsedPreview:];
-[_UIMorphPlatterViewBase setCollapsedShadowIntensity:];
-[_UIMorphPlatterViewBase setCollapsedShadowStyle:];
-[_UIMorphPlatterViewBase setExpandedPreview:];
-[_UIMorphPlatterViewBase setExpandedShadowIntensity:];
-[_UIMorphPlatterViewBase setExpandedShadowStyle:];
-[_UIMorphPlatterViewBase setHideChromeWhenCollapsed:];
-[_UIMorphPlatterViewBase setHidesCollapsedSourceView:];
-[_UIMorphPlatterViewBase setPreferredMorphingAxis:];
-[_UIMorphPlatterViewBase setShadowSettings:];
-[_UIMorphPlatterViewBase setShouldApplyClippingHandler:];
-[_UIMorphPlatterViewBase setShouldMorphContents:];
-[_UIMorphPlatterViewBase setWantsEdgeAntialiasing:];
-[_UIMorphPlatterViewBase shadowSettings];
-[_UIMorphPlatterViewBase shouldApplyClippingHandler];
-[_UIMorphPlatterViewBase shouldMorphContents];
-[_UIMorphPlatterViewBase wantsEdgeAntialiasing];
```
