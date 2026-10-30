# `WFLogProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSNumber",C,GgetLogLifespanInDays) logLifespanInDays;
@property (TQ,GgetLogPrivacy) logPrivacy;
@property (TQ,GgetLogLevelEnable) logLevelEnable;
@property (TQ,GgetLogLevelPersist) logLevelPersist;
@property (TQ,GgetMaxFileSizeInMB) maxSizeInKb;
```

## Instance methods

```
-[WFLogProtocol dump];
-[WFLogProtocol setMaxSizeInKb:];
-[WFLogProtocol WFLog:privacy:cfStrMsg:];
-[WFLogProtocol WFLog:privacy:message:valist:];
-[WFLogProtocol getLogLevelEnable];
-[WFLogProtocol getLogLevelPersist];
-[WFLogProtocol getLogLifespanInDays];
-[WFLogProtocol getLogPrivacy];
-[WFLogProtocol getMaxFileSizeInMB];
-[WFLogProtocol setLogLevelEnable:];
-[WFLogProtocol setLogLevelPersist:];
-[WFLogProtocol setLogLifespanInDays:];
-[WFLogProtocol setLogPrivacy:];
```
