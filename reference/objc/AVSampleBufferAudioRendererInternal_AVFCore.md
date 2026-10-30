# `AVSampleBufferAudioRendererInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"NSString" audioOutputDeviceUniqueID;
@"NSString" audioTimePitchAlgorithm;
Q allowedAudioSpatializationFormats;
^{opaqueMTAudioProcessingTap=} audioProcessingTap;
@"AVAudioSession" audioSession;
{?="mutex"^{OpaqueFigSimpleMutex}"requester"@"AVMediaDataRequester"} mediaDataRequester;
f rate;
f volume;
B muted;
@"AVScheduledAudioParameters" scheduledAudioParameters;
^{OpaqueCMTimebase=} readOnlyControlTimebase;
@"AVWeakReference" weakReferenceToSynchronizer;
@"AVWeakReference" weakReferenceToSelf;
q status;
@"NSError" error;
@"AVContentKeySession" weakContentKeySession;
^{opaqueCMFormatDescription=} lastFormatDescription;
^{OpaqueFigCPECryptor=} lastCryptor;
^{OpaqueFigSampleBufferAudioRenderer=} figAudioRenderer;
@"AVOutputContext" outputContext;
@"<AVLoggingIdentifier>" loggingIdentifier;
@? _cancelPendingSwiftAsyncEnqueueHandler;
@? _readyForMoreMediaDataHandler;
```
