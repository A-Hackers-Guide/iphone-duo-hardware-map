# `NSFilePresenter` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSURL",R,C) presentedItemURL;
@property (T@"NSOperationQueue",R,&) presentedItemOperationQueue;
@property (T@"NSURL",?,R,C) primaryPresentedItemURL;
@property (T@"NSSet",?,R) observedPresentedItemUbiquityAttributes;
```

## Instance methods

```
-[NSFilePresenter presentedItemOperationQueue];
-[NSFilePresenter presentedItemURL];
-[NSFilePresenter relinquishPresentedItemToWriter:];
-[NSFilePresenter accommodatePresentedSubitemDeletionAtURL:completionHandler:];
-[NSFilePresenter relinquishPresentedItemToReader:];
-[NSFilePresenter savePresentedItemChangesWithCompletionHandler:];
-[NSFilePresenter accommodatePresentedItemDeletionWithCompletionHandler:];
-[NSFilePresenter presentedItemDidMoveToURL:];
-[NSFilePresenter presentedSubitemDidAppearAtURL:];
-[NSFilePresenter presentedSubitemDidChangeAtURL:];
-[NSFilePresenter accommodatePresentedItemEvictionWithCompletionHandler:];
-[NSFilePresenter observedPresentedItemUbiquityAttributes];
-[NSFilePresenter presentedItemDidChange];
-[NSFilePresenter presentedItemDidChangeUbiquityAttributes:];
-[NSFilePresenter presentedItemDidGainVersion:];
-[NSFilePresenter presentedItemDidLoseVersion:];
-[NSFilePresenter presentedItemDidResolveConflictVersion:];
-[NSFilePresenter presentedSubitemAtURL:didGainVersion:];
-[NSFilePresenter presentedSubitemAtURL:didLoseVersion:];
-[NSFilePresenter presentedSubitemAtURL:didMoveToURL:];
-[NSFilePresenter presentedSubitemAtURL:didResolveConflictVersion:];
-[NSFilePresenter primaryPresentedItemURL];
```
