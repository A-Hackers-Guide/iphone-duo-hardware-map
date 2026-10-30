# `AVPlayerCaptionLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 15 instance variables, 5 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"FigSubtitleCALayer" _subtitleLayer;
@"AVPlayerLayerIntermediateLayer" _closedCaptionLayer;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSObject<OS_dispatch_queue>" _configurationQueue;
@"AVPlayer" _player;
@"AVPlayerCaptionLayer" _interstitialLayer;
B _showInterstitialInstead;
@"CALayer" _subtitlePreviewLayer;
@"AVPlayerLayerSubtitlePreviewHelper" _subtitlePreviewHelper;
{CGPoint="x"d"y"d} _captionPreviewPosition;
@"AVPlayer" _playerBeingObserved;
@"NSSet" _KVOInvokers;
{NSEdgeInsets="top"d"left"d"bottom"d"right"d} _legibleContentInsets;
@"AVCaptionInsetsOptions" _insetsOptions;
{CGPoint="x"d"y"d} __captionPreviewPosition;
```

## Properties

```
@property (T{CGPoint=dd},N,V__captionPreviewPosition) _captionPreviewPosition;
@property (T@"AVPlayer",&,N) player;
@property (T{NSEdgeInsets=dddd},N) captionContentInsets;
@property (TB,N,GisOverscanSubtitleSupportEnabled) overscanSubtitleSupportEnabled;
@property (T@"AVCaptionInsetsOptions",C,N,V_insetsOptions) insetsOptions;
```

## Class methods

```
+[AVPlayerCaptionLayer captionLayerWithPlayer:];
```

## Instance methods

```
-[AVPlayerCaptionLayer player];
-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:];
-[AVPlayerCaptionLayer isOverscanSubtitleSupportEnabled];
-[AVPlayerCaptionLayer setCaptionPreviewProfileID:position:text:];
-[AVPlayerCaptionLayer init];
-[AVPlayerCaptionLayer stopShowingCaptionPreview];
-[AVPlayerCaptionLayer dealloc];
-[AVPlayerCaptionLayer setValue:forKeyPath:];
-[AVPlayerCaptionLayer setBounds:];
-[AVPlayerCaptionLayer setPlayer:];
-[AVPlayerCaptionLayer setOverscanSubtitleSupportEnabled:];
-[AVPlayerCaptionLayer layoutSublayers];
-[AVPlayerCaptionLayer _captionPreviewPosition];
-[AVPlayerCaptionLayer _closedCaptionLayer];
-[AVPlayerCaptionLayer _ensureSubtitlePreviewLayer];
-[AVPlayerCaptionLayer _interstitialLayer];
-[AVPlayerCaptionLayer _setCaptionPreviewPosition:];
-[AVPlayerCaptionLayer _setShowInterstitialInstead:];
-[AVPlayerCaptionLayer _showInterstitialInstead];
-[AVPlayerCaptionLayer _startObservingPlayer:];
-[AVPlayerCaptionLayer _stopObservingPlayer:];
-[AVPlayerCaptionLayer _subtitleLayer];
-[AVPlayerCaptionLayer _updateSubtitlePreviewLayerImage];
-[AVPlayerCaptionLayer captionContentInsets];
-[AVPlayerCaptionLayer insetsOptions];
-[AVPlayerCaptionLayer setCaptionContentInsets:];
-[AVPlayerCaptionLayer setInsetsOptions:];
-[AVPlayerCaptionLayer set_captionPreviewPosition:];
```
