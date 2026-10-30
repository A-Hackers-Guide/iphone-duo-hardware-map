# `ICDocCamRetakeTransitionAnimator`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _presenting;
@"UIImage" _retakeImage;
@"NSIndexPath" _indexPath;
d _duration;
@? _completion;
```

## Properties

```
@property (T@"UIImage",&,N,V_retakeImage) retakeImage;
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
-[ICDocCamRetakeTransitionAnimator setCompletion:];
-[ICDocCamRetakeTransitionAnimator completion];
-[ICDocCamRetakeTransitionAnimator indexPath];
-[ICDocCamRetakeTransitionAnimator animateTransition:];
-[ICDocCamRetakeTransitionAnimator transitionDuration:];
-[ICDocCamRetakeTransitionAnimator duration];
-[ICDocCamRetakeTransitionAnimator setIndexPath:];
-[ICDocCamRetakeTransitionAnimator setDuration:];
-[ICDocCamRetakeTransitionAnimator setPresenting:];
-[ICDocCamRetakeTransitionAnimator presenting];
-[ICDocCamRetakeTransitionAnimator setRetakeImage:];
-[ICDocCamRetakeTransitionAnimator initWithImage:indexPath:duration:completion:];
-[ICDocCamRetakeTransitionAnimator makeUIImageFromCIImage:];
-[ICDocCamRetakeTransitionAnimator retakeImage];
```
