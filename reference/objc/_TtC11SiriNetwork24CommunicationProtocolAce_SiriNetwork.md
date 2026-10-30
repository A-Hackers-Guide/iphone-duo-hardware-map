# `_TtC11SiriNetwork24CommunicationProtocolAce`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 26 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
SiriNetwork.CommunicationProtocolDelegate ? delegate;
DispatchQueue queue;
Foundation.Data ? bufferedInputData;
Foundation.Data bufferedProviderHeaderOutputData;
Foundation.Data ? bufferedGeneralOutputData;
Foundation.Data ? bufferedUncompressedData;
Swift.Unmanaged __C.CFHTTPMessage ? httpResponseHeader;
SiriNetwork.DataDecompressing ? inputDecompressor;
SiriNetwork.DataCompressing ? outputCompressor;
(objc_protocol 0x2adeddcf0) ? aceHeaderTimerSource;
_$sSu aceHeaderTimerFireCount;
_$sSD -> Swift.UInt32 _$sSbc outstandingBarriers;
Swift.UInt32 currentBarrierIndex;
(objc_protocol 0x2adeddcf0) ? pingTimerSource;
Swift.UInt32 currentPingIndex;
SiriNetwork.PingInfo ? pingInfo;
Swift.Bool sendPings;
Foundation.Data ? lastInputData;
_$sSVSg lastInputDataPointer;
_$sSi lastInputLength;
_$sSi inputLengthUnchangedCounter;
_$sSVSg lastOutputDataPointer;
_$sSi lastOutputLength;
_$sSi outputLengthUnchangedCounter;
Foundation.Data ? safetyNetBuffer;
os.OSAllocatedUnfairLock _$syt compressorLock;
```
