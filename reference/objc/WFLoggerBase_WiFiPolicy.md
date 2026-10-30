# `WFLoggerBase`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFLogProtocol`
- 3 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"WFLogger" _ctxt;
C _internalInstall;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (TC,R) WFIsInternalInstall;
@property (T@"NSNumber",C,GgetLogLifespanInDays) logLifespanInDays;
@property (TQ,GgetLogPrivacy) logPrivacy;
@property (TQ,GgetLogLevelEnable) logLevelEnable;
@property (TQ,GgetLogLevelPersist) logLevelPersist;
@property (TQ,GgetMaxFileSizeInMB) maxSizeInKb;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFLoggerBase dump];
-[WFLoggerBase setMaxSizeInKb:];
-[WFLoggerBase WFIsInternalInstall];
-[WFLoggerBase WFLog:privacy:cfStrMsg:];
-[WFLoggerBase WFLog:privacy:message:valist:];
-[WFLoggerBase getLogLevelEnable];
-[WFLoggerBase getLogLevelPersist];
-[WFLoggerBase getLogLifespanInDays];
-[WFLoggerBase getLogPrivacy];
-[WFLoggerBase getMaxFileSizeInMB];
-[WFLoggerBase setLogLevelEnable:];
-[WFLoggerBase setLogLevelPersist:];
-[WFLoggerBase setLogLifespanInDays:];
-[WFLoggerBase setLogPrivacy:];
-[WFLoggerBase stopWatchingLogFile];
```
