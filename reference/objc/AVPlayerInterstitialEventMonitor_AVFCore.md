# `AVPlayerInterstitialEventMonitor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"AVPlayer" _primaryPlayer;
@"AVQueuePlayer" _interstitialPlayer;
@"AVWeakReference" _weakReference;
^{OpaqueFigPlayerInterstitialCoordinator=} _observedCoord;
@"NSObject<OS_dispatch_queue>" _ivarQueue;
@"AVPlayerInterstitialEvent" _cachedCurrentEvent;
```

## Properties

```
@property (T@"AVPlayer",R,W,N) primaryPlayer;
@property (T@"AVQueuePlayer",R,N) interstitialPlayer;
@property (T@"NSArray",R,C) events;
@property (T@"AVPlayerInterstitialEvent",R) currentEvent;
@property (Tq,R) currentEventSkippableState;
@property (T@"NSString",R) currentEventSkipControlLabel;
```

## Class methods

```
+[AVPlayerInterstitialEventMonitor interstitialEventMonitorWithPrimaryPlayer:];
```

## Instance methods

```
-[AVPlayerInterstitialEventMonitor currentEvent];
-[AVPlayerInterstitialEventMonitor init];
-[AVPlayerInterstitialEventMonitor dealloc];
-[AVPlayerInterstitialEventMonitor events];
-[AVPlayerInterstitialEventMonitor _addMonitorListeners:];
-[AVPlayerInterstitialEventMonitor _removeMonitorListeners];
-[AVPlayerInterstitialEventMonitor _setCachedCurrentEvent:];
-[AVPlayerInterstitialEventMonitor _updateCachedCurrentEvent];
-[AVPlayerInterstitialEventMonitor currentEventSkipControlLabel];
-[AVPlayerInterstitialEventMonitor currentEventSkippableState];
-[AVPlayerInterstitialEventMonitor initWithPrimaryPlayer:];
-[AVPlayerInterstitialEventMonitor interstitialPlayer];
-[AVPlayerInterstitialEventMonitor makeCopyOf:immutable:];
-[AVPlayerInterstitialEventMonitor primaryPlayer];
```
