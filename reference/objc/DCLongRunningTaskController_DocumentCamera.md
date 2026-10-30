# `DCLongRunningTaskController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DCProgressViewControllerDelegate`
- 16 instance variables, 16 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _isCancelled;
B _shouldShowCancelButton;
B _shouldShowCircularProgress;
B _progressViewControllerDidFinishPresenting;
B _shouldDismissProgressViewController;
@? _progressToStringTransformer;
@"UIViewController" _viewControllerToPresentFrom;
@"UIWindow" _window;
d _intervalBeforeOpeningProgressDialog;
@ _keepAlive;
@? _completionBlock;
@? _updateProgressUIBlock;
@"NSProgress" _progress;
@"NSDate" _lastAccessibilityAnnouncementDate;
@"NSDate" _openProgressDate;
@"DCProgressViewController" _progressViewController;
```

## Properties

```
@property (T@"UIWindow",&,N,V_window) window;
@property (Td,N,V_intervalBeforeOpeningProgressDialog) intervalBeforeOpeningProgressDialog;
@property (T@,&,N,V_keepAlive) keepAlive;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@?,C,N,V_updateProgressUIBlock) updateProgressUIBlock;
@property (T@"NSProgress",&,N,V_progress) progress;
@property (T@"NSDate",&,N,V_lastAccessibilityAnnouncementDate) lastAccessibilityAnnouncementDate;
@property (T@"NSDate",&,N,V_openProgressDate) openProgressDate;
@property (TB,N,V_isCancelled) isCancelled;
@property (T@"DCProgressViewController",&,N,V_progressViewController) progressViewController;
@property (TB,N,V_progressViewControllerDidFinishPresenting) progressViewControllerDidFinishPresenting;
@property (TB,N,V_shouldDismissProgressViewController) shouldDismissProgressViewController;
@property (TB,N,V_shouldShowCancelButton) shouldShowCancelButton;
@property (T@?,C,N,V_progressToStringTransformer) progressToStringTransformer;
@property (T@"UIViewController",&,N,V_viewControllerToPresentFrom) viewControllerToPresentFrom;
@property (TB,N,V_shouldShowCircularProgress) shouldShowCircularProgress;
```

## Instance methods

```
-[DCLongRunningTaskController setCompletionBlock:];
-[DCLongRunningTaskController completionBlock];
-[DCLongRunningTaskController observeValueForKeyPath:ofObject:change:context:];
-[DCLongRunningTaskController setProgress:];
-[DCLongRunningTaskController updateProgress];
-[DCLongRunningTaskController init];
-[DCLongRunningTaskController isCancelled];
-[DCLongRunningTaskController window];
-[DCLongRunningTaskController setProgressViewController:];
-[DCLongRunningTaskController progress];
-[DCLongRunningTaskController shouldShowCancelButton];
-[DCLongRunningTaskController keepAlive];
-[DCLongRunningTaskController progressViewController];
-[DCLongRunningTaskController setKeepAlive:];
-[DCLongRunningTaskController setWindow:];
-[DCLongRunningTaskController setIsCancelled:];
-[DCLongRunningTaskController viewControllerToPresentFrom];
-[DCLongRunningTaskController setShouldShowCancelButton:];
-[DCLongRunningTaskController setViewControllerToPresentFrom:];
-[DCLongRunningTaskController closeProgressDialog];
-[DCLongRunningTaskController completeTaskIfNecessary];
-[DCLongRunningTaskController initWithWindow:intervalBeforeOpeningProgressDialog:];
-[DCLongRunningTaskController intervalBeforeOpeningProgressDialog];
-[DCLongRunningTaskController lastAccessibilityAnnouncementDate];
-[DCLongRunningTaskController openProgressDate];
-[DCLongRunningTaskController openProgressDialog];
-[DCLongRunningTaskController progressViewControllerDidFinishPresenting];
-[DCLongRunningTaskController setIntervalBeforeOpeningProgressDialog:];
-[DCLongRunningTaskController setLastAccessibilityAnnouncementDate:];
-[DCLongRunningTaskController setOpenProgressDate:];
-[DCLongRunningTaskController setProgressViewControllerDidFinishPresenting:];
-[DCLongRunningTaskController setShouldDismissProgressViewController:];
-[DCLongRunningTaskController setShouldShowCircularProgress:];
-[DCLongRunningTaskController setUpdateProgressUIBlock:];
-[DCLongRunningTaskController shouldDismissProgressViewController];
-[DCLongRunningTaskController shouldShowCircularProgress];
-[DCLongRunningTaskController startTask:completionBlock:];
-[DCLongRunningTaskController updateProgressUIBlock];
-[DCLongRunningTaskController willDismissProgressViewController:];
-[DCLongRunningTaskController setProgressToStringTransformer:];
-[DCLongRunningTaskController progressToStringTransformer];
```
