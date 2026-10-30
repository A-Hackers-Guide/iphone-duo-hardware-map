# `FigVideoContainerLayerForVideoReceiver`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigVideoContainerLayer`
- 3 instance variables, 3 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"FigVideoContainerLayerForVideoReceiver" _proxyLayer;
{?="videoLayer"@"FigVideoLayer""videoDestination"@"FigVideoDestination""videoReceiver"^{OpaqueFigVideoReceiver}"hideLayerForEmptyConfig"B"lock"^{OpaqueFigSimpleMutex}} _backing;
{?="readyForDisplay"B"presentationSize"{CGSize="width"d"height"d}"lock"^{OpaqueFigSimpleMutex}} _configuration;
```

## Properties

```
@property (TB,R,N,GisReadyForDisplay) readyForDisplay;
@property (T{CGSize=dd},R,N) presentationSize;
@property (T@"FigVideoDestination",R,N) videoDestination;
```

## Instance methods

```
-[FigVideoContainerLayerForVideoReceiver _createVideoTargetForVideoReceiver:];
-[FigVideoContainerLayerForVideoReceiver videoLayer];
-[FigVideoContainerLayerForVideoReceiver isReadyForDisplay];
-[FigVideoContainerLayerForVideoReceiver setPresentationSize:];
-[FigVideoContainerLayerForVideoReceiver init];
-[FigVideoContainerLayerForVideoReceiver initWithUUID:];
-[FigVideoContainerLayerForVideoReceiver dealloc];
-[FigVideoContainerLayerForVideoReceiver _createFigVideoReceiverWithVideoLayer:];
-[FigVideoContainerLayerForVideoReceiver initWithHideForEmptyVideoReceiverConfiguration:];
-[FigVideoContainerLayerForVideoReceiver proxyLayer];
-[FigVideoContainerLayerForVideoReceiver rebuild];
-[FigVideoContainerLayerForVideoReceiver presentationSize];
-[FigVideoContainerLayerForVideoReceiver setVideoLayer:];
-[FigVideoContainerLayerForVideoReceiver setReadyForDisplay:];
-[FigVideoContainerLayerForVideoReceiver _subscribeToVideoReceiver:];
-[FigVideoContainerLayerForVideoReceiver initWithUUID:videoLayer:hideForEmptyVideoReceiverConfiguration:];
-[FigVideoContainerLayerForVideoReceiver videoDestination];
-[FigVideoContainerLayerForVideoReceiver initWithVideoLayer:];
-[FigVideoContainerLayerForVideoReceiver rebuildCommittingSynchronously:];
-[FigVideoContainerLayerForVideoReceiver _unsubscribeFromVideoReceiver:];
-[FigVideoContainerLayerForVideoReceiver setProxyLayer:];
-[FigVideoContainerLayerForVideoReceiver copyDisplayedVideoFrame];
```
