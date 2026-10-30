# `UIEmojiAndStickerCollectionViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIKeyboardLayoutStarDelegate`
- 8 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIKeyboardLayoutStar" _layout;
@"UIKBScreenTraits" _screenTraits;
@"UIEmojiAndStickerBackgroundView" _backgroundView;
@"UIEmojiNoResultsView" _noResultsView;
B _previousShowsNoResultsView;
@"STKEmojiAndStickerCollectionViewConfiguration" _configuration;
@"<UIEmojiAndStickerCollectionViewControllerDelegate>" _delegate;
@"NSString" _bundleId;
```

## Properties

```
@property (T@"STKEmojiAndStickerCollectionViewConfiguration",&,N,V_configuration) configuration;
@property (T@"<UIEmojiAndStickerCollectionViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@,R,N) emojiKeyManager;
@property (T@"NSString",C,N,V_bundleId) bundleId;
@property (T@"NSArray",&,N) searchResults;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIEmojiAndStickerCollectionViewController handleKeyEvent:];
-[UIEmojiAndStickerCollectionViewController setSearchResults:];
-[UIEmojiAndStickerCollectionViewController searchResults];
-[UIEmojiAndStickerCollectionViewController viewIsAppearing:];
-[UIEmojiAndStickerCollectionViewController init];
-[UIEmojiAndStickerCollectionViewController viewWillDisappear:];
-[UIEmojiAndStickerCollectionViewController setConfiguration:];
-[UIEmojiAndStickerCollectionViewController setBundleId:];
-[UIEmojiAndStickerCollectionViewController viewDidLoad];
-[UIEmojiAndStickerCollectionViewController initWithConfiguration:];
-[UIEmojiAndStickerCollectionViewController _canShowWhileLocked];
-[UIEmojiAndStickerCollectionViewController setDelegate:];
-[UIEmojiAndStickerCollectionViewController configuration];
-[UIEmojiAndStickerCollectionViewController bundleId];
-[UIEmojiAndStickerCollectionViewController delegate];
-[UIEmojiAndStickerCollectionViewController viewWillLayoutSubviews];
-[UIEmojiAndStickerCollectionViewController emojiKeyManager];
-[UIEmojiAndStickerCollectionViewController addNoResultsViewIfNeeded];
-[UIEmojiAndStickerCollectionViewController handleHardwareKeyboardEvent:];
-[UIEmojiAndStickerCollectionViewController handleKeyUIEvent:dismiss:];
```
