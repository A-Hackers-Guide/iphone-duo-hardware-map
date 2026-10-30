# `_UIDragSourceLiftEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionEffect`
- 2 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _liftOperationByContext;
B _scrollCancelling;
```

## Properties

```
@property (TB,N,V_scrollCancelling) scrollCancelling;
@property (T@"<UITimingCurveProvider>",R,N) liftTimingParameters;
@property (Td,R,N) liftAnimationDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDragSourceLiftEffect _uninstallInteractionPlattersForOperation:];
-[_UIDragSourceLiftEffect init];
-[_UIDragSourceLiftEffect existingOperationForContext:];
-[_UIDragSourceLiftEffect setScrollCancelling:];
-[_UIDragSourceLiftEffect _setInteractionEffectsLifted:withOperation:];
-[_UIDragSourceLiftEffect interaction:didChangeWithContext:];
-[_UIDragSourceLiftEffect liftTimingParameters];
-[_UIDragSourceLiftEffect liftAnimationDuration];
-[_UIDragSourceLiftEffect _addworkaroundForPropertyAnimator:inView:];
-[_UIDragSourceLiftEffect _installInteractionPlattersForOperation:];
-[_UIDragSourceLiftEffect reversedTimingParametersForTimingParameters:];
-[_UIDragSourceLiftEffect scrollCancelling];
```
