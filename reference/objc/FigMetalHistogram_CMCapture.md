# `FigMetalHistogram`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
[1@"<MTLComputePipelineState>"] _pipelineStates;
```

## Instance methods

```
-[FigMetalHistogram initWithMetalContext:];
-[FigMetalHistogram singleComponentCPUAverageInputPixelBuffer:validRect:outputAverage:];
-[FigMetalHistogram singleComponentCPUHistogramInputPixelBuffer:validRect:outputHistogram:];
-[FigMetalHistogram singleComponentCPUHistogramInputPixelBuffer:validRect:subSampleX:subSampleY:outputHistogram:];
-[FigMetalHistogram singleComponentGPUAverageInputPixelBuffer:validRect:outputAverage:];
-[FigMetalHistogram singleComponentGPUHistogramInputPixelBuffer:validRect:outputHistogram:];
```
