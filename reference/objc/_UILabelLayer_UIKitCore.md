# `_UILabelLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 7 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"_UILabelContentLayer" _contentLayer;
@"_UILabelLightReactiveLayer" _lightReactiveLayer;
@"_UILabelLightInertLayer" _lightInertLayer;
B _contentInsetsValid;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
Q _oversizeEdgesIncludedInLabelLayer;
@"UIView" _lightContainerView;
```

## Properties

```
@property (TB,R,N,V_contentInsetsValid) letterformAwareInsetsAreValid;
@property (T{UIEdgeInsets=dddd},R,N,V_contentInsets) letterformAwareInsets;
@property (TQ,N,V_oversizeEdgesIncludedInLabelLayer) oversizeEdgesIncludedInLabelLayer;
@property (T@"UIView",&,N,V_lightContainerView) lightContainerView;
```

## Instance methods

```
-[_UILabelLayer setContentsGravity:];
-[_UILabelLayer setOversizeEdgesIncludedInLabelLayer:];
-[_UILabelLayer letterformAwareInsets];
-[_UILabelLayer setNeedsDisplayOnBoundsChange:];
-[_UILabelLayer reactToLightChanged];
-[_UILabelLayer _labelLayerToClipDuringBoundsSizeAnimation];
-[_UILabelLayer setContentsMultiplyColor:];
-[_UILabelLayer invalidateContentInsets];
-[_UILabelLayer setBounds:];
-[_UILabelLayer _setLabelMasksToBoundsForAnimation:];
-[_UILabelLayer _updateSublayers];
-[_UILabelLayer setContentsScale:];
-[_UILabelLayer _clearContents];
-[_UILabelLayer oversizeEdgesIncludedInLabelLayer];
-[_UILabelLayer lightContainerView];
-[_UILabelLayer setFrame:];
-[_UILabelLayer layoutSublayers];
-[_UILabelLayer setLightContainerView:];
-[_UILabelLayer setNeedsDisplayInRect:];
-[_UILabelLayer updateContentInsets];
-[_UILabelLayer setContentsFormat:];
-[_UILabelLayer _glyphPathBoundsExceedsLayers:drawableGlyphPathBounds:edgesClipped:];
-[_UILabelLayer letterformAwareInsetsAreValid];
-[_UILabelLayer setMasksToBounds:];
```
