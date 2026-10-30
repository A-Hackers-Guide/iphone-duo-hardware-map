# `BLSHTailspinLogWriter`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSString" _reason;
@? _completion;
```

## Class methods

```
+[BLSHTailspinLogWriter isTailspinAvailable];
```

## Instance methods

```
-[BLSHTailspinLogWriter initWithReason:];
-[BLSHTailspinLogWriter _finish:];
-[BLSHTailspinLogWriter writeTailspinLogWithCompletion:];
-[BLSHTailspinLogWriter _tailspinFilesDirectory];
```
