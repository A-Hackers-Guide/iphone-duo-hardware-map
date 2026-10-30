# `AVCaptionRenderer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"AVCaptionRendererInternal" _internal;
```

## Properties

```
@property (T@"NSArray",C,N) captions;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) bounds;
```

## Class methods

```
+[AVCaptionRenderer captionPreviewForProfileID:extendedLanguageTag:renderSize:];
```

## Instance methods

```
-[AVCaptionRenderer init];
-[AVCaptionRenderer dealloc];
-[AVCaptionRenderer setBounds:];
-[AVCaptionRenderer bounds];
-[AVCaptionRenderer description];
-[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession];
-[AVCaptionRenderer captionSceneChangesInRange:];
-[AVCaptionRenderer captions];
-[AVCaptionRenderer defaultStyles];
-[AVCaptionRenderer renderInContext:atTime:];
-[AVCaptionRenderer renderInContext:forTime:];
-[AVCaptionRenderer setCaptions:];
-[AVCaptionRenderer setDefaultStyles:];
-[AVCaptionRenderer setupFigCaptionClient];
-[AVCaptionRenderer synchronizeWithCurrentAccessibilityPreferencesWithCompletionHandler:];
-[AVCaptionRenderer teardownFigCaptionClient];
```
