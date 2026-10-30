# `BWCameraInfoMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 13 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _generateLivePhotosMetadata;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
^{opaqueCMFormatDescription=} _formatSpecificBoxedMetadataFormatDescription;
^{opaqueCMFormatDescription=} _basicBoxedMetadataFormatDescription;
B _previousGeneratedMetadataBufferWasEmpty;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _boxedMetadataOutput;
{?="width"i"height"i} _videoDimensions;
I _localIDForLivePhotosMetadata_BE;
I _localIDForOpticalCenterMetadata_BE;
B _generateGreenGhostMetadata;
B _updateBoxedMetadataFormatDescriptionForFirstBuffer;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_boxedMetadataOutput) boxedMetadataOutput;
```

## Class methods

```
+[BWCameraInfoMetadataNode initialize];
```

## Instance methods

```
-[BWCameraInfoMetadataNode renderSampleBuffer:forInput:];
-[BWCameraInfoMetadataNode dealloc];
-[BWCameraInfoMetadataNode initForLivePhotosMetadata:generateDebugMetadata:generateMotionMetadata:];
-[BWCameraInfoMetadataNode boxedMetadataOutput];
-[BWCameraInfoMetadataNode handleDroppedSample:forInput:];
-[BWCameraInfoMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWCameraInfoMetadataNode passthruOutput];
-[BWCameraInfoMetadataNode nodeSubType];
-[BWCameraInfoMetadataNode didSelectFormat:forInput:];
-[BWCameraInfoMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCameraInfoMetadataNode nodeType];
```
