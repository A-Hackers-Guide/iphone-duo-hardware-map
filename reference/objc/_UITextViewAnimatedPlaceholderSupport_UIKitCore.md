# `_UITextViewAnimatedPlaceholderSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP5UIKit22UITextEffectViewSource_`
- 6 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
? textView;
$__lazy_storage_$_containerView;
$__lazy_storage_$_textEffectsView;
completionBlocks;
activeReplacementEffect;
activePlaceholders;
```

## Properties

```
@property (T@"UITextView",N,W,VtextView) textView;
```

## Instance methods

```
-[_UITextViewAnimatedPlaceholderSupport setTextView:];
-[_UITextViewAnimatedPlaceholderSupport canGenerateTargetedPreviewsWithCompletionHandler:];
-[_UITextViewAnimatedPlaceholderSupport textView];
-[_UITextViewAnimatedPlaceholderSupport targetedPreviewFor:completionHandler:];
-[_UITextViewAnimatedPlaceholderSupport updateTextChunkVisibilityForAnimation:visible:completionHandler:];
-[_UITextViewAnimatedPlaceholderSupport init];
-[_UITextViewAnimatedPlaceholderSupport initWithTextView:];
-[_UITextViewAnimatedPlaceholderSupport canGenerateTargetedPreviewForChunk:completionHandler:];
-[_UITextViewAnimatedPlaceholderSupport insertAttributedTextUsingReplacementEffect:completion:];
-[_UITextViewAnimatedPlaceholderSupport insertLoadingPlaceholderAtLocation:lines:completion:];
-[_UITextViewAnimatedPlaceholderSupport layoutManagedSubviews];
-[_UITextViewAnimatedPlaceholderSupport removePlaceholder:];
-[_UITextViewAnimatedPlaceholderSupport replacePlaceholder:withText:completion:];
-[_UITextViewAnimatedPlaceholderSupport replaceRangeUsingReplacementEffect:withAttributedText:completion:];
```
