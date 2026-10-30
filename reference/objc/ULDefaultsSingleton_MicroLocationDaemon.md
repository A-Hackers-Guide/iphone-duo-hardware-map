# `ULDefaultsSingleton`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _defaultsDictionary;
@"NSUserDefaults" _defaults;
```

## Properties

```
@property (T@"NSUserDefaults",&,N,V_defaults) defaults;
@property (T@"NSDictionary",&,N,V_defaultsDictionary) defaultsDictionary;
```

## Class methods

```
+[ULDefaultsSingleton shared];
```

## Instance methods

```
-[ULDefaultsSingleton setDefaults:];
-[ULDefaultsSingleton defaults];
-[ULDefaultsSingleton init];
-[ULDefaultsSingleton refresh];
-[ULDefaultsSingleton _defaultsSync];
-[ULDefaultsSingleton defaultsDictionary];
-[ULDefaultsSingleton resetTemporaryKey:];
-[ULDefaultsSingleton setDefaultsDictionary:];
-[ULDefaultsSingleton settingsString];
-[ULDefaultsSingleton updateTemporaryKey:withObject:];
```
