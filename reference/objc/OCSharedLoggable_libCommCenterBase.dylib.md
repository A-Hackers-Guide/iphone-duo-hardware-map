# `OCSharedLoggable`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`](../userland/System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterBase.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _queue;
{OsLogContext="domain"*"handle"{OSSharedRef<os_log_s>="fRef"^{os_log_s}}} _logContext;
```

## Properties

```
@property (T{queue={object=^{dispatch_object_s}}},N,GgetQueue,V_queue) queue;
@property (T{OsLogContext=*{OSSharedRef<os_log_s>=^{os_log_s}}},N,GgetLogContext,V_logContext) logContext;
```

## Instance methods

```
-[OCSharedLoggable getQueue];
-[OCSharedLoggable setLogContext:];
-[OCSharedLoggable setQueue:];
-[OCSharedLoggable executeBlock:];
-[OCSharedLoggable executeFunction:];
-[OCSharedLoggable getLogContext];
-[OCSharedLoggable initWithName:qosClass:logContext:];
-[OCSharedLoggable initWithQueue:logContext:];
```
