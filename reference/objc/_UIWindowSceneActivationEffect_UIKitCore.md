# `_UIWindowSceneActivationEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentEffect`
- 6 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<_UIContentEffectDescriptor>" _descriptor;
@"UIView" _platterContainer;
@"NSMutableArray" _completions;
@"_UIHighlightPlatterView" _platterView;
q _state;
d _currentScale;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_completions) completions;
@property (T@"_UIHighlightPlatterView",&,N,V_platterView) platterView;
@property (Tq,N,V_state) state;
@property (Td,N,V_currentScale) currentScale;
@property (T@"UITargetedPreview",R,N) handOffPreview;
@property (T@"UIView",R,N,V_platterContainer) platterContainer;
@property (T@"<_UIContentEffectDescriptor>",R,N,V_descriptor) descriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIWindowSceneActivationEffect platterView];
-[_UIWindowSceneActivationEffect addCompletion:];
-[_UIWindowSceneActivationEffect setDescriptor:andKey:];
-[_UIWindowSceneActivationEffect previewForContinuingToEffectWithPreview:];
-[_UIWindowSceneActivationEffect setState:];
-[_UIWindowSceneActivationEffect setPlatterView:];
-[_UIWindowSceneActivationEffect descriptor];
-[_UIWindowSceneActivationEffect begin];
-[_UIWindowSceneActivationEffect completions];
-[_UIWindowSceneActivationEffect initWithDescriptor:];
-[_UIWindowSceneActivationEffect state];
-[_UIWindowSceneActivationEffect _shadowBehavior];
-[_UIWindowSceneActivationEffect advanceToScale:];
-[_UIWindowSceneActivationEffect _interactiveScaleBehavior];
-[_UIWindowSceneActivationEffect _performAllCompletionBlocks];
-[_UIWindowSceneActivationEffect _settlingBehavior];
-[_UIWindowSceneActivationEffect currentScale];
-[_UIWindowSceneActivationEffect endExpanded:withVelocity:];
-[_UIWindowSceneActivationEffect handOffPreview];
-[_UIWindowSceneActivationEffect platterContainer];
-[_UIWindowSceneActivationEffect setCurrentScale:];
```
