# `UIKeyboardEmojiVariantView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIKBKeyViewContentView`
- 3 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"UIKeyboardEmojiVariantDivider" _divider;
@"NSMutableArray" _cells;
@"UIView" _touchForwardingView;
```

## Properties

```
@property (T@"UIView",&,N,V_touchForwardingView) touchForwardingView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardEmojiVariantView preferredContentViewSizeForKey:withTraits:];
```

## Instance methods

```
-[UIKeyboardEmojiVariantView retestSelectedVariantIndexForKey:atPoint:phase:];
-[UIKeyboardEmojiVariantView updateForKeyplane:key:];
-[UIKeyboardEmojiVariantView nextResponder];
-[UIKeyboardEmojiVariantView initWithFrame:];
-[UIKeyboardEmojiVariantView setTouchForwardingView:];
-[UIKeyboardEmojiVariantView touchForwardingView];
-[UIKeyboardEmojiVariantView updateHighlightForSelectedVariantIndex:];
-[UIKeyboardEmojiVariantView updateRenderConfig:];
-[UIKeyboardEmojiVariantView updateSelectedVariantIndexForKey:atPoint:];
```
