# `AVPlayerLooper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"AVPlayerLooperInternal" _looper;
```

## Properties

```
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (Tq,R) loopCount;
@property (T@"NSArray",R) loopingPlayerItems;
```

## Class methods

```
+[AVPlayerLooper initialize];
+[AVPlayerLooper playerLooperWithPlayer:templateItem:];
+[AVPlayerLooper playerLooperWithPlayer:templateItem:timeRange:];
```

## Instance methods

```
-[AVPlayerLooper observeValueForKeyPath:ofObject:change:context:];
-[AVPlayerLooper init];
-[AVPlayerLooper dealloc];
-[AVPlayerLooper status];
-[AVPlayerLooper error];
-[AVPlayerLooper disableLooping];
-[AVPlayerLooper _changeStatusToFailedWithError:];
-[AVPlayerLooper _turnOffLooping];
-[AVPlayerLooper _calculateNumberOfCopiesNeeded];
-[AVPlayerLooper _cleanupAfterPlayingLastLoopingCopy];
-[AVPlayerLooper _configureLoopingItem:];
-[AVPlayerLooper _isWaitingForLastCopyToFinishSet];
-[AVPlayerLooper _setupLoopingReturningError:];
-[AVPlayerLooper initWithPlayer:templateItem:timeRange:];
-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:];
-[AVPlayerLooper loopCount];
-[AVPlayerLooper loopingPlayerItems];
```
