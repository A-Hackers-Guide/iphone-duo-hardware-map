# `_UIVisualEffectDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _filterEntries;
@"NSMutableArray" _viewEffects;
@"NSMutableArray" _underlays;
@"NSMutableArray" _overlays;
B _textShouldRenderWithTintColor;
B _allowsVibrancyInContent;
B _disableInPlaceFiltering;
B _requestAlphaTransition;
B _contentViewRequiresClipping;
B _layerHitTestsAsOpaque;
@"UIView<_UIVisualEffectViewParticipating>" _identityContainerView;
@"UIView<_UIVisualEffectViewParticipating>" _requestedContainerView;
q _alphaTransition;
```

## Properties

```
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N,V_identityContainerView) _identityContainerView;
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N,V_requestedContainerView) _requestedContainerView;
@property (Tq,N,V_alphaTransition) alphaTransition;
@property (TB,N,V_contentViewRequiresClipping) contentViewRequiresClipping;
@property (TB,N,V_layerHitTestsAsOpaque) layerHitTestsAsOpaque;
@property (T@"NSArray",C,N,V_filterEntries) filterEntries;
@property (T@"NSArray",C,N,V_viewEffects) viewEffects;
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N) containerView;
@property (T@"NSArray",C,N,V_underlays) underlays;
@property (T@"NSArray",C,N,V_overlays) overlays;
@property (TB,N,V_textShouldRenderWithTintColor) textShouldRenderWithTintColor;
@property (TB,N,V_allowsVibrancyInContent) allowsVibrancyInContent;
@property (TB,N,V_disableInPlaceFiltering) disableInPlaceFiltering;
@property (TB,N,V_requestAlphaTransition) requestAlphaTransition;
```

## Class methods

```
+[_UIVisualEffectDescriptor newTransitionDescriptorForStops:];
```

## Instance methods

```
-[_UIVisualEffectDescriptor setContainerView:];
-[_UIVisualEffectDescriptor setTextShouldRenderWithTintColor:];
-[_UIVisualEffectDescriptor addOverlay:];
-[_UIVisualEffectDescriptor addViewEffect:];
-[_UIVisualEffectDescriptor init];
-[_UIVisualEffectDescriptor layerHitTestsAsOpaque];
-[_UIVisualEffectDescriptor setLayerHitTestsAsOpaque:];
-[_UIVisualEffectDescriptor uniqueFilterNames];
-[_UIVisualEffectDescriptor setAlphaTransition:];
-[_UIVisualEffectDescriptor copyForTransitionToDescriptor:];
-[_UIVisualEffectDescriptor requestAlphaTransition];
-[_UIVisualEffectDescriptor _identityContainerView];
-[_UIVisualEffectDescriptor setFilterEntries:];
-[_UIVisualEffectDescriptor containerView];
-[_UIVisualEffectDescriptor overlays];
-[_UIVisualEffectDescriptor underlays];
-[_UIVisualEffectDescriptor viewEffects];
-[_UIVisualEffectDescriptor setDisableInPlaceFiltering:];
-[_UIVisualEffectDescriptor contentViewRequiresClipping];
-[_UIVisualEffectDescriptor setRequestAlphaTransition:];
-[_UIVisualEffectDescriptor allowsVibrancyInContent];
-[_UIVisualEffectDescriptor addFilterEntry:];
-[_UIVisualEffectDescriptor addUnderlay:];
-[_UIVisualEffectDescriptor textShouldRenderWithTintColor];
-[_UIVisualEffectDescriptor description];
-[_UIVisualEffectDescriptor alphaTransition];
-[_UIVisualEffectDescriptor disableInPlaceFiltering];
-[_UIVisualEffectDescriptor set_identityContainerView:];
-[_UIVisualEffectDescriptor filterEntries];
-[_UIVisualEffectDescriptor setOverlays:];
-[_UIVisualEffectDescriptor set_requestedContainerView:];
-[_UIVisualEffectDescriptor _requestedContainerView];
-[_UIVisualEffectDescriptor setUnderlays:];
-[_UIVisualEffectDescriptor setViewEffects:];
-[_UIVisualEffectDescriptor setContentViewRequiresClipping:];
-[_UIVisualEffectDescriptor setAllowsVibrancyInContent:];
```
