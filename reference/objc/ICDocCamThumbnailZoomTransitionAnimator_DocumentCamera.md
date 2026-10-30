# `ICDocCamThumbnailZoomTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _presenting;
@"UIImage" _thumbnailImage;
@"NSIndexPath" _indexPath;
d _duration;
@? _completion;
```

## Properties

```
@property (T@"UIImage",&,N,V_thumbnailImage) thumbnailImage;
@property (T@"NSIndexPath",&,N,V_indexPath) indexPath;
@property (Td,N,V_duration) duration;
@property (T@?,C,N,V_completion) completion;
@property (TB,N,V_presenting) presenting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamThumbnailZoomTransitionAnimator setCompletion:];
-[ICDocCamThumbnailZoomTransitionAnimator setThumbnailImage:];
-[ICDocCamThumbnailZoomTransitionAnimator completion];
-[ICDocCamThumbnailZoomTransitionAnimator indexPath];
-[ICDocCamThumbnailZoomTransitionAnimator animateTransition:];
-[ICDocCamThumbnailZoomTransitionAnimator transitionDuration:];
-[ICDocCamThumbnailZoomTransitionAnimator duration];
-[ICDocCamThumbnailZoomTransitionAnimator setIndexPath:];
-[ICDocCamThumbnailZoomTransitionAnimator _shouldCrossFadeNavigationBar];
-[ICDocCamThumbnailZoomTransitionAnimator setDuration:];
-[ICDocCamThumbnailZoomTransitionAnimator thumbnailImage];
-[ICDocCamThumbnailZoomTransitionAnimator setPresenting:];
-[ICDocCamThumbnailZoomTransitionAnimator presenting];
-[ICDocCamThumbnailZoomTransitionAnimator initWithImage:indexPath:duration:completion:];
```
