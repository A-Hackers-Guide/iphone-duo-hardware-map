# `CAMImageWell`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- Protocols: `UIGestureRecognizerDelegate`
- 14 instance variables, 20 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _scaledForInteraction;
B _thumbnailImageHidden;
i __currentPresentationStyle;
q _layoutStyle;
q _cameraOrientation;
@"<CAMImageWellPresentationDelegate>" _presentationDelegate;
@"UIView" __containerView;
@"UIImageView" __thumbnailImageView;
@"NSMutableArray" __dimmingViewQueue;
@"UIImage" __thumbnailImage;
@"UIImage" __placeholderImage;
@"NSString" __uuid;
Q __thumbnailUpdateID;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tappableEdgeInsets;
```

## Properties

```
@property (T@"UIImage",R,N) thumbnailImage;
@property (T@"UIView",R,N,V__containerView) _containerView;
@property (T@"UIImageView",R,N,V__thumbnailImageView) _thumbnailImageView;
@property (T@"NSMutableArray",R,N,V__dimmingViewQueue) _dimmingViewQueue;
@property (T@"UIImage",&,N,S_setThumbnailImage:,V__thumbnailImage) _thumbnailImage;
@property (T@"UIImage",&,N,S_setPlaceholderImage:,V__placeholderImage) _placeholderImage;
@property (T@"NSString",&,N,S_setUuid:,V__uuid) _uuid;
@property (TQ,N,S_setThumbnailUpdateID:,V__thumbnailUpdateID) _thumbnailUpdateID;
@property (Ti,N,S_setCurrentPresentationStyle:,V__currentPresentationStyle) _currentPresentationStyle;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (Tq,N,V_cameraOrientation) cameraOrientation;
@property (T{UIEdgeInsets=dddd},N,V_tappableEdgeInsets) tappableEdgeInsets;
@property (TB,N,GisScaledForInteraction,V_scaledForInteraction) scaledForInteraction;
@property (T@"NSString",R,N) thumbnailImageUUID;
@property (TB,N,GisThumbnailImageHidden,V_thumbnailImageHidden) thumbnailImageHidden;
@property (T@"<CAMImageWellPresentationDelegate>",W,N,V_presentationDelegate) presentationDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMImageWell setLayoutStyle:];
-[CAMImageWell presentationDelegate];
-[CAMImageWell layoutStyle];
-[CAMImageWell setPresentationDelegate:];
-[CAMImageWell intrinsicContentSize];
-[CAMImageWell alignmentRectInsets];
-[CAMImageWell initWithLayoutStyle:];
-[CAMImageWell layoutSubviews];
-[CAMImageWell sizeThatFits:];
-[CAMImageWell _containerView];
-[CAMImageWell setTappableEdgeInsets:];
-[CAMImageWell initWithCoder:];
-[CAMImageWell tappableEdgeInsets];
-[CAMImageWell initWithFrame:];
-[CAMImageWell thumbnailImage];
-[CAMImageWell _setUuid:];
-[CAMImageWell _uuid];
-[CAMImageWell _thumbnailImageView];
-[CAMImageWell setCameraOrientation:];
-[CAMImageWell _performEmitAnimationWithImage:orientation:withCompletionBlock:];
-[CAMImageWell _thumbnailImage];
-[CAMImageWell _affineTransformForImageOrientation:];
-[CAMImageWell _commonCAMImageWellInitializationWithLayoutStyle:];
-[CAMImageWell _cornerRadiusForLayoutStyle:];
-[CAMImageWell _currentPresentationStyle];
-[CAMImageWell _dimmingViewQueue];
-[CAMImageWell _placeholderImage];
-[CAMImageWell _placeholderImageForLayoutStyle:];
-[CAMImageWell _removeFirstDimmingView];
-[CAMImageWell _setCurrentPresentationStyle:];
-[CAMImageWell _setPlaceholderImage:];
-[CAMImageWell _setThumbnailImage:];
-[CAMImageWell _setThumbnailUpdateID:];
-[CAMImageWell _thumbnailUpdateID];
-[CAMImageWell _updateForLayoutStyle];
-[CAMImageWell _updatePresentationStyleAndImageViewAnimated:];
-[CAMImageWell _updateThumbnailImageAnimated:];
-[CAMImageWell _updateThumbnailTransformFromCameraOrientation];
-[CAMImageWell alignmentRectForFrame:scaledForInteraction:];
-[CAMImageWell cameraOrientation];
-[CAMImageWell isScaledForInteraction];
-[CAMImageWell isThumbnailImageHidden];
-[CAMImageWell prepareForThumbnailUpdateFromCapture];
-[CAMImageWell recoverFromFailedThumbnailUpdate];
-[CAMImageWell setCameraOrientation:animated:];
-[CAMImageWell setScaledForInteraction:];
-[CAMImageWell setScaledForInteraction:animated:];
-[CAMImageWell setThumbnailImage:uuid:animated:];
-[CAMImageWell setThumbnailImageHidden:];
-[CAMImageWell thumbnailImageUUID];
```
