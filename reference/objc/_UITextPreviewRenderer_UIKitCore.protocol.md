# `_UITextPreviewRenderer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"UIImage",R,N) image;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) firstLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bodyRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) lastLineRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentBounds;
@property (TB,N) excludeBackground;
```

## Instance methods

```
-[_UITextPreviewRenderer contentBounds];
-[_UITextPreviewRenderer image];
-[_UITextPreviewRenderer addRenderingAttributes:];
-[_UITextPreviewRenderer bodyRect];
-[_UITextPreviewRenderer excludeBackground];
-[_UITextPreviewRenderer firstLineRect];
-[_UITextPreviewRenderer lastLineRect];
-[_UITextPreviewRenderer removeRenderingAttributes:];
-[_UITextPreviewRenderer setExcludeBackground:];
```
