# `BWInferenceFusionTrackerMeanPixelCalculator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"<MTLCommandQueue>" _commandQueue;
@"MPSImageStatisticsMean" _meanFilter;
@"<MTLTexture>" _meanTexture;
```

## Instance methods

```
-[BWInferenceFusionTrackerMeanPixelCalculator initWithCommandQueue:];
-[BWInferenceFusionTrackerMeanPixelCalculator dealloc];
-[BWInferenceFusionTrackerMeanPixelCalculator asyncMeanPixelForBuffer:completionHandler:];
```
