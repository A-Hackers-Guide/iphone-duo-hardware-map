# `BWPiecemealEncodingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"BWPhotoEncoderController" _photoEncoderController;
```

## Class methods

```
+[BWPiecemealEncodingNode initialize];
```

## Instance methods

```
-[BWPiecemealEncodingNode sharePhotoEncoderControllerForPiecemealEncoding:];
-[BWPiecemealEncodingNode renderSampleBuffer:forInput:];
-[BWPiecemealEncodingNode dealloc];
-[BWPiecemealEncodingNode _releaseResources];
-[BWPiecemealEncodingNode didReachEndOfDataForConfigurationID:input:];
-[BWPiecemealEncodingNode initWithNodeConfiguration:];
-[BWPiecemealEncodingNode didSelectFormat:forInput:];
-[BWPiecemealEncodingNode nodeType];
```
