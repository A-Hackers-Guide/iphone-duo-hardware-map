# `LAUIPKGlyphWrapper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 13 instance methods, 3 class methods

## Instance variables

```
B _hidden;
B _fastAnimations;
B _grayedOut;
@"UIView" _view;
@"UIView<GlyphMethods>" _glyphView;
@"UIView<GlyphMethods>" _idleTouchID;
@"NSObject<OS_dispatch_queue>" _glyphQueue;
```

## Properties

```
@property (T@"UIView<GlyphMethods>",R,N,V_glyphView) glyphView;
@property (T@"UIView<GlyphMethods>",R,N,V_idleTouchID) idleTouchID;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_glyphQueue) glyphQueue;
@property (T@"UIView",R,N,V_view) view;
@property (TB,N,V_fastAnimations) fastAnimations;
@property (TB,N,V_grayedOut) grayedOut;
@property (TB,N,V_hidden) hidden;
```

## Class methods

```
+[LAUIPKGlyphWrapper _loadClassFromString:];
+[LAUIPKGlyphWrapper _loadPKUI];
+[LAUIPKGlyphWrapper glyphWithStyle:frame:];
```

## Instance methods

```
-[LAUIPKGlyphWrapper setHidden:];
-[LAUIPKGlyphWrapper view];
-[LAUIPKGlyphWrapper glyphView];
-[LAUIPKGlyphWrapper hidden];
-[LAUIPKGlyphWrapper setFastAnimations:];
-[LAUIPKGlyphWrapper initWithGlyphView:];
-[LAUIPKGlyphWrapper _minimumAnimationDurationForState:];
-[LAUIPKGlyphWrapper fastAnimations];
-[LAUIPKGlyphWrapper glyphQueue];
-[LAUIPKGlyphWrapper grayedOut];
-[LAUIPKGlyphWrapper idleTouchID];
-[LAUIPKGlyphWrapper setGrayedOut:];
-[LAUIPKGlyphWrapper setState:idleTouchID:animated:completionHandler:];
```
