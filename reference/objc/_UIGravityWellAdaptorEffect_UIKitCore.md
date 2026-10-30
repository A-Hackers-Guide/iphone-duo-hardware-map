# `_UIGravityWellAdaptorEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIGravityWellEffect`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
d _maxProgress;
@"<_UIClickHighlightEffect>" _adaptedEffect;
@"_UIGravityWellAdaptorInteraction" _adaptorInteraction;
```

## Properties

```
@property (T@"<_UIClickHighlightEffect>",&,N,V_adaptedEffect) adaptedEffect;
@property (T@"_UIGravityWellAdaptorInteraction",&,N,V_adaptorInteraction) adaptorInteraction;
@property (Td,N,V_maxProgress) maxProgress;
```

## Class methods

```
+[_UIGravityWellAdaptorEffect effectWithAdaptedClickEffect:];
```

## Instance methods

```
-[_UIGravityWellAdaptorEffect addCompletion:];
-[_UIGravityWellAdaptorEffect updateWithProgress:];
-[_UIGravityWellAdaptorEffect secondaryBodyPreviews];
-[_UIGravityWellAdaptorEffect previewForContinuingToEffectWithPreview:];
-[_UIGravityWellAdaptorEffect begin];
-[_UIGravityWellAdaptorEffect setAdaptedEffect:];
-[_UIGravityWellAdaptorEffect end];
-[_UIGravityWellAdaptorEffect adaptorInteraction];
-[_UIGravityWellAdaptorEffect setMaxProgress:];
-[_UIGravityWellAdaptorEffect endForHandOff];
-[_UIGravityWellAdaptorEffect setAdaptorInteraction:];
-[_UIGravityWellAdaptorEffect maxProgress];
-[_UIGravityWellAdaptorEffect adaptedEffect];
```
