# `BWCoreImageFilterRendererParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRendererParameters`
- 3 instance variables, 9 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _filters;
B _requiresFaceLandmarks;
B _requiresDepthMap;
```

## Properties

```
@property (T@"NSArray",C,N,V_filters) filters;
@property (TB,R,N,V_requiresDepthMap) requiresDepthMap;
@property (TB,R,N,V_requiresFaceLandmarks) requiresFaceLandmarks;
@property (Ts,R,N) type;
@property (Tf,R,N) interpolationFractionComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCoreImageFilterRendererParameters initialize];
+[BWCoreImageFilterRendererParameters containsFilterRequiringFaceLandmarks:];
```

## Instance methods

```
-[BWCoreImageFilterRendererParameters dealloc];
-[BWCoreImageFilterRendererParameters setFilters:];
-[BWCoreImageFilterRendererParameters filters];
-[BWCoreImageFilterRendererParameters type];
-[BWCoreImageFilterRendererParameters copyWithZone:];
-[BWCoreImageFilterRendererParameters depthTypeForFilter:];
-[BWCoreImageFilterRendererParameters initWithFilters:];
-[BWCoreImageFilterRendererParameters interpolationFractionComplete];
-[BWCoreImageFilterRendererParameters prepareForRenderingWithInputVideoFormat:];
-[BWCoreImageFilterRendererParameters requiresDepthMap];
-[BWCoreImageFilterRendererParameters requiresFaceLandmarks];
-[BWCoreImageFilterRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:];
```
