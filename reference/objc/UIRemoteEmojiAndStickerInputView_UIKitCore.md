# `UIRemoteEmojiAndStickerInputView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBViewControllerBackedKeyView`
- Protocols: `STKEmojiAndStickerCollectionViewControllerDelegate`, `_UIStickerPickerKeyboardSessionDelegate`
- 7 instance variables, 9 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"STKEmojiAndStickerCollectionViewController" _viewController;
@"UIKBTree" _keyplane;
B _isInSearchPopover;
B _focusingCollectionView;
@"TUIEmojiSearchInputViewController" _emojiSearchInputViewController;
@"TUIEmojiSearchTextField" _emojiSearchField;
@ _emojiKeyManager;
```

## Properties

```
@property (T@,W,N,V_emojiKeyManager) emojiKeyManager;
@property (TB,N,V_isInSearchPopover) isInSearchPopover;
@property (TB,N,V_focusingCollectionView) focusingCollectionView;
@property (T@"TUIEmojiSearchInputViewController",&,N,V_emojiSearchInputViewController) emojiSearchInputViewController;
@property (T@"TUIEmojiSearchTextField",&,N,V_emojiSearchField) emojiSearchField;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIRemoteEmojiAndStickerInputView handleKeyEvent:];
-[UIRemoteEmojiAndStickerInputView emojiSearchTextFieldDidBecomeInactive:];
-[UIRemoteEmojiAndStickerInputView emojiSearchTextFieldDidBecomeActive:];
-[UIRemoteEmojiAndStickerInputView emojiSearchTextFieldWillBecomeInactive:];
-[UIRemoteEmojiAndStickerInputView emojiSearchTextFieldWillBecomeActive:];
-[UIRemoteEmojiAndStickerInputView didSelectEmoji:dismiss:];
-[UIRemoteEmojiAndStickerInputView didSelectSticker:dismiss:];
-[UIRemoteEmojiAndStickerInputView contentViewController];
-[UIRemoteEmojiAndStickerInputView didSelectPresentPicker];
-[UIRemoteEmojiAndStickerInputView hitTest:withEvent:];
-[UIRemoteEmojiAndStickerInputView didSelectEmoji:];
-[UIRemoteEmojiAndStickerInputView setFrame:];
-[UIRemoteEmojiAndStickerInputView emojiKeyManager];
-[UIRemoteEmojiAndStickerInputView didSelectSticker:];
-[UIRemoteEmojiAndStickerInputView setEmojiKeyManager:];
-[UIRemoteEmojiAndStickerInputView didSelectEditWithStickerIdentifer:sourceRect:];
-[UIRemoteEmojiAndStickerInputView emojiSearchField];
-[UIRemoteEmojiAndStickerInputView emojiSearchInputViewController];
-[UIRemoteEmojiAndStickerInputView emojiSearchTextField:shouldSendQuery:];
-[UIRemoteEmojiAndStickerInputView focusingCollectionView];
-[UIRemoteEmojiAndStickerInputView initWithFrame:keyplane:key:screenTraits:];
-[UIRemoteEmojiAndStickerInputView isInSearchPopover];
-[UIRemoteEmojiAndStickerInputView setEmojiSearchField:];
-[UIRemoteEmojiAndStickerInputView setEmojiSearchInputViewController:];
-[UIRemoteEmojiAndStickerInputView setFocusingCollectionView:];
-[UIRemoteEmojiAndStickerInputView setIsInSearchPopover:];
-[UIRemoteEmojiAndStickerInputView shouldCutAHoleForEmojiSearchField];
-[UIRemoteEmojiAndStickerInputView willHideStickerEditor];
-[UIRemoteEmojiAndStickerInputView willShowStickerEditor];
```
