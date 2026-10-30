# `LACUserInterfacePresenter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUserInterfacePresenting`
- 3 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"<LACUserInterfaceController>" _uiController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUserInterfacePresenter initWithReplyQueue:uiController:];
-[LACUserInterfacePresenter presentUIForIdentifier:request:completion:];
```
