# `UIViewControllerPreviewing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"UIGestureRecognizer",R,N) previewingGestureRecognizerForFailureRelationship;
@property (T@"<UIViewControllerPreviewingDelegate>",R,N) delegate;
@property (T@"UIView",R,N) sourceView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) sourceRect;
```

## Instance methods

```
-[UIViewControllerPreviewing setSourceRect:];
-[UIViewControllerPreviewing sourceRect];
-[UIViewControllerPreviewing delegate];
-[UIViewControllerPreviewing sourceView];
-[UIViewControllerPreviewing previewingGestureRecognizerForFailureRelationship];
```
