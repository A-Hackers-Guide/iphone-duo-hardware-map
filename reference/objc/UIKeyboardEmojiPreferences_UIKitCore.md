# `UIKeyboardEmojiPreferences`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 47 instance methods, 1 class methods

## Instance variables

```
@"EMFEmojiPreferencesClient" _preferencesClient;
@"NSObject<OS_dispatch_queue>" _clientDispatchQueue;
@"NSArray" _localRecentsWithClient;
@"NSArray" _localRecentsWithoutClient;
B _deviceWasLockedWhenKeyboardWasShown;
B _hasCheckedMemojiPreference;
B _supportsMemoji;
```

## Properties

```
@property (T@"EMFEmojiPreferencesClient",R,N) preferencesClient;
@property (TB,N,V_hasCheckedMemojiPreference) hasCheckedMemojiPreference;
@property (TB,N,V_supportsMemoji) supportsMemoji;
@property (TQ,N) maximumRecentsCount;
@property (T@"NSArray",&,N) recents;
@property (T@"NSDictionary",&,N) skinToneBaseKeyPreferences;
@property (Tq,N) selectedCategoryType;
@property (TB,R,N) hasDisplayedSkinToneHelp;
```

## Class methods

```
+[UIKeyboardEmojiPreferences sharedInstance];
```

## Instance methods

```
-[UIKeyboardEmojiPreferences didDisplaySkinToneHelp];
-[UIKeyboardEmojiPreferences lastUsedVariantEmojiForEmojiString:];
-[UIKeyboardEmojiPreferences recentEmojiAtIndex:size:];
-[UIKeyboardEmojiPreferences hasCheckedMemojiPreference];
-[UIKeyboardEmojiPreferences setSupportsMemoji:];
-[UIKeyboardEmojiPreferences preferencesControllerChanged:];
-[UIKeyboardEmojiPreferences setSkinToneBaseKeyPreferences:];
-[UIKeyboardEmojiPreferences emojiUsedFromEmojiKeyboardSearch:inputModeIdentifier:resultIndex:query:completionHandler:];
-[UIKeyboardEmojiPreferences handleSuspend:];
-[UIKeyboardEmojiPreferences init];
-[UIKeyboardEmojiPreferences setSelectedCategoryType:];
-[UIKeyboardEmojiPreferences shouldShowRecents];
-[UIKeyboardEmojiPreferences refreshLocalRecents];
-[UIKeyboardEmojiPreferences handleWrite:];
-[UIKeyboardEmojiPreferences dealloc];
-[UIKeyboardEmojiPreferences writeEmojiDefaults];
-[UIKeyboardEmojiPreferences memojiSettingEnabled];
-[UIKeyboardEmojiPreferences updateSkinToneBaseKey:variantUsed:];
-[UIKeyboardEmojiPreferences clearLocalRecentsCache];
-[UIKeyboardEmojiPreferences emojiUsed:language:];
-[UIKeyboardEmojiPreferences handleBackground:];
-[UIKeyboardEmojiPreferences handleRead:];
-[UIKeyboardEmojiPreferences setMaximumRecentsCount:];
-[UIKeyboardEmojiPreferences preferencesClient];
-[UIKeyboardEmojiPreferences readEmojiDefaults];
-[UIKeyboardEmojiPreferences hasLastUsedVariantForEmojiString:];
-[UIKeyboardEmojiPreferences clearEmojiKeyboardPreferenceClient];
-[UIKeyboardEmojiPreferences skinToneBaseKeyPreferences];
-[UIKeyboardEmojiPreferences emojiPredicted:typingName:language:];
-[UIKeyboardEmojiPreferences _usageForEmoji:language:associatedText:resultIndex:isFromRecentsCategory:isFromEmojiSearch:isFromCandidateBar:completionHandler:];
-[UIKeyboardEmojiPreferences maximumRecentsCount];
-[UIKeyboardEmojiPreferences emojiCategoryDefaultsIndex:];
-[UIKeyboardEmojiPreferences setEmojiCategoryDefaultsIndex:forCategory:];
-[UIKeyboardEmojiPreferences supportsMemoji];
-[UIKeyboardEmojiPreferences recents];
-[UIKeyboardEmojiPreferences setRecents:];
-[UIKeyboardEmojiPreferences emojiUsed:];
-[UIKeyboardEmojiPreferences emojiWithoutDuplicateRecents:];
-[UIKeyboardEmojiPreferences _updateCachedDeviceLockState];
-[UIKeyboardEmojiPreferences _validatedRecentTokens];
-[UIKeyboardEmojiPreferences deviceSupportsMemoji];
-[UIKeyboardEmojiPreferences hasDisplayedSkinToneHelp];
-[UIKeyboardEmojiPreferences emojiUsed:language:completion:];
-[UIKeyboardEmojiPreferences setHasCheckedMemojiPreference:];
-[UIKeyboardEmojiPreferences typingNameForEmoji:language:];
-[UIKeyboardEmojiPreferences emojiUsedFromEmojiKeyboardPalette:inputModeIdentifier:completionHandler:];
-[UIKeyboardEmojiPreferences selectedCategoryType];
```
