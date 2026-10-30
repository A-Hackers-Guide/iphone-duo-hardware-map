# `SBRingerNoticeUICoordinating` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,N,GisRingerSilent) ringerSilent;
@property (Tf,N) volume;
@property (TB,R,N,GisPresented) presented;
@property (TB,R,N,GisActivatedForPreviewing) activatedForPreviewing;
```

## Instance methods

```
-[SBRingerNoticeUICoordinating isPresented];
-[SBRingerNoticeUICoordinating volume];
-[SBRingerNoticeUICoordinating setVolume:];
-[SBRingerNoticeUICoordinating setVolume:animated:forKeyPress:];
-[SBRingerNoticeUICoordinating buttonReleased];
-[SBRingerNoticeUICoordinating isActivatedForPreviewing];
-[SBRingerNoticeUICoordinating isRingerSilent];
-[SBRingerNoticeUICoordinating nudgeUp:];
-[SBRingerNoticeUICoordinating presentForMuteChange:];
-[SBRingerNoticeUICoordinating setRingerSilent:];
```
