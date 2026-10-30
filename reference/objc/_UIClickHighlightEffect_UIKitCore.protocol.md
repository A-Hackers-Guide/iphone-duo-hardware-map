# `_UIClickHighlightEffect` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIInteractionEffect`
- 0 instance variables, 3 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"UITargetedPreview",R,N) targetedPreviewForEffectContinuation;
@property (T@"UITargetedPreview",R,N) targetedPreview;
@property (T@?,C,N) completionBlock;
```

## Class methods

```
+[_UIClickHighlightEffect effectWithPreview:continuingFromPreview:];
```

## Instance methods

```
-[_UIClickHighlightEffect setCompletionBlock:];
-[_UIClickHighlightEffect completionBlock];
-[_UIClickHighlightEffect targetedPreview];
-[_UIClickHighlightEffect targetedPreviewForEffectContinuation];
```
