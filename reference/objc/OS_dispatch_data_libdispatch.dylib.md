# `OS_dispatch_data`

- Image: [`/usr/lib/system/libdispatch.dylib`](../userland/usr__lib__system__libdispatch.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_dispatch_data`
- 0 instance variables, 6 properties, 15 instance methods, 1 class methods

## Properties

```
@property (TQ,R,N) length;
@property (Tr^v,R,N) bytes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[OS_dispatch_data allocWithZone:];
```

## Instance methods

```
-[OS_dispatch_data _suspend];
-[OS_dispatch_data _activate];
-[OS_dispatch_data _isCompact];
-[OS_dispatch_data debugDescription];
-[OS_dispatch_data init];
-[OS_dispatch_data dealloc];
-[OS_dispatch_data _getContext];
-[OS_dispatch_data _setTargetQueue:];
-[OS_dispatch_data length];
-[OS_dispatch_data initWithBytes:length:copy:freeWhenDone:bytesAreVM:];
-[OS_dispatch_data _setFinalizer:];
-[OS_dispatch_data _resume];
-[OS_dispatch_data bytes];
-[OS_dispatch_data _setContext:];
-[OS_dispatch_data _bytesAreVM];
```
