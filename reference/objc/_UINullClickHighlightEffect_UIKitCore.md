# `_UINullClickHighlightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickHighlightEffect`
- 2 instance variables, 7 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"UITargetedPreview" _targetedPreview;
@? _completionBlock;
```

## Properties

```
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
+[_UINullClickHighlightEffect effectWithPreview:continuingFromPreview:];
```

## Instance methods

```
-[_UINullClickHighlightEffect setCompletionBlock:];
-[_UINullClickHighlightEffect completionBlock];
-[_UINullClickHighlightEffect interaction:didChangeWithContext:];
-[_UINullClickHighlightEffect targetedPreview];
-[_UINullClickHighlightEffect targetedPreviewForEffectContinuation];
```
