# `_UIApplicationModalProgressController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 14 properties, 46 instance methods, 2 class methods

## Instance variables

```
B _disableButtonAction;
@"_UIProgressView" _progressView;
@"UIWindowScene" _weakScene;
B _presented;
d _displayDelaySeconds;
@"UIWindow" _window;
@"UIViewController" _sourceViewController;
@"UIAlertController" _alertController;
@? _dismissalHandler;
@? _preDisplayTestBlock;
@"NSProgress" _progress;
@"NSTimer" _showTimer;
@"NSTimer" _hideTimer;
d _displayStartTime;
@"NSProgress" _urlProgress;
```

## Properties

```
@property (TB,N,G_isPresented,S_setPresented:,V_presented) presented;
@property (T@"UIWindow",&,N,G_window,S_setWindow:,V_window) window;
@property (T@"UIViewController",&,N,G_sourceViewController,S_setSourceViewController:,V_sourceViewController) sourceViewController;
@property (T@"UIAlertController",&,N,G_alertController,S_setAlertController:,V_alertController) alertController;
@property (T@?,C,N,G_dismissalHandler,S_setDismissalHandler:,V_dismissalHandler) dismissalHandler;
@property (T@?,C,N,G_preDisplaySetBlock,S_setPreDisplayTestBlock:,V_preDisplayTestBlock) preDisplayTestBlock;
@property (T@"NSProgress",&,N,G_progress,S_setProgress:,V_progress) progress;
@property (T@"NSTimer",&,N,G_showTimer,S_setShowTimer:,V_showTimer) showTimer;
@property (T@"NSTimer",&,N,G_hideTimer,S_setHideTimer:,V_hideTimer) hideTimer;
@property (Td,N,G_displayStartTime,S_setDisplayStartTime:,V_displayStartTime) displayStartTime;
@property (T@"NSProgress",&,N,V_urlProgress) urlProgress;
@property (Td,N,V_displayDelaySeconds) displayDelaySeconds;
@property (T@"NSString",C,N) title;
@property (T@"NSString",C,N) message;
```

## Class methods

```
+[_UIApplicationModalProgressController sharedInstance];
+[_UIApplicationModalProgressController instanceForScene:];
```

## Instance methods

```
-[_UIApplicationModalProgressController _window];
-[_UIApplicationModalProgressController _setPresented:];
-[_UIApplicationModalProgressController _reset];
-[_UIApplicationModalProgressController setMessage:];
-[_UIApplicationModalProgressController init];
-[_UIApplicationModalProgressController message];
-[_UIApplicationModalProgressController _setAlertController:];
-[_UIApplicationModalProgressController _progress];
-[_UIApplicationModalProgressController title];
-[_UIApplicationModalProgressController _isPresented];
-[_UIApplicationModalProgressController setTitle:];
-[_UIApplicationModalProgressController _alertController];
-[_UIApplicationModalProgressController setUrlProgress:];
-[_UIApplicationModalProgressController _callAndClearDismissalHandlerWasDismissedByUser:];
-[_UIApplicationModalProgressController _createSourceWindow];
-[_UIApplicationModalProgressController _defaultSourceViewControllerCreatingWindowIfNeeded];
-[_UIApplicationModalProgressController _dismissButtonAction:];
-[_UIApplicationModalProgressController _dismissalHandler];
-[_UIApplicationModalProgressController _displayStartTime];
-[_UIApplicationModalProgressController _hideImmediatelyWasDismissedByUser:];
-[_UIApplicationModalProgressController _hideTimer];
-[_UIApplicationModalProgressController _hideTimerAction:];
-[_UIApplicationModalProgressController _preDisplaySetBlock];
-[_UIApplicationModalProgressController _setDismissalHandler:];
-[_UIApplicationModalProgressController _setDisplayStartTime:];
-[_UIApplicationModalProgressController _setHideTimer:];
-[_UIApplicationModalProgressController _setPreDisplayTestBlock:];
-[_UIApplicationModalProgressController _setProgress:];
-[_UIApplicationModalProgressController _setShowTimer:];
-[_UIApplicationModalProgressController _setSourceViewController:];
-[_UIApplicationModalProgressController _setWindow:];
-[_UIApplicationModalProgressController _shouldAnimatePresentationForIdiom:];
-[_UIApplicationModalProgressController _showTimer];
-[_UIApplicationModalProgressController _showTimerAction:];
-[_UIApplicationModalProgressController _sourceScene];
-[_UIApplicationModalProgressController _sourceViewController];
-[_UIApplicationModalProgressController displayDelaySeconds];
-[_UIApplicationModalProgressController displayForCopyingFileAtURL:toURL:sourceViewController:completionHandler:];
-[_UIApplicationModalProgressController displayForDownloadingURL:copyToURL:sourceViewController:completionHandler:];
-[_UIApplicationModalProgressController displayForDownloadingURL:sourceViewController:completionHandler:];
-[_UIApplicationModalProgressController displayWithTitle:message:progress:buttonTitle:sourceViewController:preDisplayTestBlock:dismissalHandler:];
-[_UIApplicationModalProgressController hideAfterDelay:forceCompletion:replacementDismissalHandler:];
-[_UIApplicationModalProgressController hideAfterMinimumUptimeWithDismissalHandler:];
-[_UIApplicationModalProgressController reconfigureWithTitle:message:progress:buttonTitle:dismissalHandler:];
-[_UIApplicationModalProgressController setDisplayDelaySeconds:];
-[_UIApplicationModalProgressController urlProgress];
```
