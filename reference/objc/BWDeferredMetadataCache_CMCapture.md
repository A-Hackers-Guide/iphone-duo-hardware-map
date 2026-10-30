# `BWDeferredMetadataCache`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
@"BWFigCaptureStream" _stream;
i _numberOfExpectedSampleBuffersForEachPTS;
[5{BWDeferredMetadataCacheEntry="pts"{?="value"q"timescale"i"flags"I"epoch"q}"metadataDict"^{__CFDictionary}"servedOutputs"^{__CFSet}"useCount"s"age"s}] _cache;
```

## Properties

```
@property (Ti,N) numberOfExpectedSampleBuffersForEachPTS;
```

## Class methods

```
+[BWDeferredMetadataCache initialize];
```

## Instance methods

```
-[BWDeferredMetadataCache flush];
-[BWDeferredMetadataCache dealloc];
-[BWDeferredMetadataCache addMetadataAttachmentToSampleBuffer:withDutyCycleMetadataCache:outputID:];
-[BWDeferredMetadataCache initWithCaptureStream:atomicTransactions:];
-[BWDeferredMetadataCache numberOfExpectedSampleBuffersForEachPTS];
-[BWDeferredMetadataCache setNumberOfExpectedSampleBuffersForEachPTS:];
```
