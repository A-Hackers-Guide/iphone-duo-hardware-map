# `SBProductivityGestureEducationPillViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BNPresentable`
- 3 instance variables, 17 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"PLPillView" _pillView;
@"<SBProductivityGestureEducationPillViewControllerDelegate>" _delegate;
@"SBProductivityGestureEducationItem" _item;
```

## Properties

```
@property (T@"<SBProductivityGestureEducationPillViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSURL",R,C,N) actionURL;
@property (T@"SBProductivityGestureEducationItem",R,C,N,V_item) item;
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N) requestIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProductivityGestureEducationPillViewController requestIdentifier];
-[SBProductivityGestureEducationPillViewController presentableBehavior];
-[SBProductivityGestureEducationPillViewController viewDidLoad];
-[SBProductivityGestureEducationPillViewController requesterIdentifier];
-[SBProductivityGestureEducationPillViewController item];
-[SBProductivityGestureEducationPillViewController viewController];
-[SBProductivityGestureEducationPillViewController initWithItem:];
-[SBProductivityGestureEducationPillViewController setDelegate:];
-[SBProductivityGestureEducationPillViewController presentableWillAppearAsBanner:];
-[SBProductivityGestureEducationPillViewController delegate];
-[SBProductivityGestureEducationPillViewController _handleSingleTap:];
-[SBProductivityGestureEducationPillViewController actionURL];
-[SBProductivityGestureEducationPillViewController presentableDidDisappearAsBanner:withReason:];
-[SBProductivityGestureEducationPillViewController presentableWillNotAppearAsBanner:withReason:];
-[SBProductivityGestureEducationPillViewController presentableDescription];
-[SBProductivityGestureEducationPillViewController _titleString];
-[SBProductivityGestureEducationPillViewController _marqueeStarted:];
-[SBProductivityGestureEducationPillViewController _pillActionContentItem];
-[SBProductivityGestureEducationPillViewController _pillLeadingImageView];
-[SBProductivityGestureEducationPillViewController _pillTitleContentItem];
-[SBProductivityGestureEducationPillViewController _titleForItemType:];
-[SBProductivityGestureEducationPillViewController _titleKeyForEducationType:];
```
