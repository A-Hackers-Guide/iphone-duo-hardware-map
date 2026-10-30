# `BWPreviewHistogramNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 3 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _msrHistogramsEnabled;
B _ispHistogramsEnabled;
B _ispHistogramDownsamplingEnabled;
```

## Properties

```
@property (TB,N,V_msrHistogramsEnabled) msrHistogramsEnabled;
@property (TB,N,V_ispHistogramsEnabled) ispHistogramsEnabled;
```

## Class methods

```
+[BWPreviewHistogramNode initialize];
```

## Instance methods

```
-[BWPreviewHistogramNode renderSampleBuffer:forInput:];
-[BWPreviewHistogramNode init];
-[BWPreviewHistogramNode hasNonLiveConfigurationChanges];
-[BWPreviewHistogramNode setIspHistogramsEnabled:];
-[BWPreviewHistogramNode msrHistogramsEnabled];
-[BWPreviewHistogramNode ispHistogramsEnabled];
-[BWPreviewHistogramNode setMsrHistogramsEnabled:];
-[BWPreviewHistogramNode nodeSubType];
-[BWPreviewHistogramNode nodeType];
```
