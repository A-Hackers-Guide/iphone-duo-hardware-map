# `BWTimewarpMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 12 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
^{OpaqueCMClock=} _sourceClock;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
@"BWNodeOutput" _passthruOutput;
@"BWNodeOutput" _boxedMetadataOutput;
I _localIDForPreTimewarpFrameMillisecondsSince1970Metadata_BE;
I _localIDForTimewarpDecimationTagMetadata_BE;
I _localIDForTimewarpDecimationLevelMetadata_BE;
I _localIDForTimewarpSequenceCaptureIDMetadata_BE;
{?="value"q"timescale"i"flags"I"epoch"q} _firstPreTimewarpPTSInHostTime;
Q _firstPreTimewarpPTSAsMillisecondsSince1970;
C _maxDecimationLevel;
I _maxSequenceNumber;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_passthruOutput) passthruOutput;
@property (T@"BWNodeOutput",R,N,V_boxedMetadataOutput) boxedMetadataOutput;
```

## Class methods

```
+[BWTimewarpMetadataNode initialize];
```

## Instance methods

```
-[BWTimewarpMetadataNode renderSampleBuffer:forInput:];
-[BWTimewarpMetadataNode dealloc];
-[BWTimewarpMetadataNode boxedMetadataOutput];
-[BWTimewarpMetadataNode handleDroppedSample:forInput:];
-[BWTimewarpMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWTimewarpMetadataNode passthruOutput];
-[BWTimewarpMetadataNode nodeSubType];
-[BWTimewarpMetadataNode didSelectFormat:forInput:];
-[BWTimewarpMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWTimewarpMetadataNode nodeType];
-[BWTimewarpMetadataNode initForTimewarpMode:sourceClock:];
```
