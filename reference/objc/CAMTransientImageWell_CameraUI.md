# `CAMTransientImageWell`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 9 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _autoStashesImages;
B __stashed;
@"<CAMTransientImageWellDelegate>" _delegate;
q _orientation;
@"UIImageView" __imageView;
@"NSTimer" __autoStashTimer;
@"UITapGestureRecognizer" __tapGestureRecognizer;
@"UISwipeGestureRecognizer" __unstashGestureRecognizer;
@"UISwipeGestureRecognizer" __stashGestureRecognizer;
```

## Properties

```
@property (T@"UIImageView",&,N,S_setImageView:,V__imageView) _imageView;
@property (T@"NSTimer",&,N,V__autoStashTimer) _autoStashTimer;
@property (TB,N,G_isStashed,S_setStashed:,V__stashed) _stashed;
@property (T@"UITapGestureRecognizer",R,N,V__tapGestureRecognizer) _tapGestureRecognizer;
@property (T@"UISwipeGestureRecognizer",R,N,V__unstashGestureRecognizer) _unstashGestureRecognizer;
@property (T@"UISwipeGestureRecognizer",R,N,V__stashGestureRecognizer) _stashGestureRecognizer;
@property (T@"<CAMTransientImageWellDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_orientation) orientation;
@property (TB,N,V_autoStashesImages) autoStashesImages;
@property (T@"UIImage",&,N) image;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) imageFrame;
@property (TB,N) currentImageHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTransientImageWell setOrientation:animated:];
-[CAMTransientImageWell setOrientation:];
-[CAMTransientImageWell _imageView];
-[CAMTransientImageWell _handleTap:];
-[CAMTransientImageWell orientation];
-[CAMTransientImageWell layoutSubviews];
-[CAMTransientImageWell hitTest:withEvent:];
-[CAMTransientImageWell setDelegate:];
-[CAMTransientImageWell _tapGestureRecognizer];
-[CAMTransientImageWell delegate];
-[CAMTransientImageWell setImage:animated:];
-[CAMTransientImageWell image];
-[CAMTransientImageWell initWithFrame:];
-[CAMTransientImageWell setImage:];
-[CAMTransientImageWell _setImageView:];
-[CAMTransientImageWell imageFrame];
-[CAMTransientImageWell _autoStashTimer];
-[CAMTransientImageWell _cancelAutoStashTimer];
-[CAMTransientImageWell _dismissImageAnimated:];
-[CAMTransientImageWell _dismissImageView:animated:];
-[CAMTransientImageWell _handleAutoStashTimerFired:];
-[CAMTransientImageWell _handleStashSwipe:];
-[CAMTransientImageWell _handleUnstashSwipe:];
-[CAMTransientImageWell _imageViewMaxSize];
-[CAMTransientImageWell _imageViewSizeForContentSize:];
-[CAMTransientImageWell _imageViewSpawnPoint];
-[CAMTransientImageWell _imageViewStashPoint];
-[CAMTransientImageWell _isStashed];
-[CAMTransientImageWell _restartAutoStashTimer];
-[CAMTransientImageWell _restartAutoStashTimerWithDuration:];
-[CAMTransientImageWell _setStashed:];
-[CAMTransientImageWell _setStashed:animated:];
-[CAMTransientImageWell _stashGestureRecognizer];
-[CAMTransientImageWell _unorientedFrameForImageView:];
-[CAMTransientImageWell _unstashGestureRecognizer];
-[CAMTransientImageWell autoStashesImages];
-[CAMTransientImageWell clearImageAnimated:];
-[CAMTransientImageWell currentImageHidden];
-[CAMTransientImageWell setAutoStashesImages:];
-[CAMTransientImageWell setCurrentImageHidden:];
-[CAMTransientImageWell set_autoStashTimer:];
```
