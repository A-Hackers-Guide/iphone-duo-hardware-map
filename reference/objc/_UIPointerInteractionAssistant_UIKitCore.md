# `_UIPointerInteractionAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPointerInteraction`
- Protocols: `_UIViewSubtreeMonitor`, `UIPointerInteractionDelegate`, `UIInteraction_Internal`
- 3 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"_UIPointerInteractionAssistantEffectContainerView" _previewContainer;
@"UIWindow" _manual_weak_monitoredWindow;
@"NSMutableDictionary" _assistants;
```

## Properties

```
@property (T@"UIView",R,N) previewContainer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N) view;
```

## Instance methods

```
-[_UIPointerInteractionAssistant _willMoveFromWindow:toWindow:];
-[_UIPointerInteractionAssistant initWithDelegate:];
-[_UIPointerInteractionAssistant pointerInteraction:styleForRegion:];
-[_UIPointerInteractionAssistant createRegionFromRect:targetView:identifier:selected:];
-[_UIPointerInteractionAssistant init];
-[_UIPointerInteractionAssistant pointerInteraction:willEnterRegion:animator:];
-[_UIPointerInteractionAssistant pointerInteraction:willExitRegion:animator:];
-[_UIPointerInteractionAssistant createPreviewTargetForView:center:];
-[_UIPointerInteractionAssistant _monitoredView:didMoveFromSuperview:toSuperview:];
-[_UIPointerInteractionAssistant setAssistedView:identifier:];
-[_UIPointerInteractionAssistant _monitoredView:willMoveFromSuperview:toSuperview:];
-[_UIPointerInteractionAssistant willMoveToView:];
-[_UIPointerInteractionAssistant pointerInteraction:regionForRequest:defaultRegion:];
-[_UIPointerInteractionAssistant _monitorsView:];
-[_UIPointerInteractionAssistant createStyleForButton:shapeProvider:];
-[_UIPointerInteractionAssistant request:locationInView:];
-[_UIPointerInteractionAssistant previewContainer];
-[_UIPointerInteractionAssistant setAssistedView:delegate:identifier:];
```
