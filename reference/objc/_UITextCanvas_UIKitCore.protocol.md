# `_UITextCanvas` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSTextViewportLayoutControllerDelegate_Private`
- 0 instance variables, 2 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<_UITextCanvasContext>",W,N) context;
@property (TB) layoutFragmentViewsNeedDisplay;
```

## Instance methods

```
-[_UITextCanvas layoutFragmentViewsNeedDisplay];
-[_UITextCanvas viewportBoundsDidChange];
-[_UITextCanvas isEditingDidChange];
-[_UITextCanvas flushElementViews];
-[_UITextCanvas textViewportLayoutController:retrieveCachedRenderingSurfaceForKey:];
-[_UITextCanvas observeEnclosingScrollView];
-[_UITextCanvas updateContentSizeIfNeeded];
-[_UITextCanvas setContext:];
-[_UITextCanvas textViewportLayoutController:renderingSurfaceForTextLayoutFragment:];
-[_UITextCanvas textViewportLayoutController:cacheRenderingSurface:forKey:];
-[_UITextCanvas _registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:];
-[_UITextCanvas drawTextInRect:];
-[_UITextCanvas isScrollingChangedTo:];
-[_UITextCanvas context];
-[_UITextCanvas setLayoutFragmentViewsNeedDisplay:];
-[_UITextCanvas configureCustomTextRenderer];
```
