# `FigVideoDestination`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigVideoTarget=} _videoTarget;
@? _clientRebuildHandler;
i _rebuildState;
^{OpaqueFigReentrantMutex=} _mutex;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
```

## Properties

```
@property (Ti,R,N) rebuildState;
```

## Instance methods

```
-[FigVideoDestination addObserversForVideoTarget:];
-[FigVideoDestination init];
-[FigVideoDestination _setLoadingStateForVideoTarget:andPostNotificationIfStateChanged:];
-[FigVideoDestination removeObserversFromVideoTarget:];
-[FigVideoDestination dealloc];
-[FigVideoDestination copyVideoTarget];
-[FigVideoDestination setRebuildHandler:];
-[FigVideoDestination rebuild];
-[FigVideoDestination _setRebuildState:andPostNotificationIfStateChanged:];
-[FigVideoDestination setVideoTarget:];
-[FigVideoDestination initWithVideoTarget:];
-[FigVideoDestination rebuildState];
```
