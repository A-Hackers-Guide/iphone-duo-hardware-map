# `JTVideoMediaUtils`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _cachedAssetInformationValid;
B _cacheWillDieDuringLoad;
f _cachedFrameRate;
I _cachedCodec4cc;
i _cachedDurationAt30fps;
@"PVColorSpace" _cachedColorSpace;
Q _cachedVideoTrackCount;
Q _cachedAudioTrackCount;
{CGSize="width"d"height"d} _cachedNaturalSize;
{?="value"q"timescale"i"flags"I"epoch"q} _cachedPreciseAssetDuration;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _cachedTransform;
```

## Properties

```
@property (TB,N,V_cachedAssetInformationValid) cachedAssetInformationValid;
@property (T{CGSize=dd},N,V_cachedNaturalSize) cachedNaturalSize;
@property (Tf,N,V_cachedFrameRate) cachedFrameRate;
@property (T{CGAffineTransform=dddddd},N,V_cachedTransform) cachedTransform;
@property (TI,N,V_cachedCodec4cc) cachedCodec4cc;
@property (T@"PVColorSpace",&,N,V_cachedColorSpace) cachedColorSpace;
@property (Ti,N,V_cachedDurationAt30fps) cachedDurationAt30fps;
@property (T{?=qiIq},N,V_cachedPreciseAssetDuration) cachedPreciseAssetDuration;
@property (TQ,N,V_cachedVideoTrackCount) cachedVideoTrackCount;
@property (TQ,N,V_cachedAudioTrackCount) cachedAudioTrackCount;
@property (TB,N,V_cacheWillDieDuringLoad) cacheWillDieDuringLoad;
```

## Instance methods

```
-[JTVideoMediaUtils transform];
-[JTVideoMediaUtils colorSpace];
-[JTVideoMediaUtils isProRes];
-[JTVideoMediaUtils frameRate];
-[JTVideoMediaUtils cachedFrameRate];
-[JTVideoMediaUtils setCachedFrameRate:];
-[JTVideoMediaUtils naturalSizeWithIsMissing:asset:];
-[JTVideoMediaUtils setCachedAssetInformationValid:];
-[JTVideoMediaUtils cachedTransform];
-[JTVideoMediaUtils cacheTrackInformationWithAVAsset:];
-[JTVideoMediaUtils cacheWillDieDuringLoad];
-[JTVideoMediaUtils cachedAssetInformationValid];
-[JTVideoMediaUtils cachedAudioTrackCount];
-[JTVideoMediaUtils cachedCodec4cc];
-[JTVideoMediaUtils cachedColorSpace];
-[JTVideoMediaUtils cachedDurationAt30fps];
-[JTVideoMediaUtils cachedNaturalSize];
-[JTVideoMediaUtils cachedPreciseAssetDuration];
-[JTVideoMediaUtils cachedVideoTrackCount];
-[JTVideoMediaUtils durationAt30fpsWithAssetDuration:];
-[JTVideoMediaUtils hasAudibleCharacteristicWithIsMissing:];
-[JTVideoMediaUtils hasAudioTracks];
-[JTVideoMediaUtils hasVideoTracks];
-[JTVideoMediaUtils invalidateCachedAssetInformation];
-[JTVideoMediaUtils isOriginalHEVC4k];
-[JTVideoMediaUtils isUnsupportedAudio];
-[JTVideoMediaUtils requestAVAssetAsyncWithAsset:needsDerivativeMedia:frameRate:completion:];
-[JTVideoMediaUtils setCacheWillDieDuringLoad:];
-[JTVideoMediaUtils setCachedAudioTrackCount:];
-[JTVideoMediaUtils setCachedCodec4cc:];
-[JTVideoMediaUtils setCachedColorSpace:];
-[JTVideoMediaUtils setCachedDurationAt30fps:];
-[JTVideoMediaUtils setCachedNaturalSize:];
-[JTVideoMediaUtils setCachedPreciseAssetDuration:];
-[JTVideoMediaUtils setCachedTransform:];
-[JTVideoMediaUtils setCachedVideoTrackCount:];
```
