# `WFLogger`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"WFLoggerBase" _loggerBase;
Q _destination;
Q _privacy;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
C _wflRunningOnWatchClassDevice;
C _wflEnableDualLoggingOnWatchClassDevice;
```

## Properties

```
@property (T@"NSNumber",R,C,GgetLogLifespanInDays) logLifespanInDays;
@property (TQ,R,GgetLogLevelEnable) logLevelEnable;
@property (TQ,R,GgetLogLevelPersist) logLevelPersist;
@property (TQ,R,GgetDestination) destination;
@property (TQ,R,GgetLogPrivacy) logPrivacy;
@property (TQ,R,GgetMaxFileSizeInMB) maxFileSizeInMB;
```

## Class methods

```
+[WFLogger sharedWFLoggerSingleton];
```

## Instance methods

```
-[WFLogger dump];
-[WFLogger init];
-[WFLogger WFLog:message:];
-[WFLogger getDestination];
-[WFLogger getLogLevelEnable];
-[WFLogger getLogLevelPersist];
-[WFLogger getLogLifespanInDays];
-[WFLogger getLogPrivacy];
-[WFLogger getMaxFileSizeInMB];
-[WFLogger loggerBase];
-[WFLogger setDestinationCircularBuffer];
-[WFLogger setDestinationFile:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:];
-[WFLogger setDestinationFileLocation:fileNamePrefix:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:];
-[WFLogger setDestinationOsLog:category:logLifespanInDays:logLevel:logPrivacy:];
```
