# `BWMetalColorCubeRendererParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRendererParameters`
- 5 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"CIFilter" _colorFilter;
@"BWColorLookupCache" _colorLookupCache;
@"NSData" _foregroundColorLookupTable;
@"NSData" _backgroundColorLookupTable;
f _interpolationFractionComplete;
```

## Properties

```
@property (T@"BWColorLookupCache",R,&,N,V_colorLookupCache) colorLookupCache;
@property (T@"NSData",&,N,V_foregroundColorLookupTable) foregroundColorLookupTable;
@property (T@"NSData",&,N,V_backgroundColorLookupTable) backgroundColorLookupTable;
@property (T@"CIFilter",&,N,V_colorFilter) colorFilter;
@property (Ts,R,N) type;
@property (Tf,R,N,V_interpolationFractionComplete) interpolationFractionComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWMetalColorCubeRendererParameters initialize];
```

## Instance methods

```
-[BWMetalColorCubeRendererParameters dealloc];
-[BWMetalColorCubeRendererParameters colorFilter];
-[BWMetalColorCubeRendererParameters type];
-[BWMetalColorCubeRendererParameters setColorFilter:];
-[BWMetalColorCubeRendererParameters copyWithZone:];
-[BWMetalColorCubeRendererParameters colorLookupCache];
-[BWMetalColorCubeRendererParameters backgroundColorLookupTable];
-[BWMetalColorCubeRendererParameters foregroundColorLookupTable];
-[BWMetalColorCubeRendererParameters initWithColorFilter:colorLookupCache:];
-[BWMetalColorCubeRendererParameters interpolationFractionComplete];
-[BWMetalColorCubeRendererParameters prepareForRenderingWithInputVideoFormat:];
-[BWMetalColorCubeRendererParameters setBackgroundColorLookupTable:];
-[BWMetalColorCubeRendererParameters setForegroundColorLookupTable:];
-[BWMetalColorCubeRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:];
```
