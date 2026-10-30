# `LACUIPackagedViewStateController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUIPackagedViewPlatformStateControllerDelegate`
- 2 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<LACUIPackagedViewPlatformStateController>" _stateController;
@"LACUIPackagedViewStateTransition" _pendingStateTransition;
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
-[LACUIPackagedViewStateController setState:animated:completion:];
-[LACUIPackagedViewStateController initWithLayer:];
-[LACUIPackagedViewStateController setInitialState];
-[LACUIPackagedViewStateController _clearPendingTransitionWithFlag:];
-[LACUIPackagedViewStateController initWithPlatformStateController:];
-[LACUIPackagedViewStateController packagedViewPlatformStateController:didTransitionToState:completed:];
```
