# `BWCinematicVideoMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 13 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _metadataFormatDescription;
B _previousGeneratedMetadataBufferWasEmpty;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _metadataOutput;
I _localIDForAperture_BE;
I _localIDForDisparity_BE;
I _localIDForCinematographyMetadata_BE;
I _localIDForRenderingMetadata_BE;
I _localIDForDialogueLevel_BE;
I _localIDForAmbienceLevel_BE;
B _disabled;
B _useRawCinematography;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_metadataOutput) metadataOutput;
@property (TB,N,V_disabled) disabled;
@property (TB,N,V_useRawCinematography) useRawCinematography;
```

## Class methods

```
+[BWCinematicVideoMetadataNode initialize];
```

## Instance methods

```
-[BWCinematicVideoMetadataNode metadataOutput];
-[BWCinematicVideoMetadataNode disabled];
-[BWCinematicVideoMetadataNode renderSampleBuffer:forInput:];
-[BWCinematicVideoMetadataNode init];
-[BWCinematicVideoMetadataNode dealloc];
-[BWCinematicVideoMetadataNode handleDroppedSample:forInput:];
-[BWCinematicVideoMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWCinematicVideoMetadataNode passthruOutput];
-[BWCinematicVideoMetadataNode nodeSubType];
-[BWCinematicVideoMetadataNode didSelectFormat:forInput:];
-[BWCinematicVideoMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCinematicVideoMetadataNode setDisabled:];
-[BWCinematicVideoMetadataNode nodeType];
-[BWCinematicVideoMetadataNode initWithMetadataMode:];
-[BWCinematicVideoMetadataNode setUseRawCinematography:];
-[BWCinematicVideoMetadataNode useRawCinematography];
```
