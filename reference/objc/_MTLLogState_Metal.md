# `_MTLLogState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLLogState`
- 14 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _logLevel;
q _logBufferSize;
@"<MTLBuffer>" _logBuffer;
@"<MTLResidencySet>" _logBufferResidencySet;
@"<MTLDevice>" _device;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _logHandlerLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _logBufferLock;
B _usedForShaderValidation;
@"NSMutableArray" _handlers;
@"NSMutableDictionary" defaultLoggerCache;
@"NSString" metalSubsystem;
@"NSString" shaderLoggingCategory;
@"NSString" metalLoggingKey;
I droppedMessages;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_MTLLogState convertToLogLevel:];
```

## Instance methods

```
-[_MTLLogState dealloc];
-[_MTLLogState initWithDevice:descriptor:error:];
-[_MTLLogState addLogHandler:];
-[_MTLLogState checkAndGetMessage:logBuffer:message:];
-[_MTLLogState decodeLog];
-[_MTLLogState defaultLogHandler:category:level:message:];
-[_MTLLogState defaultOSLogger:level:message:];
-[_MTLLogState invokeLogHandlers:category:level:message:];
-[_MTLLogState populateDefaultLoggerCache:logger:];
-[_MTLLogState populateDefaultLoggerCache:subsystem:category:];
-[_MTLLogState setUsedForShaderValidation:];
```
