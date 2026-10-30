# `_UITextParagraphAnchoredAttachmentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextViewportRenderingSurface`
- 5 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UITextLayoutCanvasView" _textLayoutCanvasView;
@"NSTextLayoutFragment" _textLayoutFragment;
@"NSTextAttachmentViewProvider" _attachmentViewProvider;
B _cacheAndRetainInViewHierarchy;
@"NSTextParagraphAnchoredAttachment" _anchoredAttachment;
```

## Properties

```
@property (T@"NSTextParagraphAnchoredAttachment",R,W,V_anchoredAttachment) anchoredAttachment;
@property (T@"NSTextLayoutFragment",W,D) textLayoutFragment;
@property (TB,R,N) isLayoutFragmentView;
@property (TB,N,V_cacheAndRetainInViewHierarchy) cacheAndRetainInViewHierarchy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextParagraphAnchoredAttachmentView drawRect:];
-[_UITextParagraphAnchoredAttachmentView layoutSubviews];
-[_UITextParagraphAnchoredAttachmentView setTextLayoutFragment:];
-[_UITextParagraphAnchoredAttachmentView textLayoutFragment];
-[_UITextParagraphAnchoredAttachmentView autoresizingMask];
-[_UITextParagraphAnchoredAttachmentView anchoredAttachment];
-[_UITextParagraphAnchoredAttachmentView cacheAndRetainInViewHierarchy];
-[_UITextParagraphAnchoredAttachmentView initWithTextLayoutCanvasView:anchoredAttachment:];
-[_UITextParagraphAnchoredAttachmentView isLayoutFragmentView];
-[_UITextParagraphAnchoredAttachmentView setCacheAndRetainInViewHierarchy:];
```
