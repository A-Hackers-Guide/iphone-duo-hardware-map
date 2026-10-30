# `VMDisplayModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBDisplayModule`
- 6 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"<VMHeadroomRequestDelegate>" _headroomRequestDelegate;
@"<CBBrightnessProxy>" _brightnessControlProxy;
@"NSString" _uuid;
B _builtIn;
@"NSObject<OS_xpc_object>" _lastBrightnessTransaction;
```

## Properties

```
@property (T@"NSString",R,V_uuid) uuid;
@property (TB,R,V_builtIn) builtIn;
```

## Instance methods

```
-[VMDisplayModule setProperty:forKey:];
-[VMDisplayModule uuid];
-[VMDisplayModule dealloc];
-[VMDisplayModule invalidate];
-[VMDisplayModule builtIn];
-[VMDisplayModule initWithBrightnessControl:displayUUID:builtIn:delegate:andQueue:];
-[VMDisplayModule setBrightnessProperty:forKey:];
-[VMDisplayModule setPropertyOnQueue:forKey:];
```
