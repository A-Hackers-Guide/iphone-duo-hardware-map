# `AVPlayerItemAccessLogEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 27 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"AVPlayerItemAccessLogEventInternal" _playerItemAccessLogEvent;
```

## Properties

```
@property (Tq,R,N) numberOfSegmentsDownloaded;
@property (Tq,R,N) numberOfMediaRequests;
@property (T@"NSDate",R,N) playbackStartDate;
@property (T@"NSString",R,N) URI;
@property (T@"NSString",R,N) serverAddress;
@property (Tq,R,N) numberOfServerAddressChanges;
@property (T@"NSString",R,N) playbackSessionID;
@property (Td,R,N) playbackStartOffset;
@property (Td,R,N) segmentsDownloadedDuration;
@property (Td,R,N) durationWatched;
@property (Tq,R,N) numberOfStalls;
@property (Tq,R,N) numberOfBytesTransferred;
@property (Td,R,N) transferDuration;
@property (Td,R,N) observedBitrate;
@property (Td,R,N) indicatedBitrate;
@property (Td,R,N) indicatedAverageBitrate;
@property (Td,R,N) averageVideoBitrate;
@property (Td,R,N) averageAudioBitrate;
@property (Tq,R,N) numberOfDroppedVideoFrames;
@property (Td,R,N) startupTime;
@property (Tq,R,N) downloadOverdue;
@property (Td,R,N) observedMaxBitrate;
@property (Td,R,N) observedMinBitrate;
@property (Td,R,N) observedBitrateStandardDeviation;
@property (T@"NSString",R,N) playbackType;
@property (Tq,R,N) mediaRequestsWWAN;
@property (Td,R,N) switchBitrate;
```

## Instance methods

```
-[AVPlayerItemAccessLogEvent playbackStartDate];
-[AVPlayerItemAccessLogEvent initWithDictionary:];
-[AVPlayerItemAccessLogEvent init];
-[AVPlayerItemAccessLogEvent dealloc];
-[AVPlayerItemAccessLogEvent averageAudioBitrate];
-[AVPlayerItemAccessLogEvent averageVideoBitrate];
-[AVPlayerItemAccessLogEvent serverAddress];
-[AVPlayerItemAccessLogEvent URI];
-[AVPlayerItemAccessLogEvent serviceIdentifier];
-[AVPlayerItemAccessLogEvent performanceMetrics];
-[AVPlayerItemAccessLogEvent copyWithZone:];
-[AVPlayerItemAccessLogEvent downloadOverdue];
-[AVPlayerItemAccessLogEvent durationWatched];
-[AVPlayerItemAccessLogEvent entryReasonCode];
-[AVPlayerItemAccessLogEvent observedBitrate];
-[AVPlayerItemAccessLogEvent _common_init];
-[AVPlayerItemAccessLogEvent currentObservedBitrate];
-[AVPlayerItemAccessLogEvent indicatedAverageBitrate];
-[AVPlayerItemAccessLogEvent indicatedBitrate];
-[AVPlayerItemAccessLogEvent mediaRequestsWWAN];
-[AVPlayerItemAccessLogEvent numberOfBytesTransferred];
-[AVPlayerItemAccessLogEvent numberOfDroppedVideoFrames];
-[AVPlayerItemAccessLogEvent numberOfMediaRequests];
-[AVPlayerItemAccessLogEvent numberOfSegmentsDownloaded];
-[AVPlayerItemAccessLogEvent numberOfServerAddressChanges];
-[AVPlayerItemAccessLogEvent numberOfStalls];
-[AVPlayerItemAccessLogEvent observedBitrateStandardDeviation];
-[AVPlayerItemAccessLogEvent observedMaxBitrate];
-[AVPlayerItemAccessLogEvent observedMinBitrate];
-[AVPlayerItemAccessLogEvent playbackSessionID];
-[AVPlayerItemAccessLogEvent playbackStartOffset];
-[AVPlayerItemAccessLogEvent playbackType];
-[AVPlayerItemAccessLogEvent segmentsDownloadedDuration];
-[AVPlayerItemAccessLogEvent startupTime];
-[AVPlayerItemAccessLogEvent switchBitrate];
-[AVPlayerItemAccessLogEvent transferDuration];
```
