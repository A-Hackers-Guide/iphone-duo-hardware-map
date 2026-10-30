# `AVResult`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _ivarAccessLock;
q _status;
@"NSError" _error;
```

## Properties

```
@property (TB,R,GisFailed) failed;
```

## Instance methods

```
-[AVResult isFailed];
-[AVResult init];
-[AVResult dealloc];
-[AVResult markAsCompleted];
-[AVResult getStatus:error:];
-[AVResult markAsFailedWithError:];
```
