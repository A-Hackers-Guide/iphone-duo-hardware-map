# `LAContextUIHelper`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACContextObserver`
- 1 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"LAAuthorizationViewController" _ui;
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
-[LAContextUIHelper dealloc];
-[LAContextUIHelper cancel];
-[LAContextUIHelper contextDidBecomeInvalid:];
-[LAContextUIHelper authenticateWithOptions:availableMechanisms:hostVC:context:reply:];
```
