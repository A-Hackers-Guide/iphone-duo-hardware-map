# `_UIContextMenuAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIContextMenuInteractionCommitAnimating`
- 4 instance variables, 9 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _preferredCommitStyle;
@"UIViewController" _previewViewController;
@"NSMutableArray" _animations;
@"NSMutableArray" _completions;
```

## Properties

```
@property (TB,R,N) hasAnyActions;
@property (T@"NSMutableArray",R,N,V_animations) animations;
@property (T@"NSMutableArray",R,N,V_completions) completions;
@property (Tq,N,V_preferredCommitStyle) preferredCommitStyle;
@property (T@"UIViewController",R,N,V_previewViewController) previewViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIContextMenuAnimator animatorWithViewController:];
```

## Instance methods

```
-[_UIContextMenuAnimator addAnimations:];
-[_UIContextMenuAnimator addCompletion:];
-[_UIContextMenuAnimator animations];
-[_UIContextMenuAnimator completions];
-[_UIContextMenuAnimator performAllCompletions];
-[_UIContextMenuAnimator hasAnyActions];
-[_UIContextMenuAnimator preferredCommitStyle];
-[_UIContextMenuAnimator setPreferredCommitStyle:];
-[_UIContextMenuAnimator previewViewController];
-[_UIContextMenuAnimator performAllAnimations];
```
