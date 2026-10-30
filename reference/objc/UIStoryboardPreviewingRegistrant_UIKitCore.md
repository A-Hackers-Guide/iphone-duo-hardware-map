# `UIStoryboardPreviewingRegistrant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `UIViewControllerPreviewingDelegate`
- 4 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerPreviewing>" _previewingContext;
@"UIStoryboardPreviewingSegueTemplateStorage" _segueTemplateStorage;
@"UIViewController" _viewController;
@"UIView" _sourceView;
```

## Properties

```
@property (T@"UIViewController",W,N,V_viewController) viewController;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIStoryboardPreviewingRegistrant setViewController:];
-[UIStoryboardPreviewingRegistrant viewController];
-[UIStoryboardPreviewingRegistrant setSourceView:];
-[UIStoryboardPreviewingRegistrant encodeWithCoder:];
-[UIStoryboardPreviewingRegistrant initWithCoder:];
-[UIStoryboardPreviewingRegistrant sourceView];
-[UIStoryboardPreviewingRegistrant previewingContext:commitViewController:];
-[UIStoryboardPreviewingRegistrant previewingContext:viewControllerForLocation:];
-[UIStoryboardPreviewingRegistrant registerForPreviewing];
-[UIStoryboardPreviewingRegistrant unregisterForPreviewing];
```
