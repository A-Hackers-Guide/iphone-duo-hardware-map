# `CFXPlayButtonView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<CFXPlayButtonViewDelegate>" _delegate;
@"CAShapeLayer" _playControlMaskLayer;
@"UIView" _contentView;
@"UIButton" _playButton;
@"UIImage" _playImage;
@"UIImage" _pauseImage;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_playControlMaskLayer) playControlMaskLayer;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"UIButton",W,N,V_playButton) playButton;
@property (T@"UIImage",&,N,V_playImage) playImage;
@property (T@"UIImage",&,N,V_pauseImage) pauseImage;
@property (T@"<CFXPlayButtonViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CFXPlayButtonView setContentView:];
-[CFXPlayButtonView layoutSubviews];
-[CFXPlayButtonView setDelegate:];
-[CFXPlayButtonView setPlayButton:];
-[CFXPlayButtonView contentView];
-[CFXPlayButtonView delegate];
-[CFXPlayButtonView sharedInit];
-[CFXPlayButtonView initWithCoder:];
-[CFXPlayButtonView initWithFrame:];
-[CFXPlayButtonView playButton];
-[CFXPlayButtonView pauseImage];
-[CFXPlayButtonView playImage];
-[CFXPlayButtonView playButtonTapped:];
-[CFXPlayButtonView notifyWasTapped];
-[CFXPlayButtonView notifyPlaybackDidStart];
-[CFXPlayButtonView notifyPlaybackDidStop];
-[CFXPlayButtonView playControlMaskLayer];
-[CFXPlayButtonView setPauseImage:];
-[CFXPlayButtonView setPlayControlMaskLayer:];
-[CFXPlayButtonView setPlayImage:];
```
