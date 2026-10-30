# `LACBATS`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 2 class methods

## Instance variables

```
B _wasLaunchedByBATS;
B _isRunningInBATS;
```

## Properties

```
@property (TB,R,N,V_wasLaunchedByBATS) wasLaunchedByBATS;
@property (TB,R,N,V_isRunningInBATS) isRunningInBATS;
```

## Class methods

```
+[LACBATS sharedInstance];
+[LACBATS _isBATSEnvironmentSet];
```

## Instance methods

```
-[LACBATS init];
-[LACBATS isRunningInBATS];
-[LACBATS wasLaunchedByBATS];
```
