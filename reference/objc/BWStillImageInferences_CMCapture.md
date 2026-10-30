# `BWStillImageInferences`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _inferenceBufferByAttachedMediaKey;
@"NSMutableDictionary" _metadataByAttachedMediaKey;
@"NSMutableDictionary" _inferenceByAttachmentKey;
@"NSDictionary" _inferenceAttachedMediaMetadata;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_inferenceAttachedMediaMetadata) inferenceAttachedMediaMetadata;
@property (T@"NSArray",R,N) inferenceBufferKeys;
@property (T@"NSArray",R,N) metadataKeys;
@property (T@"NSArray",R,N) inferenceKeys;
@property (T@"NSArray",R,N) inferenceAttachedMediaMetadataKeys;
```

## Class methods

```
+[BWStillImageInferences initialize];
```

## Instance methods

```
-[BWStillImageInferences init];
-[BWStillImageInferences dealloc];
-[BWStillImageInferences description];
-[BWStillImageInferences addInference:inferenceAttachmentKey:];
-[BWStillImageInferences addInferenceAttachedMediaMetadata:];
-[BWStillImageInferences addInferenceBuffer:metadata:inferenceAttachedMediaKey:];
-[BWStillImageInferences createSampleBufferForInferenceForAttachedMediaKey:pts:];
-[BWStillImageInferences inferenceAttachedMediaMetadata];
-[BWStillImageInferences inferenceAttachedMediaMetadataKeys];
-[BWStillImageInferences inferenceBufferForAttachedMediaKey:];
-[BWStillImageInferences inferenceBufferKeys];
-[BWStillImageInferences inferenceForAttachmentKey:];
-[BWStillImageInferences inferenceKeys];
-[BWStillImageInferences mergeInferences:];
-[BWStillImageInferences metadataForAttachedMediaKey:];
-[BWStillImageInferences metadataKeys];
```
