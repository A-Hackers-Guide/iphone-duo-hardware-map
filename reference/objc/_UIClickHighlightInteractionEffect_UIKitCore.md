# `_UIClickHighlightInteractionEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickHighlightEffect`
- 7 instance variables, 9 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _phase;
q _inflightAnimationCount;
B _isActive;
@"UITargetedPreview" _targetedPreview;
@? _completionBlock;
@"_UIAnchoredClickHighlightPlatterView" _highlightPlatter;
@"UITargetedPreview" _continuationPreview;
```

## Properties

```
@property (T@"_UIAnchoredClickHighlightPlatterView",&,N,V_highlightPlatter) highlightPlatter;
@property (T@"UITargetedPreview",&,N,V_continuationPreview) continuationPreview;
@property (T@"UITargetedPreview",R,N) targetedPreviewForEffectContinuation;
@property (T@"UITargetedPreview",R,N,V_targetedPreview) targetedPreview;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIClickHighlightInteractionEffect effectWithPreview:continuingFromPreview:];
```

## Instance methods

```
-[_UIClickHighlightInteractionEffect continuationPreview];
-[_UIClickHighlightInteractionEffect setContinuationPreview:];
-[_UIClickHighlightInteractionEffect setCompletionBlock:];
-[_UIClickHighlightInteractionEffect completionBlock];
-[_UIClickHighlightInteractionEffect interaction:didChangeWithContext:];
-[_UIClickHighlightInteractionEffect targetedPreview];
-[_UIClickHighlightInteractionEffect _completeHighlightEffect];
-[_UIClickHighlightInteractionEffect _createHighlightPlatter];
-[_UIClickHighlightInteractionEffect highlightPlatter];
-[_UIClickHighlightInteractionEffect initWithTargetedPreview:continuingFromPreview:];
-[_UIClickHighlightInteractionEffect setHighlightPlatter:];
-[_UIClickHighlightInteractionEffect targetedPreviewForEffectContinuation];
```
