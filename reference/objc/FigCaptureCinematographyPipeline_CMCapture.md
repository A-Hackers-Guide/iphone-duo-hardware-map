# `FigCaptureCinematographyPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 12 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
@"FigCaptureCinematographyPipelineConfiguration" _configuration;
@"BWVideoDepthNode" _videoDepthNode;
@"BWCinematicPerceptionNode" _perceptionNode;
@"BWRealtimeCinematographyNode" _cinematographyNode;
@"BWSmartStyleLearningNode" _smartStyleLearningNode;
@"NSString" _sourceID;
@"BWFanOutNode" _videoCaptureSplitterNode;
I _videoCaptureOutputIndex;
@"BWFanOutNode" _previewSplitterNode;
I _previewOutputIndex;
@"FigCaptureSmartStyle" _smartStyle;
@"FigCaptureTextureStyle" _textureStyle;
```

## Class methods

```
+[FigCaptureCinematographyPipeline initialize];
```

## Instance methods

```
-[FigCaptureCinematographyPipeline dealloc];
```
