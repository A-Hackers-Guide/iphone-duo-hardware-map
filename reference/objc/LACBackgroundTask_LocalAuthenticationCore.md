# `LACBackgroundTask`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
identifier;
worker;
engine;
```

## Properties

```
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[LACBackgroundTask init];
-[LACBackgroundTask dealloc];
-[LACBackgroundTask description];
-[LACBackgroundTask initWithWorker:];
-[LACBackgroundTask initWithIdentifier:worker:];
-[LACBackgroundTask runSynchronouslyWithTimeout:];
-[LACBackgroundTask runWithTimeout:completion:];
-[LACBackgroundTask runWithTimeout:queue:completion:];
```
