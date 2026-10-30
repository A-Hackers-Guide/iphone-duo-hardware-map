# `BWMonocularDepthConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _monocularDepthType;
q _depthPrioritization;
{?="width"i"height"i} _depthDataDimensions;
B _appliesFinalCropRect;
```

## Properties

```
@property (TI,R,N,V_monocularDepthType) monocularDepthType;
@property (Tq,R,N,V_depthPrioritization) depthPrioritization;
@property (T{?=ii},N,V_depthDataDimensions) depthDataDimensions;
@property (TB,N,V_appliesFinalCropRect) appliesFinalCropRect;
```

## Instance methods

```
-[BWMonocularDepthConfiguration setDepthDataDimensions:];
-[BWMonocularDepthConfiguration appliesFinalCropRect];
-[BWMonocularDepthConfiguration depthDataDimensions];
-[BWMonocularDepthConfiguration setAppliesFinalCropRect:];
-[BWMonocularDepthConfiguration description];
-[BWMonocularDepthConfiguration depthPrioritization];
-[BWMonocularDepthConfiguration initWithInferenceType:monocularDepthType:];
-[BWMonocularDepthConfiguration monocularDepthType];
```
