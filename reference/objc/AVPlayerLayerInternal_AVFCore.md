# `AVPlayerLayerInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 54 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVNetworkPlaybackPerfHUDLayer" hudLayer;
@"NSObject<OS_dispatch_queue>" serialQueue;
B isPresentationLayer;
^{OpaqueFigSimpleMutex=} isReadyForDisplayMutex;
@"NSObject<OS_dispatch_queue>" configurationQueue;
@"AVKeyPathDependencyManager" dependencyManager;
@ playerItemHasEnqueuedVideoFrameListener;
@ windowSceneDidEnterBackgroundListener;
@ windowSceneWillEnterForegroundListener;
@"AVPlayer" player;
@"NSString" videoGravity;
@"NSDictionary" pixelBufferAttributes;
B lanczosDownscalingEnabled;
q lanczosDownscalingFactor;
@"FigBaseCALayer" maskLayer;
@"FigVideoContainerLayer" videoLayer;
@"FigSubtitleCALayer" subtitleLayer;
@"CALayer" subtitlePreviewLayer;
@"FigBaseCALayer" closedCaptionLayer;
@"AVPlayerLayer" interstitialLayer;
@"AVPlayerLayerSubtitlePreviewHelper" subtitlePreviewHelper;
{CGPoint="x"d"y"d} captionPreviewPosition;
B isLegibleDisplayEnabled;
B isForScrubbingOnly;
@"AVPlayerLayer" associatedRemoteModeLayer;
B willManageSublayersAsSwappedLayers;
q activeMode;
B isPartOfForegroundScene;
B showInterstitialInstead;
B useInterstitialLayerForVideoRect;
B signalsVideoRectChangeBeforeChangingContentsAspectRatio;
@"NSObject<OS_dispatch_source>" interstitialVisibilityUpdateTimer;
B overridesPreferredDynamicRangeForVideo;
B isReadyForDisplay;
@"AVPlayer" playerBeingObserved;
{CGSize="width"d"height"d} latestAppliedPresentationSize;
B preventsChangesToSublayerHierarchy;
@"NSDictionary" clientLayers;
B isPIPModeEnabled;
@"CALayer" placeholderContentLayerDuringPIPMode;
B isConnectedToSecondScreen;
{NSEdgeInsets="top"d"left"d"bottom"d"right"d} legibleContentInsets;
B honorContentScale;
d screenScale;
i lastWindowSceneEvent;
B isVisible;
@"AVSinkSubscriber" playerCurrentItemSink;
@"AVSinkSubscriber" currentItemPresentationSizeSink;
@"AVSinkSubscriber" currentItemTracksSink;
@"AVSinkSubscriber" currentItemNonForcedSubtitlesEnabledSink;
@"AVSinkSubscriber" playerIsDisplayingClosedCaptionsSink;
@"<AVLoggingIdentifier>" loggingIdentifier;
@ videoLayerIsReadyForDisplayDidChangeListener;
@ videoLayerPresentationSizeDidChangeListener;
```
