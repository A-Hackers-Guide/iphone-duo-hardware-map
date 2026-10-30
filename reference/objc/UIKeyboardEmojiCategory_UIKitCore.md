# `UIKeyboardEmojiCategory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 15 instance methods, 22 class methods

## Instance variables

```
q _categoryType;
@"NSArray" _emoji;
q _lastVisibleFirstEmojiIndex;
@"NSMutableDictionary" _localizedNames;
@"NSMutableDictionary" _shortLocalizedNames;
@"NSString" _displaySymbol;
```

## Properties

```
@property (Tq,V_categoryType) categoryType;
@property (T@"NSMutableDictionary",&,V_localizedNames) localizedNames;
@property (T@"NSMutableDictionary",&,V_shortLocalizedNames) shortLocalizedNames;
@property (T@"NSArray",&,V_emoji) emoji;
@property (Tq,N,V_lastVisibleFirstEmojiIndex) lastVisibleFirstEmojiIndex;
@property (T@"NSString",R,N,Gname) name;
@property (T@"NSString",R,GdisplaySymbol,V_displaySymbol) displaySymbol;
```

## Class methods

```
+[UIKeyboardEmojiCategory localizedStringForKey:];
+[UIKeyboardEmojiCategory isRTLMode];
+[UIKeyboardEmojiCategory numberOfCategories];
+[UIKeyboardEmojiCategory professionSkinToneEmojiBaseKey:];
+[UIKeyboardEmojiCategory sharedManager];
+[UIKeyboardEmojiCategory categories];
+[UIKeyboardEmojiCategory allowedCategoryIndexes];
+[UIKeyboardEmojiCategory categoriesByType];
+[UIKeyboardEmojiCategory categoryForType:];
+[UIKeyboardEmojiCategory categoryIndexForCategoryType:];
+[UIKeyboardEmojiCategory categoryTypeForCategoryIndex:];
+[UIKeyboardEmojiCategory displayName:];
+[UIKeyboardEmojiCategory doesShowStickers];
+[UIKeyboardEmojiCategory emojiCategoryStringForCategoryType:];
+[UIKeyboardEmojiCategory emojiCategoryTypeForCategoryString:];
+[UIKeyboardEmojiCategory emojiRecentsFromPreferences];
+[UIKeyboardEmojiCategory enabledCategoryIndexes];
+[UIKeyboardEmojiCategory fallbackDisplayName:];
+[UIKeyboardEmojiCategory hasVariantsForEmoji:];
+[UIKeyboardEmojiCategory isEmojiKeyboardIntelligenceCategoryEnabled];
+[UIKeyboardEmojiCategory loadPrecomputedEmojiFlagCategory];
+[UIKeyboardEmojiCategory setDoesShowStickers:];
```

## Instance methods

```
-[UIKeyboardEmojiCategory setCategoryType:];
-[UIKeyboardEmojiCategory categoryType];
-[UIKeyboardEmojiCategory dealloc];
-[UIKeyboardEmojiCategory name];
-[UIKeyboardEmojiCategory localizedNames];
-[UIKeyboardEmojiCategory localeDidChange];
-[UIKeyboardEmojiCategory displaySymbol];
-[UIKeyboardEmojiCategory emoji];
-[UIKeyboardEmojiCategory lastVisibleFirstEmojiIndex];
-[UIKeyboardEmojiCategory releaseCategories];
-[UIKeyboardEmojiCategory setEmoji:];
-[UIKeyboardEmojiCategory setLastVisibleFirstEmojiIndex:];
-[UIKeyboardEmojiCategory setLocalizedNames:];
-[UIKeyboardEmojiCategory setShortLocalizedNames:];
-[UIKeyboardEmojiCategory shortLocalizedNames];
```
