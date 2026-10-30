# `UIForcePresentationController` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) presentationPhaseCompletionBlock;
@property (T@"UIGestureRecognizer",&,N) panningGestureRecognizer;
@property (TB,N) _sourceViewSnapshotAndScaleTransformSuppressed;
@property (T@"UIView",R,N) _revealContainerView;
@property (T@"_UIStatesFeedbackGenerator",&,N) feedbackGenerator;
@property (T@"<_UIForcePresentationControllerDelegate>",W,N) forcePresentationControllerDelegate;
```

## Instance methods

```
-[UIForcePresentationController setFeedbackGenerator:];
-[UIForcePresentationController feedbackGenerator];
-[UIForcePresentationController _canCommitPresentation];
-[UIForcePresentationController _canDismissPresentation];
-[UIForcePresentationController _revealContainerView];
-[UIForcePresentationController _sourceViewSnapshotAndScaleTransformSuppressed];
-[UIForcePresentationController forcePresentationControllerDelegate];
-[UIForcePresentationController panningGestureRecognizer];
-[UIForcePresentationController presentationPhaseCompletionBlock];
-[UIForcePresentationController setForcePresentationControllerDelegate:];
-[UIForcePresentationController setPanningGestureRecognizer:];
-[UIForcePresentationController setPresentationPhaseCompletionBlock:];
-[UIForcePresentationController set_sourceViewSnapshotAndScaleTransformSuppressed:];
-[UIForcePresentationController _willCommitPresentation];
```
