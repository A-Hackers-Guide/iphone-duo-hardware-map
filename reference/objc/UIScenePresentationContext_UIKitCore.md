# `UIScenePresentationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 27 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"BSMutableSettings" _settings;
@"UIScenePresentationContext" _defaultPresentationContext;
@"UIMutableTransformer" _transformer;
```

## Properties

```
@property (T@"UIScenePresentationContext",R,N,V_defaultPresentationContext) _defaultPresentationContext;
@property (T@"NSSet",R,C,N) _exclusiveLayerTargetsToInclude;
@property (T@"NSSet",R,C,N) _layerTargetsToExclude;
@property (TB,R,N,G_isVisibilityPropagationEnabled) _visibilityPropagationEnabled;
@property (TB,R,N) _forwardsKeyboardLayersToHost;
@property (T@"NSString",R,C,N) _minificationFilterName;
@property (TB,R,N,GisClippingDisabled) clippingDisabled;
@property (TQ,R,N) appearanceStyle;
@property (T@"UIColor",R,C,N) backgroundColorWhileHosting;
@property (T@"UIColor",R,C,N) backgroundColorWhileNotHosting;
@property (TQ,R,N) presentedLayerTypes;
@property (T@"NSDictionary",R,C,N) layerPresentationOverrides;
@property (T@"UITransformer",R,C,N) hostTransformer;
@property (TQ,R,N) renderingMode;
@property (T@"UISceneAsynchronousRenderingOptions",R,C,N) asynchronousRenderingOptions;
@property (TB,R,N) inheritsSecurity;
@property (TB,R,N) resizesHostedContext;
@property (TB,R,N) zombifiesHostedContext;
@property (TB,R,N) shouldPassthroughHitTestEventsIfTransparent;
@property (TB,R,N) stopsHitTestTransformAccumulation;
@property (TB,R,N) stopsSecureSuperlayersValidation;
@property (TB,R,N) shouldSupportFlattening;
@property (T@"UISceneWindowLayerPresentationContext",R,C,N) windowLayerPresentationContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScenePresentationContext hostTransformer];
-[UIScenePresentationContext stopsSecureSuperlayersValidation];
-[UIScenePresentationContext resizesHostedContext];
-[UIScenePresentationContext stopsHitTestTransformAccumulation];
-[UIScenePresentationContext mutableCopyWithZone:];
-[UIScenePresentationContext backgroundColorWhileNotHosting];
-[UIScenePresentationContext layerPresentationOverrides];
-[UIScenePresentationContext succinctDescriptionBuilder];
-[UIScenePresentationContext _initWithSettings:defaultPresentationContext:];
-[UIScenePresentationContext init];
-[UIScenePresentationContext _layerTargetsToExclude];
-[UIScenePresentationContext _initWithPresentationContext:];
-[UIScenePresentationContext backgroundColorWhileHosting];
-[UIScenePresentationContext appearanceStyle];
-[UIScenePresentationContext descriptionWithMultilinePrefix:];
-[UIScenePresentationContext isClippingDisabled];
-[UIScenePresentationContext _initWithDefaultPresentationContext:];
-[UIScenePresentationContext succinctDescription];
-[UIScenePresentationContext shouldPassthroughHitTestEventsIfTransparent];
-[UIScenePresentationContext inheritsSecurity];
-[UIScenePresentationContext hash];
-[UIScenePresentationContext _exclusiveLayerTargetsToInclude];
-[UIScenePresentationContext description];
-[UIScenePresentationContext shouldSupportFlattening];
-[UIScenePresentationContext renderingMode];
-[UIScenePresentationContext _isVisibilityPropagationEnabled];
-[UIScenePresentationContext _initWithDefaultValues];
-[UIScenePresentationContext copyWithZone:];
-[UIScenePresentationContext presentedLayerTypes];
-[UIScenePresentationContext _defaultPresentationContext];
-[UIScenePresentationContext isEqual:];
-[UIScenePresentationContext asynchronousRenderingOptions];
-[UIScenePresentationContext _minificationFilterName];
-[UIScenePresentationContext zombifiesHostedContext];
-[UIScenePresentationContext windowLayerPresentationContext];
-[UIScenePresentationContext _forwardsKeyboardLayersToHost];
-[UIScenePresentationContext descriptionBuilderWithMultilinePrefix:];
```
