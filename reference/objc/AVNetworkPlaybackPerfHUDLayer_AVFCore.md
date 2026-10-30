# `AVNetworkPlaybackPerfHUDLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CATextLayer`
- 21 instance variables, 2 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _hudTimer;
@"AVPlayer" _player;
@"AVPlayerLayer" _playerLayer;
B _showHud;
B _spatialDiagnostics;
i _colorId;
d _opacity;
i _fontSizeInt;
B _updateUISettings;
i _hudXoffset;
i _hudYoffset;
f _hudUpdateInterval;
B _showCompleteURI;
q _prevVariantIdx;
q _prevStallCount;
q _totalStallCount;
@"NSNumber" _displayResolutionHeight;
@"NSNumber" _displayResolutionWidth;
@"NSNumber" _audioSpatializationMode;
B _requestInFlight;
@"NSMutableDictionary" _loadingStatusCache;
```

## Properties

```
@property (T@"AVPlayer",W,V_player) player;
@property (T@"AVPlayerLayer",W,V_playerLayer) playerLayer;
```

## Instance methods

```
-[AVNetworkPlaybackPerfHUDLayer hudEnabled];
-[AVNetworkPlaybackPerfHUDLayer setColor:];
-[AVNetworkPlaybackPerfHUDLayer player];
-[AVNetworkPlaybackPerfHUDLayer getHudSetting];
-[AVNetworkPlaybackPerfHUDLayer playerLayer];
-[AVNetworkPlaybackPerfHUDLayer setPlayerLayer:];
-[AVNetworkPlaybackPerfHUDLayer init];
-[AVNetworkPlaybackPerfHUDLayer dealloc];
-[AVNetworkPlaybackPerfHUDLayer currentItemTracksChanged];
-[AVNetworkPlaybackPerfHUDLayer currentItemChanged];
-[AVNetworkPlaybackPerfHUDLayer setBounds:];
-[AVNetworkPlaybackPerfHUDLayer setPlayer:];
-[AVNetworkPlaybackPerfHUDLayer _hudUpdateTrigger];
-[AVNetworkPlaybackPerfHUDLayer displayStringGenerator];
-[AVNetworkPlaybackPerfHUDLayer valueLoadedForKey:onObject:];
-[AVNetworkPlaybackPerfHUDLayer getScaleFactorForDisplaySize:];
-[AVNetworkPlaybackPerfHUDLayer startDispatchTimer];
-[AVNetworkPlaybackPerfHUDLayer copyPropertiesFromStringGenerator:];
-[AVNetworkPlaybackPerfHUDLayer readHudSettingsAndCallCompletionHandler:];
-[AVNetworkPlaybackPerfHUDLayer updateHudWithDisplayString:];
```
