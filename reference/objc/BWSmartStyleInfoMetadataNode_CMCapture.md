# `BWSmartStyleInfoMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 7 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _boxedMetadataOutput;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
B _currentRecordingSupportsReversibility;
B _previousGeneratedMetadataBufferWasEmpty;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
I _localIDForSmartStyleInfoPlistMetadata_BE;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_boxedMetadataOutput) boxedMetadataOutput;
```

## Class methods

```
+[BWSmartStyleInfoMetadataNode initialize];
```

## Instance methods

```
-[BWSmartStyleInfoMetadataNode renderSampleBuffer:forInput:];
-[BWSmartStyleInfoMetadataNode init];
-[BWSmartStyleInfoMetadataNode dealloc];
-[BWSmartStyleInfoMetadataNode hasNonLiveConfigurationChanges];
-[BWSmartStyleInfoMetadataNode boxedMetadataOutput];
-[BWSmartStyleInfoMetadataNode handleDroppedSample:forInput:];
-[BWSmartStyleInfoMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWSmartStyleInfoMetadataNode passthruOutput];
-[BWSmartStyleInfoMetadataNode nodeSubType];
-[BWSmartStyleInfoMetadataNode didSelectFormat:forInput:];
-[BWSmartStyleInfoMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSmartStyleInfoMetadataNode nodeType];
```
