# `LAPSPasscodeChangeSystemDispatchDecorator`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeSystem`
- 2 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<LAPSPasscodeChangeSystem>" _system;
@"NSObject<OS_dispatch_queue>" _workQueue;
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
-[LAPSPasscodeChangeSystemDispatchDecorator hasPasscode];
-[LAPSPasscodeChangeSystemDispatchDecorator initWithSystem:];
-[LAPSPasscodeChangeSystemDispatchDecorator _performOnBackgroundQueue:];
-[LAPSPasscodeChangeSystemDispatchDecorator _performOnMainQueue:];
-[LAPSPasscodeChangeSystemDispatchDecorator canChangePasscodeWithError:];
-[LAPSPasscodeChangeSystemDispatchDecorator changePasscode:to:completion:];
-[LAPSPasscodeChangeSystemDispatchDecorator initWithSystem:workQueue:];
-[LAPSPasscodeChangeSystemDispatchDecorator lastPasscodeChange];
-[LAPSPasscodeChangeSystemDispatchDecorator newPasscodeRequest];
-[LAPSPasscodeChangeSystemDispatchDecorator oldPasscodeRequest];
-[LAPSPasscodeChangeSystemDispatchDecorator verifyNewPasscode:completion:];
-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:completion:];
-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:contextRef:completion:];
```
