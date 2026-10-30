# `LAPreboard`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPreboard.framework/LocalAuthenticationPreboard`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPreboard.framework__LocalAuthenticationPreboard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPreboardType`
- 1 instance variables, 13 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"<LACPreboardControlling>" controller;
```

## Properties

```
@property (T@"<LACPreboardControlling>",N,R,Vcontroller) controller;
@property (T@"NSString",N,R) iconSystemName;
@property (T@"NSString",N,R) title;
@property (T@"NSString",N,R) message;
@property (T@"NSArray",N,R) items;
@property (T@"NSString",N,R) confirmationTitle;
@property (T@"NSString",N,R) confirmationMessage;
@property (T@"NSString",N,R) confirmationActionTitle;
@property (T@"NSString",N,R) confirmationCancelTitle;
@property (T@"NSString",N,R) passcodeTitle;
@property (T@"NSString",N,R) passcodeSubtitle;
@property (TB,N,R) isRequired;
@property (Tq,N,R) useCase;
```

## Class methods

```
+[LAPreboard sharedInstance];
```

## Instance methods

```
-[LAPreboard useCase];
-[LAPreboard controller];
-[LAPreboard init];
-[LAPreboard message];
-[LAPreboard isRequired];
-[LAPreboard items];
-[LAPreboard title];
-[LAPreboard initWithController:];
-[LAPreboard iconSystemName];
-[LAPreboard confirmationTitle];
-[LAPreboard confirmationMessage];
-[LAPreboard enableCurrentUseCaseWithSecurePasscode:completion:];
-[LAPreboard launchPreboardWithCompletion:];
-[LAPreboard terminateWithCompletion:];
-[LAPreboard passcodeTitle];
-[LAPreboard actionTitleWithHomeButton:];
-[LAPreboard confirmationActionTitle];
-[LAPreboard confirmationCancelTitle];
-[LAPreboard enableCurrentUseCaseWithPasscode:completion:];
-[LAPreboard passcodeSubtitle];
```
