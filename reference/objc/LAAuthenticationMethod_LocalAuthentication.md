# `LAAuthenticationMethod`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
B _running;
@"LAAuthenticationMethodConfiguration" _configuration;
```

## Properties

```
@property (T@"LAAuthenticationMethodConfiguration",R,N,V_configuration) configuration;
```

## Instance methods

```
-[LAAuthenticationMethod terminate];
-[LAAuthenticationMethod dealloc];
-[LAAuthenticationMethod start];
-[LAAuthenticationMethod initWithConfiguration:];
-[LAAuthenticationMethod addObserver:];
-[LAAuthenticationMethod configuration];
-[LAAuthenticationMethod forEachObserverWithInvoke:];
-[LAAuthenticationMethod forEachObserverWithProtocol:selector:invoke:];
```
