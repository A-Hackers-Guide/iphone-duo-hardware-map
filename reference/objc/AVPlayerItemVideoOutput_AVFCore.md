# `AVPlayerItemVideoOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemOutput`
- 1 instance variables, 2 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"AVPlayerItemVideoOutputInternal" _videoOutputInternal;
```

## Properties

```
@property (T@"<AVPlayerItemOutputPullDelegate>",R,W) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Instance methods

```
-[AVPlayerItemVideoOutput setDelegate:queue:];
-[AVPlayerItemVideoOutput init];
-[AVPlayerItemVideoOutput dealloc];
-[AVPlayerItemVideoOutput isDefunct];
-[AVPlayerItemVideoOutput delegate];
-[AVPlayerItemVideoOutput initWithPixelBufferAttributes:];
-[AVPlayerItemVideoOutput delegateQueue];
-[AVPlayerItemVideoOutput _attachToPlayerItem:];
-[AVPlayerItemVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:];
-[AVPlayerItemVideoOutput _detachFromPlayerItem];
-[AVPlayerItemVideoOutput _dispatchOutputMediaDataWillChange];
-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed];
-[AVPlayerItemVideoOutput _pixelBufferAttributes];
-[AVPlayerItemVideoOutput _respondToPlayerItemFormatDescriptionsChange];
-[AVPlayerItemVideoOutput _setTagBuffersWithConversionInformation];
-[AVPlayerItemVideoOutput _setTimebase:];
-[AVPlayerItemVideoOutput _startObservingTimebaseNotificationsForTimebase:];
-[AVPlayerItemVideoOutput _stopObservingTimebaseNotificationsForTimebase:];
-[AVPlayerItemVideoOutput _visualContext];
-[AVPlayerItemVideoOutput clientStateOnRequestedMediaDataChangeNotification];
-[AVPlayerItemVideoOutput copyPixelBufferForItemTime:itemTimeForDisplay:];
-[AVPlayerItemVideoOutput copyPixelBufferForItemTime:remove:itemTimeForDisplay:];
-[AVPlayerItemVideoOutput earliestAvailablePixelBufferItemTime];
-[AVPlayerItemVideoOutput hasNewPixelBufferForItemTime:];
-[AVPlayerItemVideoOutput initWithOutputSettings:];
-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeAsSoonAsPossible];
-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeWithAdvanceInterval:];
-[AVPlayerItemVideoOutput setSuppressesPlayerRendering:];
-[AVPlayerItemVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:];
-[AVPlayerItemVideoOutput suppressesPlayerRendering];
```
