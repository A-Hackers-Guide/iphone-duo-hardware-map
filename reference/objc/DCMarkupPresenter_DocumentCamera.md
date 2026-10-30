# `DCMarkupPresenter`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"ICDocCamDocumentInfo" _documentInfo;
@"ICDocCamImageCache" _imageCache;
@"MURemoteViewController" _markupRemoteViewController;
@"MarkupViewController" _markupViewController;
@"UIViewController" _presentingViewController;
Q _inkStyle;
@? _frameBlock;
@? _completionBlock;
@? _startPresentBlock;
@? _dismissCompletionBlock;
```

## Properties

```
@property (T@"ICDocCamDocumentInfo",&,V_documentInfo) documentInfo;
@property (T@"ICDocCamImageCache",&,V_imageCache) imageCache;
@property (T@"MURemoteViewController",&,N,V_markupRemoteViewController) markupRemoteViewController;
@property (T@"MarkupViewController",&,N,V_markupViewController) markupViewController;
@property (T@"UIViewController",W,V_presentingViewController) presentingViewController;
@property (TQ,N,V_inkStyle) inkStyle;
@property (T@?,C,N,V_frameBlock) frameBlock;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@?,C,N,V_startPresentBlock) startPresentBlock;
@property (T@?,C,N,V_dismissCompletionBlock) dismissCompletionBlock;
```

## Class methods

```
+[DCMarkupPresenter cleanupMarkup];
+[DCMarkupPresenter markupDocumentInfo:imageCache:fromView:presentingViewController:inkStyle:frameBlock:startPresentBlock:completionBlock:dismissCompletionBlock:];
```

## Instance methods

```
-[DCMarkupPresenter setImageCache:];
-[DCMarkupPresenter setCompletionBlock:];
-[DCMarkupPresenter completionBlock];
-[DCMarkupPresenter setPresentingViewController:];
-[DCMarkupPresenter documentInfo];
-[DCMarkupPresenter presentingViewController];
-[DCMarkupPresenter imageCache];
-[DCMarkupPresenter setDocumentInfo:];
-[DCMarkupPresenter inkStyle];
-[DCMarkupPresenter setInkStyle:];
-[DCMarkupPresenter dismissCompletionBlock];
-[DCMarkupPresenter dismissMarkupViewController];
-[DCMarkupPresenter frameBlock];
-[DCMarkupPresenter handleReturnedURL:];
-[DCMarkupPresenter markupCancelAction:];
-[DCMarkupPresenter markupDoneAction:];
-[DCMarkupPresenter markupRemoteViewController];
-[DCMarkupPresenter markupViewController];
-[DCMarkupPresenter presentMarkupFromView:];
-[DCMarkupPresenter presentMarkupViewControllerFromView:];
-[DCMarkupPresenter setDismissCompletionBlock:];
-[DCMarkupPresenter setFrameBlock:];
-[DCMarkupPresenter setMarkupRemoteViewController:];
-[DCMarkupPresenter setMarkupViewController:];
-[DCMarkupPresenter setStartPresentBlock:];
-[DCMarkupPresenter startPresentBlock];
```
