# `AVStreamDataParserInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"<AVStreamDataParserOutputHandling>" _delegate;
@"NSObject<OS_dispatch_queue>" _threadSafetyQ;
q _status;
@"NSError" _error;
@"AVAsset" _asset;
@"NSMutableArray" _trackIDsNotProvidingMedia;
@"NSArray" _allowableMIMETypes;
^{OpaqueFigManifold=} _figManifold;
Q _typeIdOfInitialFigManifold;
^{OpaqueCMBlockBuffer=} _accumulatedInitializationData;
B _encounteredStreamDiscontinuity;
@"AVWeakReference" _legacyStreamSession;
@"AVContentKeySession" _defaultContentKeySession;
@"AVWeakReference" _contentKeySession;
@"AVContentKeyRequest" _sessionKeyRequest;
B _startedUsingInternalContentKeySession;
i _currentTrackID;
@"NSMutableDictionary" _tracksBecomingReadyByTrackID;
@"NSMutableArray" _samplesBeforeReady;
Q _samplesBeforeReadyTotalSize;
{?="value"q"timescale"i"flags"I"epoch"q} _samplesBeforeReadyTotalDuration;
@"NSMutableDictionary" _trackDecryptorsByTrackID;
@"NSMutableDictionary" _trackFormatDescriptionsByTrackID;
B _preferSandboxedParsing;
B _allowsHEVCInTransportStreams;
B _allowsLATMInTransportStreams;
{?="value"q"timescale"i"flags"I"epoch"q} _hintForStartTime;
```
