# `_UIViewControllerPreviewingContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPreviewInteractionControllerDelegate`, `UIViewControllerPreviewing_Internal`
- 6 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerPreviewingDelegate>" _delegate;
@"UIView" _customViewForInteractiveHighlight;
@"UIView" _sourceView;
@"UIViewController" _viewController;
@"_UIPreviewInteractionController" _previewInteractionController;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T@"UIView",&,N,V_sourceView) sourceView;
@property (T@"UIViewController",W,N,V_viewController) viewController;
@property (T@"_UIPreviewInteractionController",&,N,V_previewInteractionController) previewInteractionController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIViewControllerPreviewingDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N,V_customViewForInteractiveHighlight) customViewForInteractiveHighlight;
@property (T@"UIGestureRecognizer",R,N) previewingGestureRecognizerForFailureRelationship;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
```

## Instance methods

```
-[_UIViewControllerPreviewingContext setSourceRect:];
-[_UIViewControllerPreviewingContext setViewController:];
-[_UIViewControllerPreviewingContext sourceRect];
-[_UIViewControllerPreviewingContext unregister];
-[_UIViewControllerPreviewingContext viewController];
-[_UIViewControllerPreviewingContext setDelegate:];
-[_UIViewControllerPreviewingContext setSourceView:];
-[_UIViewControllerPreviewingContext delegate];
-[_UIViewControllerPreviewingContext sourceView];
-[_UIViewControllerPreviewingContext customViewForInteractiveHighlight];
-[_UIViewControllerPreviewingContext initWithSourceView:viewController:];
-[_UIViewControllerPreviewingContext preferredSourceViewRectInCoordinateSpace:];
-[_UIViewControllerPreviewingContext previewInteractionController];
-[_UIViewControllerPreviewingContext previewInteractionController:commitViewController:];
-[_UIViewControllerPreviewingContext previewInteractionController:didDismissViewController:committing:];
-[_UIViewControllerPreviewingContext previewInteractionController:viewControllerForPreviewingAtLocation:inCoordinateSpace:presentingViewController:];
-[_UIViewControllerPreviewingContext previewInteractionController:willDismissViewController:];
-[_UIViewControllerPreviewingContext previewInteractionController:willPresentViewController:];
-[_UIViewControllerPreviewingContext previewInteractionController:willPresentViewController:forLocation:inSourceView:];
-[_UIViewControllerPreviewingContext previewingGestureRecognizerForFailureRelationship];
-[_UIViewControllerPreviewingContext setCustomViewForInteractiveHighlight:];
-[_UIViewControllerPreviewingContext setPreviewInteractionController:];
```
