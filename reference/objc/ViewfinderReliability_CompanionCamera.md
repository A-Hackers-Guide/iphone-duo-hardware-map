# `ViewfinderReliability`

- Image: [`/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`](../userland/System__Library__PrivateFrameworks__CompanionCamera.framework__CompanionCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _log;
@"NSCountedSet" _events;
@"NSObject<OS_dispatch_source>" _resetSource;
@"NSObject<OS_dispatch_source>" _printSource;
```

## Class methods

```
+[ViewfinderReliability sharedInstance];
```

## Instance methods

```
-[ViewfinderReliability _reset];
-[ViewfinderReliability init];
-[ViewfinderReliability logEvent:];
-[ViewfinderReliability _checkForUnexpectedEvent:];
-[ViewfinderReliability _checkForRepeatedEvent:];
-[ViewfinderReliability _print];
-[ViewfinderReliability _registerSources];
```
