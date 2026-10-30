# `UISpringLoadedInteractionContextImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISpringLoadedInteractionContext_Internal`
- 6 instance variables, 11 properties, 14 instance methods, 0 class methods

## Instance variables

```
@ targetItem;
@"UIView" targetView;
@"UIView" overrideTargetView;
@ overrideTargetItem;
q _state;
@"UISpringLoadedGestureRecognizer" _currentRecognizer;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"UISpringLoadedGestureRecognizer",W,N,V_currentRecognizer) currentRecognizer;
@property (T@"UIView",&,N,VoverrideTargetView) overrideTargetView;
@property (T@,&,N,VoverrideTargetItem) overrideTargetItem;
@property (T@"<UIDropSession>",R,N) dropSession;
@property (T@"UIView",&,N,VtargetView) targetView;
@property (T@,&,N,VtargetItem) targetItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISpringLoadedInteractionContextImpl dropSession];
-[UISpringLoadedInteractionContextImpl targetView];
-[UISpringLoadedInteractionContextImpl setState:];
-[UISpringLoadedInteractionContextImpl locationInView:];
-[UISpringLoadedInteractionContextImpl setTargetView:];
-[UISpringLoadedInteractionContextImpl state];
-[UISpringLoadedInteractionContextImpl currentRecognizer];
-[UISpringLoadedInteractionContextImpl overrideTargetItem];
-[UISpringLoadedInteractionContextImpl overrideTargetView];
-[UISpringLoadedInteractionContextImpl setCurrentRecognizer:];
-[UISpringLoadedInteractionContextImpl setOverrideTargetItem:];
-[UISpringLoadedInteractionContextImpl setOverrideTargetView:];
-[UISpringLoadedInteractionContextImpl setTargetItem:];
-[UISpringLoadedInteractionContextImpl targetItem];
```
