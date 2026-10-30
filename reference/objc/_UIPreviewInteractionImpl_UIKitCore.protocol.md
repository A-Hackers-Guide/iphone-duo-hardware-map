# `_UIPreviewInteractionImpl` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"<UIPreviewInteractionDelegate>",W,N) delegate;
@property (T@"UIView",R,W,N) view;
@property (T@"<_UIPreviewInteractionTouchForceProviding>",&,N) touchForceProvider;
@property (T@"UIPreviewInteraction",W,N) previewInteraction;
```

## Instance methods

```
-[_UIPreviewInteractionImpl locationInCoordinateSpace:];
-[_UIPreviewInteractionImpl cancelInteraction];
-[_UIPreviewInteractionImpl view];
-[_UIPreviewInteractionImpl setDelegate:];
-[_UIPreviewInteractionImpl delegate];
-[_UIPreviewInteractionImpl _startPreviewAtLocation:inCoordinateSpace:];
-[_UIPreviewInteractionImpl initWithView:previewInteraction:];
-[_UIPreviewInteractionImpl previewInteraction];
-[_UIPreviewInteractionImpl setPreviewInteraction:];
-[_UIPreviewInteractionImpl setTouchForceProvider:];
-[_UIPreviewInteractionImpl touchForceProvider];
```
