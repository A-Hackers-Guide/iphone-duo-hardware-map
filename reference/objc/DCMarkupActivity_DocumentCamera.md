# `DCMarkupActivity`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIActivity`
- 7 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _inkStyle;
@"UIView" _fromView;
@"UIViewController" _presentingViewController;
@"ICDocCamDocumentInfo" _documentInfo;
@"ICDocCamImageCache" _imageCache;
@? _frameBlock;
@? _completionBlock;
```

## Properties

```
@property (T@"UIView",W,N,V_fromView) fromView;
@property (T@"UIViewController",W,N,V_presentingViewController) presentingViewController;
@property (T@"ICDocCamDocumentInfo",&,N,V_documentInfo) documentInfo;
@property (T@"ICDocCamImageCache",&,N,V_imageCache) imageCache;
@property (T@?,C,N,V_frameBlock) frameBlock;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TQ,N,V_inkStyle) inkStyle;
```

## Instance methods

```
-[DCMarkupActivity setImageCache:];
-[DCMarkupActivity setCompletionBlock:];
-[DCMarkupActivity completionBlock];
-[DCMarkupActivity performActivity];
-[DCMarkupActivity setPresentingViewController:];
-[DCMarkupActivity activityType];
-[DCMarkupActivity documentInfo];
-[DCMarkupActivity prepareWithActivityItems:];
-[DCMarkupActivity activityImage];
-[DCMarkupActivity presentingViewController];
-[DCMarkupActivity activityTitle];
-[DCMarkupActivity imageCache];
-[DCMarkupActivity fromView];
-[DCMarkupActivity setFromView:];
-[DCMarkupActivity canPerformWithActivityItems:];
-[DCMarkupActivity setDocumentInfo:];
-[DCMarkupActivity inkStyle];
-[DCMarkupActivity setInkStyle:];
-[DCMarkupActivity frameBlock];
-[DCMarkupActivity initFromView:presentingViewController:frameBlock:completionBlock:];
-[DCMarkupActivity setFrameBlock:];
```
