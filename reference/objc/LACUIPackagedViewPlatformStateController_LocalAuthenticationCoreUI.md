# `LACUIPackagedViewPlatformStateController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAStateControllerDelegate`, `LACUIPackagedViewPlatformStateController`
- 2 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CAStateController" _stateController;
@"<LACUIPackagedViewPlatformStateControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<LACUIPackagedViewPlatformStateControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUIPackagedViewPlatformStateController stateController:transitionDidStart:speed:];
-[LACUIPackagedViewPlatformStateController stateController:didSetStateOfLayer:];
-[LACUIPackagedViewPlatformStateController stateController:transitionDidStop:completed:];
-[LACUIPackagedViewPlatformStateController hasState:];
-[LACUIPackagedViewPlatformStateController initWithLayer:];
-[LACUIPackagedViewPlatformStateController setDelegate:];
-[LACUIPackagedViewPlatformStateController delegate];
-[LACUIPackagedViewPlatformStateController description];
-[LACUIPackagedViewPlatformStateController state];
-[LACUIPackagedViewPlatformStateController setInitialState];
-[LACUIPackagedViewPlatformStateController setState:speed:];
```
