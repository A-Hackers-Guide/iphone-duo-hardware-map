# `BWTextureStyleInfoMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _boxedMetadataOutput;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
B _previousGeneratedMetadataBufferWasEmpty;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
I _localIDForTextureStyleInfoPlistMetadata_BE;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_boxedMetadataOutput) boxedMetadataOutput;
```

## Class methods

```
+[BWTextureStyleInfoMetadataNode initialize];
```

## Instance methods

```
-[BWTextureStyleInfoMetadataNode renderSampleBuffer:forInput:];
-[BWTextureStyleInfoMetadataNode init];
-[BWTextureStyleInfoMetadataNode dealloc];
-[BWTextureStyleInfoMetadataNode hasNonLiveConfigurationChanges];
-[BWTextureStyleInfoMetadataNode boxedMetadataOutput];
-[BWTextureStyleInfoMetadataNode handleDroppedSample:forInput:];
-[BWTextureStyleInfoMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWTextureStyleInfoMetadataNode passthruOutput];
-[BWTextureStyleInfoMetadataNode nodeSubType];
-[BWTextureStyleInfoMetadataNode didSelectFormat:forInput:];
-[BWTextureStyleInfoMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWTextureStyleInfoMetadataNode nodeType];
```
