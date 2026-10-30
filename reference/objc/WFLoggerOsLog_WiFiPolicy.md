# `WFLoggerOsLog`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFLoggerBase`
- 6 instance variables, 1 properties, 31 instance methods, 2 class methods

## Instance variables

```
^{__CFString=} _subSystem;
^{__CFString=} _category;
@"NSObject<OS_os_log>" _osLog;
@"NSMutableDictionary" _profileSettings;
Q _currentLevel;
Q _logLifeSpanInDays;
```

## Properties

```
@property (T@"NSString",R,C,GgetProfileFilePath) profileFilePath;
```

## Class methods

```
+[WFLoggerOsLog WFLogOsLog:cfStrMsg:];
+[WFLoggerOsLog convertWFLogLevelToOsLogLevel:];
```

## Instance methods

```
-[WFLoggerOsLog dealloc];
-[WFLoggerOsLog mapLogLevelStr:];
-[WFLoggerOsLog setLevelPersist:category:value:];
-[WFLoggerOsLog setMaxSizeInKb:];
-[WFLoggerOsLog setLevelEnabled:category:value:];
-[WFLoggerOsLog WFLog:privacy:cfStrMsg:];
-[WFLoggerOsLog WFLog:privacy:message:valist:];
-[WFLoggerOsLog convertLogLevel:];
-[WFLoggerOsLog createOsLogProfile];
-[WFLoggerOsLog doesProfileExist:];
-[WFLoggerOsLog formatOsLogProfile:levelEnabled:levelPersist:ttlDays:privacy:];
-[WFLoggerOsLog getLevelEnabled:category:];
-[WFLoggerOsLog getLevelPersist:category:];
-[WFLoggerOsLog getLogLevelEnable];
-[WFLoggerOsLog getLogLevelPersist];
-[WFLoggerOsLog getLogLifespanInDays];
-[WFLoggerOsLog getLogPrivacy];
-[WFLoggerOsLog getMaxFileSizeInMB];
-[WFLoggerOsLog getPrivacy:category:];
-[WFLoggerOsLog getProfileFilePath];
-[WFLoggerOsLog getTtlDays:category:];
-[WFLoggerOsLog init:subSystem:category:logLifespanInDays:logLevel:logPrivacy:dispatchQueue:];
-[WFLoggerOsLog mapLogLevelEnum:];
-[WFLoggerOsLog setLogLevelEnable:];
-[WFLoggerOsLog setLogLevelPersist:];
-[WFLoggerOsLog setLogLifespanInDays:];
-[WFLoggerOsLog setLogPrivacy:];
-[WFLoggerOsLog setPrivacy:category:value:];
-[WFLoggerOsLog setTtlDays:category:value:];
-[WFLoggerOsLog stopWatchingLogFile];
-[WFLoggerOsLog writeDictToFile:idStr:];
```
