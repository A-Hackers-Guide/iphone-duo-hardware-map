# `BWDeepFusionInputBuffer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _buffer;
Q _type;
Q _captureFrameFlags;
@"NSDictionary" _metadata;
^{__CVBuffer=} _lscGainMap;
@"NSDictionary" _lscGainMapParameters;
```

## Properties

```
@property (T^{__CVBuffer=},R,N,V_buffer) buffer;
@property (TQ,R,N,V_type) type;
@property (TQ,R,N,V_captureFrameFlags) captureFrameFlags;
@property (T@"NSDictionary",R,N,V_metadata) metadata;
@property (T^{__CVBuffer=},R,N,V_lscGainMap) lscGainMap;
@property (T@"NSDictionary",R,N,V_lscGainMapParameters) lscGainMapParameters;
```

## Instance methods

```
-[BWDeepFusionInputBuffer buffer];
-[BWDeepFusionInputBuffer dealloc];
-[BWDeepFusionInputBuffer metadata];
-[BWDeepFusionInputBuffer type];
-[BWDeepFusionInputBuffer captureFrameFlags];
-[BWDeepFusionInputBuffer initWithBuffer:type:captureFrameFlags:metadata:lscGainMap:lscGainMapParameters:];
-[BWDeepFusionInputBuffer lscGainMap];
-[BWDeepFusionInputBuffer lscGainMapParameters];
-[BWDeepFusionInputBuffer releasePixelBuffers];
```
