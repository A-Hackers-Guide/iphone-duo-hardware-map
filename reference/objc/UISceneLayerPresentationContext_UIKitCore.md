# `UISceneLayerPresentationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`
- 6 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UITransformer" _transformer;
d _alpha;
B _hidden;
B _clippingDisabled;
Q _renderingMode;
@"NSString" _minificationFilterName;
```

## Properties

```
@property (T@"UITransformer",&,N,V_transformer) transformer;
@property (Td,N,V_alpha) alpha;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (TB,N,GisClippingDisabled,V_clippingDisabled) clippingDisabled;
@property (TQ,N,V_renderingMode) renderingMode;
@property (T@"NSString",C,N,S_setMinificationFilterName:,V_minificationFilterName) _minificationFilterName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISceneLayerPresentationContext _setMinificationFilterName:];
-[UISceneLayerPresentationContext mutableCopyWithZone:];
-[UISceneLayerPresentationContext setHidden:];
-[UISceneLayerPresentationContext succinctDescriptionBuilder];
-[UISceneLayerPresentationContext init];
-[UISceneLayerPresentationContext setRenderingMode:];
-[UISceneLayerPresentationContext descriptionWithMultilinePrefix:];
-[UISceneLayerPresentationContext isClippingDisabled];
-[UISceneLayerPresentationContext succinctDescription];
-[UISceneLayerPresentationContext isHidden];
-[UISceneLayerPresentationContext setAlpha:];
-[UISceneLayerPresentationContext transformer];
-[UISceneLayerPresentationContext setClippingDisabled:];
-[UISceneLayerPresentationContext hash];
-[UISceneLayerPresentationContext description];
-[UISceneLayerPresentationContext renderingMode];
-[UISceneLayerPresentationContext _initWithSceneLayerPresentationContext:];
-[UISceneLayerPresentationContext _isEqualToDefaultContext];
-[UISceneLayerPresentationContext alpha];
-[UISceneLayerPresentationContext setTransformer:];
-[UISceneLayerPresentationContext copyWithZone:];
-[UISceneLayerPresentationContext isEqual:];
-[UISceneLayerPresentationContext _minificationFilterName];
-[UISceneLayerPresentationContext descriptionBuilderWithMultilinePrefix:];
```
