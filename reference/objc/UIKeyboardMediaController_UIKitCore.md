# `UIKeyboardMediaController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyboardMediaServiceRemoteViewControllerDelegate`
- 10 instance variables, 6 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"UIViewController" _remoteCardViewController;
@"_UIAsyncInvocation" _remoteCardViewControllerRequest;
@"UIViewController" _recentlyUsedMediaViewController;
@"_UIAsyncInvocation" _recentlyUsedMediaViewControllerRequest;
@"UIView" _targetViewAwaitingRecents;
B _hasRequestedRecentlyUsedMediaViewController;
Q _viewServiceTerminationCount;
@"_UITextDragCaretView" _dropCaret;
B _shouldRetryFetchingRecents;
@"<UIKeyboardMediaControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIKeyboardMediaControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_shouldRetryFetchingRecents) shouldRetryFetchingRecents;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardMediaController sharedKeyboardMediaController];
```

## Instance methods

```
-[UIKeyboardMediaController _presentiMessageApp];
-[UIKeyboardMediaController shouldRetryFetchingRecents];
-[UIKeyboardMediaController presentCard];
-[UIKeyboardMediaController releaseRecentlyUsedMediaViewIfNeeded];
-[UIKeyboardMediaController remoteHandlesRecentsStickerDonation];
-[UIKeyboardMediaController viewServiceDidTerminateWithError:];
-[UIKeyboardMediaController showRecentlyUsedMediaInView:];
-[UIKeyboardMediaController dismissCard];
-[UIKeyboardMediaController dismissCardIfNeeded];
-[UIKeyboardMediaController draggedStickerToPoint:];
-[UIKeyboardMediaController shouldPrefetchRemoteView];
-[UIKeyboardMediaController _embedRecentlyUsedMediaViewInView:animated:];
-[UIKeyboardMediaController _tearDownRemoteViews];
-[UIKeyboardMediaController _displayiMessageAppWithID:];
-[UIKeyboardMediaController stageStickerWithIdentifier:representations:name:externalURI:accessibilityLabel:];
-[UIKeyboardMediaController _stickerIsSupportedPayload];
-[UIKeyboardMediaController dismissCardAnimated];
-[UIKeyboardMediaController _instantiateViewServiceRecentlyUsedMediaWithCompletionHandler:];
-[UIKeyboardMediaController prefetchRecentsViewControllerWithCompletion:];
-[UIKeyboardMediaController setDelegate:];
-[UIKeyboardMediaController remoteHandlesRecentsStickerDonationWithCompletionHandler:];
-[UIKeyboardMediaController _didInsertMedia];
-[UIKeyboardMediaController stickerPickerCardDidLoad];
-[UIKeyboardMediaController handleStickerSuggestionWithTISticker:];
-[UIKeyboardMediaController requestInsertionPointCompletion:];
-[UIKeyboardMediaController delegate];
-[UIKeyboardMediaController _didPresentCard];
-[UIKeyboardMediaController recentsViewWillBeVisible];
-[UIKeyboardMediaController stageSticker:];
-[UIKeyboardMediaController pasteImageAtFileHandle:];
-[UIKeyboardMediaController _keyboardDidChangeFrame:];
-[UIKeyboardMediaController stageStickerWithFileHandle:url:accessibilityLabel:];
-[UIKeyboardMediaController _instantiateCardFromViewService];
-[UIKeyboardMediaController _setRecentlyUsedMediaViewControllerHostBundleID];
```
