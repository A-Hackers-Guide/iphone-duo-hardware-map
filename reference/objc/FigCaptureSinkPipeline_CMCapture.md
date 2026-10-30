# `FigCaptureSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _sinkID;
@"BWNodeOutput" _upstreamOutput;
```

## Properties

```
@property (T@"NSString",R,N,V_sinkID) sinkID;
@property (TB,N) discardsSampleData;
```

## Instance methods

```
-[FigCaptureSinkPipeline dealloc];
-[FigCaptureSinkPipeline discardsSampleData];
-[FigCaptureSinkPipeline sinkID];
-[FigCaptureSinkPipeline setDiscardsSampleData:];
-[FigCaptureSinkPipeline initWithGraph:name:sinkID:];
-[FigCaptureSinkPipeline setUpstreamOutput:];
```
