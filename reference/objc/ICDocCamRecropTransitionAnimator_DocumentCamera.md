# `ICDocCamRecropTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 10 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _presenting;
@"UIImage" _filteredImage;
@"UIImage" _unfilteredImage;
@"NSIndexPath" _indexPath;
d _duration;
@? _completion;
q _orientation;
@"UIView" _startView;
@"ICDocCamImageQuad" _quadForOverlay;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containerViewFrame;
```

## Properties

```
@property (T@"UIImage",&,N,V_filteredImage) filteredImage;
@property (T@"UIImage",&,N,V_unfilteredImage) unfilteredImage;
@property (T@"NSIndexPath",&,N,V_indexPath) indexPath;
@property (Td,N,V_duration) duration;
@property (T@?,C,N,V_completion) completion;
@property (Tq,N,V_orientation) orientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_containerViewFrame) containerViewFrame;
@property (T@"UIView",W,N,V_startView) startView;
@property (T@"ICDocCamImageQuad",&,N,V_quadForOverlay) quadForOverlay;
@property (TB,N,V_presenting) presenting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamRecropTransitionAnimator setOrientation:];
-[ICDocCamRecropTransitionAnimator setCompletion:];
-[ICDocCamRecropTransitionAnimator completion];
-[ICDocCamRecropTransitionAnimator indexPath];
-[ICDocCamRecropTransitionAnimator animateTransition:];
-[ICDocCamRecropTransitionAnimator transitionDuration:];
-[ICDocCamRecropTransitionAnimator orientation];
-[ICDocCamRecropTransitionAnimator duration];
-[ICDocCamRecropTransitionAnimator setIndexPath:];
-[ICDocCamRecropTransitionAnimator startView];
-[ICDocCamRecropTransitionAnimator setDuration:];
-[ICDocCamRecropTransitionAnimator setStartView:];
-[ICDocCamRecropTransitionAnimator setPresenting:];
-[ICDocCamRecropTransitionAnimator presenting];
-[ICDocCamRecropTransitionAnimator unfilteredImage];
-[ICDocCamRecropTransitionAnimator containerViewFrame];
-[ICDocCamRecropTransitionAnimator filteredImage];
-[ICDocCamRecropTransitionAnimator imageMeshTransform:];
-[ICDocCamRecropTransitionAnimator initWithImage:unfilteredImage:orientation:indexPath:duration:completion:];
-[ICDocCamRecropTransitionAnimator matrixTransformingQuadForOverlayToImageView:];
-[ICDocCamRecropTransitionAnimator matrixTransformingToUnitSquareWithPoints:y0:x1:y1:x2:y2:x3:y3:];
-[ICDocCamRecropTransitionAnimator performPopTransitionFromViewController:toViewController:transitionContext:];
-[ICDocCamRecropTransitionAnimator performPushTransitionFromViewController:toViewController:transitionContext:];
-[ICDocCamRecropTransitionAnimator performSimpleFadeInFromViewController:toViewController:transitionContext:];
-[ICDocCamRecropTransitionAnimator quadForOverlay];
-[ICDocCamRecropTransitionAnimator scrollViewTransform:];
-[ICDocCamRecropTransitionAnimator setContainerViewFrame:];
-[ICDocCamRecropTransitionAnimator setFilteredImage:];
-[ICDocCamRecropTransitionAnimator setQuadForOverlay:];
-[ICDocCamRecropTransitionAnimator setUnfilteredImage:];
-[ICDocCamRecropTransitionAnimator sortPoints:sorted:];
```
