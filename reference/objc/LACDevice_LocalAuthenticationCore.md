# `LACDevice`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 3 properties, 4 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) isClarityBoardRunning;
@property (TB,R,N) isDynamicIslandAvailable;
@property (TB,R,N) usesFrontBoardServicesForRemoteUI;
```

## Class methods

```
+[LACDevice sharedInstance];
```

## Instance methods

```
-[LACDevice callerRunningOnForeground:pid:];
-[LACDevice isClarityBoardRunning];
-[LACDevice isDynamicIslandAvailable];
-[LACDevice usesFrontBoardServicesForRemoteUI];
```
