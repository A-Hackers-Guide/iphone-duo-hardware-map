# `UIPreviewItemController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPreviewInteractionControllerDelegate`, `UIInteractionProgressObserver`
- 19 instance variables, 14 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"MLULookupItem" _lookupItem;
@"UIPreviewInteractionController" _previewInteractionController;
@"UIView" _previewIndicatorView;
@"UIImageView" _previewIndicatorImageView;
@"UIView" _previewIndicatorSnapshotView;
@"CADisplayLink" _previewIndicatorDisplayLink;
d _lastPreviewIndicatorAnimationTimestamp;
d _previewIndicatorAnimationTargetAlpha;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previewIndicatorBoundingRect;
B _previewIndicatorUsesStandardAnimation;
B _contentManagedByClient;
@"UIPreviewItemController" _strongSelf;
B _interactionInProgress;
@"<UIPreviewItemDelegate>" _delegate;
q _type;
@"NSDictionary" _previewData;
@"UIViewController" _presentedViewController;
@"UIViewController" _presentingViewController;
@"UIView" _view;
```

## Properties

```
@property (T@"<UIPreviewItemDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_type) type;
@property (T@"NSDictionary",R,N,V_previewData) previewData;
@property (T@"NSArray",R,N) gestureRecognizers;
@property (T@"UIGestureRecognizer",R,N) presentationGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) presentationSecondaryGestureRecognizer;
@property (T@"UIViewController",R,N,V_presentedViewController) presentedViewController;
@property (T@"UIViewController",R,N,V_presentingViewController) presentingViewController;
@property (TB,R,N,V_interactionInProgress) interactionInProgress;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPreviewItemController interactionProgressDidUpdate:];
-[UIPreviewItemController interactionProgress:didEnd:];
-[UIPreviewItemController gestureRecognizers];
-[UIPreviewItemController init];
-[UIPreviewItemController initWithView:];
-[UIPreviewItemController dealloc];
-[UIPreviewItemController presentingViewController];
-[UIPreviewItemController view];
-[UIPreviewItemController setDelegate:];
-[UIPreviewItemController type];
-[UIPreviewItemController delegate];
-[UIPreviewItemController stopInteraction];
-[UIPreviewItemController _isMobileSafariRestricted];
-[UIPreviewItemController _shouldCancelPreviewWithNegativeFeedback];
-[UIPreviewItemController clearPreviewIndicator];
-[UIPreviewItemController interactionInProgress];
-[UIPreviewItemController performsCustomCommitTransitionForPreviewInteractionController:];
-[UIPreviewItemController performsViewControllerCommitTransitionForPreviewInteractionController:];
-[UIPreviewItemController preparePreviewIndicatorViewInSourceView:updateScreen:];
-[UIPreviewItemController presentationGestureRecognizer];
-[UIPreviewItemController presentationSecondaryGestureRecognizer];
-[UIPreviewItemController presentedViewController];
-[UIPreviewItemController previewData];
-[UIPreviewItemController previewInteractionController:didDismissViewController:committing:];
-[UIPreviewItemController previewInteractionController:interactionProgress:forRevealAtLocation:inSourceView:containerView:];
-[UIPreviewItemController previewInteractionController:performCommitForPreviewViewController:committedViewController:];
-[UIPreviewItemController previewInteractionController:performCustomCommitForPreviewViewController:completion:];
-[UIPreviewItemController previewInteractionController:shouldUseStandardRevealTransformForPreviewingAtLocation:inView:];
-[UIPreviewItemController previewInteractionController:viewControllerForPreviewingAtPosition:inView:presentingViewController:];
-[UIPreviewItemController previewInteractionController:willPresentViewController:forPosition:inSourceView:];
-[UIPreviewItemController previewInteractionControllerShouldPerformCompatibilityCommitTransition:];
-[UIPreviewItemController previewViewControllerForPosition:inSourceView:documentProperties:];
-[UIPreviewItemController setupPreviewIndicatorInSourceView:];
-[UIPreviewItemController startInteraction];
-[UIPreviewItemController updatePreviewIndicatorAnimation:];
```
