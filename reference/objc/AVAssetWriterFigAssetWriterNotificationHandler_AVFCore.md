# `AVAssetWriterFigAssetWriterNotificationHandler`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAssetWriter=} _figAssetWriter;
i _didNotCallDelegate;
@"AVWeakReference" _weakReferenceToSelf;
@"AVWeakReference" _weakReferenceToDelegate;
i _notificationHandlersAreRegistered;
```

## Properties

```
@property (T@"AVWeakReference",&,G_weakReferenceToDelegate,S_setWeakReferenceToDelegate:,V_weakReferenceToDelegate) weakReferenceToDelegate;
@property (T@"<AVAssetWriterFigAssetWriterNotificationHandlerDelegate>",W) delegate;
```

## Instance methods

```
-[AVAssetWriterFigAssetWriterNotificationHandler dealloc];
-[AVAssetWriterFigAssetWriterNotificationHandler _handleServerDiedNotification];
-[AVAssetWriterFigAssetWriterNotificationHandler setDelegate:];
-[AVAssetWriterFigAssetWriterNotificationHandler delegate];
-[AVAssetWriterFigAssetWriterNotificationHandler _callDelegateIfNotCalledWithSuccess:error:];
-[AVAssetWriterFigAssetWriterNotificationHandler _handleCompletedWritingNotification];
-[AVAssetWriterFigAssetWriterNotificationHandler _handleDiskReserveThresholdExhaustedNotification];
-[AVAssetWriterFigAssetWriterNotificationHandler _handleFailedNotificationWithError:];
-[AVAssetWriterFigAssetWriterNotificationHandler _setWeakReferenceToDelegate:];
-[AVAssetWriterFigAssetWriterNotificationHandler _teardownNotificationHandlers];
-[AVAssetWriterFigAssetWriterNotificationHandler _weakReferenceToDelegate];
-[AVAssetWriterFigAssetWriterNotificationHandler initWithFigAssetWriter:];
```
