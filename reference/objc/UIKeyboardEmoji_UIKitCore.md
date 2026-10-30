# `UIKeyboardEmoji`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
B _isFromRecentsCategory;
B _isFromEmojiSearch;
@"NSString" _emojiString;
Q _variantMask;
```

## Properties

```
@property (T@"NSString",&,N,V_emojiString) emojiString;
@property (TQ,V_variantMask) variantMask;
@property (TB,R,N) supportsSkinToneVariants;
@property (TB,N,V_isFromRecentsCategory) isFromRecentsCategory;
@property (TB,N,V_isFromEmojiSearch) isFromEmojiSearch;
```

## Class methods

```
+[UIKeyboardEmoji emojiWithString:withVariantMask:];
+[UIKeyboardEmoji shouldHighlightEmoji:];
```

## Instance methods

```
-[UIKeyboardEmoji supportsSkinToneVariants];
-[UIKeyboardEmoji isEqual:];
-[UIKeyboardEmoji key];
-[UIKeyboardEmoji setEmojiString:];
-[UIKeyboardEmoji initWithString:withVariantMask:];
-[UIKeyboardEmoji setVariantMask:];
-[UIKeyboardEmoji emojiString];
-[UIKeyboardEmoji isFromEmojiSearch];
-[UIKeyboardEmoji isFromRecentsCategory];
-[UIKeyboardEmoji setIsFromEmojiSearch:];
-[UIKeyboardEmoji setIsFromRecentsCategory:];
-[UIKeyboardEmoji variantMask];
```
