# `BWStreamingCVAFilterRendererParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRendererParameters`
- 8 instance variables, 11 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"CIFilter" _colorFilter;
@"BWColorLookupCache" _colorLookupCache;
@"NSData" _foregroundColorLookupTable;
@"NSData" _backgroundColorLookupTable;
B _studioAndContourRenderingEnabled;
B _stageRenderingEnabled;
f _interpolationFractionComplete;
q _renderingStrategy;
```

## Properties

```
@property (T@"BWColorLookupCache",R,&,N,V_colorLookupCache) colorLookupCache;
@property (T@"NSData",&,N,V_foregroundColorLookupTable) foregroundColorLookupTable;
@property (T@"NSData",&,N,V_backgroundColorLookupTable) backgroundColorLookupTable;
@property (T@"CIFilter",&,N,V_colorFilter) colorFilter;
@property (Tq,R,N,V_renderingStrategy) renderingStrategy;
@property (Ts,R,N) type;
@property (Tf,R,N,V_interpolationFractionComplete) interpolationFractionComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStreamingCVAFilterRendererParameters initialize];
```

## Instance methods

```
-[BWStreamingCVAFilterRendererParameters dealloc];
-[BWStreamingCVAFilterRendererParameters colorFilter];
-[BWStreamingCVAFilterRendererParameters type];
-[BWStreamingCVAFilterRendererParameters setColorFilter:];
-[BWStreamingCVAFilterRendererParameters description];
-[BWStreamingCVAFilterRendererParameters copyWithZone:];
-[BWStreamingCVAFilterRendererParameters colorLookupCache];
-[BWStreamingCVAFilterRendererParameters backgroundColorLookupTable];
-[BWStreamingCVAFilterRendererParameters foregroundColorLookupTable];
-[BWStreamingCVAFilterRendererParameters initWithColorFilter:colorLookupCache:studioAndContourRenderingEnabled:stageRenderingEnabled:];
-[BWStreamingCVAFilterRendererParameters interpolationFractionComplete];
-[BWStreamingCVAFilterRendererParameters prepareForRenderingWithInputVideoFormat:];
-[BWStreamingCVAFilterRendererParameters renderingStrategy];
-[BWStreamingCVAFilterRendererParameters setBackgroundColorLookupTable:];
-[BWStreamingCVAFilterRendererParameters setForegroundColorLookupTable:];
-[BWStreamingCVAFilterRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:];
```
