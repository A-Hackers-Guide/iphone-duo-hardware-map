# `_UISceneHostingActivationHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingActivationHandle`, `BSInvalidatable`
- 1 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneHostingActivating>" _activationTarget;
```

## Properties

```
@property (TB,R,N,GisHandleValid) handleValid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneHostingActivationHandle deactivate:];
-[_UISceneHostingActivationHandle dealloc];
-[_UISceneHostingActivationHandle isHandleValid];
-[_UISceneHostingActivationHandle invalidate];
-[_UISceneHostingActivationHandle isActive];
-[_UISceneHostingActivationHandle activate:];
```
