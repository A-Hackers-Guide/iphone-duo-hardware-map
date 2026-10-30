# `CFXClipPlayerViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXCompositionPlayerViewController`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CFXClip" _clip;
@"UIView" _playerContainerView;
@"UIView" _placeholderContainerView;
@"UIViewController<JFXAVPlayerViewer>" _avPlayerView;
@"CFXClipCompositionDataSource" _clipDataSource;
```

## Properties

```
@property (T@"UIView",&,N,V_playerContainerView) playerContainerView;
@property (T@"UIView",&,N,V_placeholderContainerView) placeholderContainerView;
@property (T@"UIViewController<JFXAVPlayerViewer>",W,N,V_avPlayerView) avPlayerView;
@property (T@"CFXClipCompositionDataSource",&,N,V_clipDataSource) clipDataSource;
@property (T@"CFXClip",&,N,V_clip) clip;
```

## Instance methods

```
-[CFXClipPlayerViewController setClip:];
-[CFXClipPlayerViewController viewWillAppear:];
-[CFXClipPlayerViewController clip];
-[CFXClipPlayerViewController prepareForSegue:sender:];
-[CFXClipPlayerViewController avPlayerView];
-[CFXClipPlayerViewController clipDataSource];
-[CFXClipPlayerViewController displayCompositionUpdateLoadingView:];
-[CFXClipPlayerViewController placeholderContainerView];
-[CFXClipPlayerViewController playerContainerView];
-[CFXClipPlayerViewController playerViewer];
-[CFXClipPlayerViewController reloadClip];
-[CFXClipPlayerViewController reloadClipAndSeekToStart:];
-[CFXClipPlayerViewController setAvPlayerView:];
-[CFXClipPlayerViewController setClipDataSource:];
-[CFXClipPlayerViewController setPlaceholderContainerView:];
-[CFXClipPlayerViewController setPlayerContainerView:];
-[CFXClipPlayerViewController updateCompositionForEffectChange];
```
