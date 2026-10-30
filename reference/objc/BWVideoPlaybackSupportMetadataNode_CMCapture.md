# `BWVideoPlaybackSupportMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 7 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _boxedMetadataOutput;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
I _localIDOfLuxMetadata_BE;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
B _previousGeneratedMetadataBufferWasEmpty;
I _prevSceneIlluminationValue;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_boxedMetadataOutput) boxedMetadataOutput;
```

## Class methods

```
+[BWVideoPlaybackSupportMetadataNode initialize];
```

## Instance methods

```
-[BWVideoPlaybackSupportMetadataNode renderSampleBuffer:forInput:];
-[BWVideoPlaybackSupportMetadataNode init];
-[BWVideoPlaybackSupportMetadataNode dealloc];
-[BWVideoPlaybackSupportMetadataNode hasNonLiveConfigurationChanges];
-[BWVideoPlaybackSupportMetadataNode boxedMetadataOutput];
-[BWVideoPlaybackSupportMetadataNode handleDroppedSample:forInput:];
-[BWVideoPlaybackSupportMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWVideoPlaybackSupportMetadataNode passthruOutput];
-[BWVideoPlaybackSupportMetadataNode nodeSubType];
-[BWVideoPlaybackSupportMetadataNode didSelectFormat:forInput:];
-[BWVideoPlaybackSupportMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWVideoPlaybackSupportMetadataNode nodeType];
```
