# `UIKeyboardEmojiKeyDisplayController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyboardEmojiCategoryUpdateDelegate`
- 3 instance variables, 7 properties, 24 instance methods, 3 class methods

## Instance variables

```
@"UIKeyboardEmojiKeyView" _inputView;
@"UIKeyboardEmojiKeyView" _categoryView;
@"UIKeyboardEmojiCategory" _lastViewedCategory;
```

## Properties

```
@property (T@"UIKeyboardEmojiKeyView",W,N,V_inputView) inputView;
@property (T@"UIKeyboardEmojiKeyView",W,N,V_categoryView) categoryView;
@property (T@"UIKeyboardEmojiCategory",W) lastViewedCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardEmojiKeyDisplayController classForCategoryControl:];
+[UIKeyboardEmojiKeyDisplayController classForInputView:];
+[UIKeyboardEmojiKeyDisplayController writeEmojiDefaultsAndReleaseActiveInputView];
```

## Instance methods

```
-[UIKeyboardEmojiKeyDisplayController lastUsedVariantEmojiForEmojiString:];
-[UIKeyboardEmojiKeyDisplayController recentEmojiAtIndex:size:];
-[UIKeyboardEmojiKeyDisplayController init];
-[UIKeyboardEmojiKeyDisplayController dealloc];
-[UIKeyboardEmojiKeyDisplayController updateSkinToneBaseKey:variantUsed:];
-[UIKeyboardEmojiKeyDisplayController emojiUsed:language:];
-[UIKeyboardEmojiKeyDisplayController hasLastUsedVariantForEmojiString:];
-[UIKeyboardEmojiKeyDisplayController skinToneBaseKeyPreferences];
-[UIKeyboardEmojiKeyDisplayController inputView];
-[UIKeyboardEmojiKeyDisplayController recents];
-[UIKeyboardEmojiKeyDisplayController emojiUsed:];
-[UIKeyboardEmojiKeyDisplayController emojiWithoutDuplicateRecents:];
-[UIKeyboardEmojiKeyDisplayController setInputView:];
-[UIKeyboardEmojiKeyDisplayController categoryView];
-[UIKeyboardEmojiKeyDisplayController didVisitIndexPath:withSender:];
-[UIKeyboardEmojiKeyDisplayController lastViewedCategory];
-[UIKeyboardEmojiKeyDisplayController lastVisibleFirstEmojiIndexforCategory:];
-[UIKeyboardEmojiKeyDisplayController reloadCategoryForIndexPath:withSender:];
-[UIKeyboardEmojiKeyDisplayController reloadCategoryForOffsetPercentage:withSender:];
-[UIKeyboardEmojiKeyDisplayController reloadForCategory:withSender:];
-[UIKeyboardEmojiKeyDisplayController setCategoryView:];
-[UIKeyboardEmojiKeyDisplayController setLastViewedCategory:];
-[UIKeyboardEmojiKeyDisplayController updateEmojiKeyManagerWithKey:withKeyView:];
-[UIKeyboardEmojiKeyDisplayController userHasSelectedSkinToneEmoji];
```
