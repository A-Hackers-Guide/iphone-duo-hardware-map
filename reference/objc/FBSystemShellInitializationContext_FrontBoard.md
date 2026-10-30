# `FBSystemShellInitializationContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"FBSystemShellInitializationOptions" _options;
B _bootedDark;
```

## Properties

```
@property (T@"FBSystemShellInitializationOptions",R,N,V_options) options;
@property (TQ,R,N) lastExitReason;
@property (TB,R,N,GwasBootedDark) bootedDark;
```

## Instance methods

```
-[FBSystemShellInitializationContext _initWithOptions:];
-[FBSystemShellInitializationContext options];
-[FBSystemShellInitializationContext copyWithZone:];
-[FBSystemShellInitializationContext lastExitReason];
-[FBSystemShellInitializationContext wasBootedDark];
```
