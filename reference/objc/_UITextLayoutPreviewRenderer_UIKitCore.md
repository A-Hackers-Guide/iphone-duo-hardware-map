# `_UITextLayoutPreviewRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextPreviewRenderer`
- 10 instance variables, 12 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _calculated;
B _unifyRects;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _firstRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _middleRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentBounds;
@"UIImage" _image;
B _excludeBackground;
@"NSTextLayoutManager" _textLayoutManager;
@"NSTextRange" _range;
```

## Properties

```
@property (T@"NSTextLayoutManager",R,N,V_textLayoutManager) textLayoutManager;
@property (T@"NSTextRange",R,N,V_range) range;
@property (T@"UIImage",R,N) image;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) firstLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bodyRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) lastLineRect;
@property (TB,N,V_excludeBackground) excludeBackground;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextLayoutPreviewRenderer contentBounds];
-[_UITextLayoutPreviewRenderer range];
-[_UITextLayoutPreviewRenderer textLayoutManager];
-[_UITextLayoutPreviewRenderer image];
-[_UITextLayoutPreviewRenderer _updateDataIfNeeded];
-[_UITextLayoutPreviewRenderer addRenderingAttributes:];
-[_UITextLayoutPreviewRenderer bodyRect];
-[_UITextLayoutPreviewRenderer excludeBackground];
-[_UITextLayoutPreviewRenderer firstLineRect];
-[_UITextLayoutPreviewRenderer initWithTextLayoutManager:range:unifyRects:];
-[_UITextLayoutPreviewRenderer lastLineRect];
-[_UITextLayoutPreviewRenderer removeRenderingAttributes:];
-[_UITextLayoutPreviewRenderer setExcludeBackground:];
```
