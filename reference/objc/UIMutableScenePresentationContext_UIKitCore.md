# `UIMutableScenePresentationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScenePresentationContext`
- 0 instance variables, 21 properties, 29 instance methods, 0 class methods

## Properties

```
@property (T@"UIScenePresentationContext",&,N,S_setDefaultPresentationContext:) _defaultPresentationContext;
@property (T@"NSSet",C,D,N,S_setExclusiveLayerTargetsToInclude:) _exclusiveLayerTargetsToInclude;
@property (T@"NSSet",C,D,N,S_setLayerTargetsToExclude:) _layerTargetsToExclude;
@property (TB,D,N,G_isVisibilityPropagationEnabled,S_setVisibilityPropagationEnabled:) _visibilityPropagationEnabled;
@property (TB,D,N,S_setForwardsKeyboardLayersToHost:) _forwardsKeyboardLayersToHost;
@property (T@"NSString",C,D,N,S_setMinificationFilterName:) _minificationFilterName;
@property (TB,D,N,GisClippingDisabled) clippingDisabled;
@property (TQ,D,N) appearanceStyle;
@property (T@"UIColor",C,D,N) backgroundColorWhileHosting;
@property (T@"UIColor",C,D,N) backgroundColorWhileNotHosting;
@property (TQ,D,N) presentedLayerTypes;
@property (T@"UITransformer",C,D,N) hostTransformer;
@property (TQ,D,N) renderingMode;
@property (T@"UISceneAsynchronousRenderingOptions",C,D,N) asynchronousRenderingOptions;
@property (TB,D,N) inheritsSecurity;
@property (TB,D,N) resizesHostedContext;
@property (TB,D,N) zombifiesHostedContext;
@property (TB,D,N) shouldPassthroughHitTestEventsIfTransparent;
@property (TB,D,N) stopsHitTestTransformAccumulation;
@property (TB,D,N) stopsSecureSuperlayersValidation;
@property (TB,D,N) shouldSupportFlattening;
```

## Instance methods

```
-[UIMutableScenePresentationContext setShouldPassthroughHitTestEventsIfTransparent:];
-[UIMutableScenePresentationContext _setDefaultPresentationContext:];
-[UIMutableScenePresentationContext setStopsSecureSuperlayersValidation:];
-[UIMutableScenePresentationContext _setMinificationFilterName:];
-[UIMutableScenePresentationContext setStopsHitTestTransformAccumulation:];
-[UIMutableScenePresentationContext setBackgroundColorWhileHosting:];
-[UIMutableScenePresentationContext setResizesHostedContext:];
-[UIMutableScenePresentationContext removeLayerPresentationOverrideForLayerTarget:];
-[UIMutableScenePresentationContext _setLayerTargetsToExclude:];
-[UIMutableScenePresentationContext _setVisibilityPropagationEnabled:];
-[UIMutableScenePresentationContext setRenderingMode:];
-[UIMutableScenePresentationContext removeAllLayerPresentationOverrides];
-[UIMutableScenePresentationContext modifyLayerPresentationOverrideContextForLayerTarget:block:];
-[UIMutableScenePresentationContext modifyWindowLayerPresentationContextWithBlock:];
-[UIMutableScenePresentationContext setBackgroundColorWhileNotHosting:];
-[UIMutableScenePresentationContext setShouldSupportFlattening:];
-[UIMutableScenePresentationContext _setExclusiveLayerTargetsToInclude:];
-[UIMutableScenePresentationContext setInheritsSecurity:];
-[UIMutableScenePresentationContext setZombifiesHostedContext:];
-[UIMutableScenePresentationContext _existingLayerPresentationContextCreatingIfNecessary:];
-[UIMutableScenePresentationContext setClippingDisabled:];
-[UIMutableScenePresentationContext setPresentedLayerTypes:];
-[UIMutableScenePresentationContext setAsynchronousRenderingOptions:];
-[UIMutableScenePresentationContext setAppearanceStyle:];
-[UIMutableScenePresentationContext copyWithZone:];
-[UIMutableScenePresentationContext setHostTransformer:];
-[UIMutableScenePresentationContext _setForwardsKeyboardLayersToHost:];
-[UIMutableScenePresentationContext _defaultPresentationContext];
-[UIMutableScenePresentationContext resetToDefaults];
```
