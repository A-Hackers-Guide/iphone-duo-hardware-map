# `WFLoggerFileWithTTL`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFLoggerBase`
- 13 instance variables, 4 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _ttlInHours;
@"NSNumber" _rotationIntervalInHours;
@"NSString" _logFilePath;
@"NSObject<OS_dispatch_source>" _eventSource;
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq} _filePtr;
@"NSDate" _fileCreationDate;
@"NSURL" _directoryURL;
@"NSString" _fileNamePrefix;
Q _maxFileSizeInBytes;
Q _cleanupAgeInSeconds;
Q _enabledLevel;
^{__CFDateFormatter=} _timestampFormatter;
@"WiFiSoftError" _softError;
```

## Properties

```
@property (T@"NSString",R,GgetLogFilePath) logFilePath;
@property (T@"NSURL",R,GgetLogDirURL) logDirPath;
@property (T@"NSString",R,GgetLogFileNamePrefix) logFileNamePrefix;
@property (T@"WiFiSoftError",R,N,V_softError) softError;
```

## Instance methods

```
-[WFLoggerFileWithTTL dealloc];
-[WFLoggerFileWithTTL cleanupOldFiles];
-[WFLoggerFileWithTTL rotateToNewFile];
-[WFLoggerFileWithTTL WFLog:privacy:cfStrMsg:];
-[WFLoggerFileWithTTL WFLog:privacy:message:valist:];
-[WFLoggerFileWithTTL _stopWatchingLogFileOnQueue];
-[WFLoggerFileWithTTL checkForRotation];
-[WFLoggerFileWithTTL createLogDirectoryIfNeeded];
-[WFLoggerFileWithTTL createNewLogFile];
-[WFLoggerFileWithTTL createPurgeableClassCFile:];
-[WFLoggerFileWithTTL getLogDirURL];
-[WFLoggerFileWithTTL getLogFileNamePrefix];
-[WFLoggerFileWithTTL getLogFilePath];
-[WFLoggerFileWithTTL getLogLevelEnable];
-[WFLoggerFileWithTTL getLogLevelPersist];
-[WFLoggerFileWithTTL getLogLifespanInDays];
-[WFLoggerFileWithTTL getLogPrivacy];
-[WFLoggerFileWithTTL getMaxFileSizeInMB];
-[WFLoggerFileWithTTL initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:dateFormatter:maxFileSizeInMB:ttlInHours:rotationIntervalInHours:dispatchQueue:];
-[WFLoggerFileWithTTL parseTimestampFromFilename:];
-[WFLoggerFileWithTTL setLogLevelEnable:];
-[WFLoggerFileWithTTL setLogLevelPersist:];
-[WFLoggerFileWithTTL setLogLifespanInDays:];
-[WFLoggerFileWithTTL setLogPrivacy:];
-[WFLoggerFileWithTTL setMaxFileSizeInMB:];
-[WFLoggerFileWithTTL shouldRotateFile];
-[WFLoggerFileWithTTL softError];
-[WFLoggerFileWithTTL startWatchingLogFile];
-[WFLoggerFileWithTTL stopWatchingLogFile];
-[WFLoggerFileWithTTL writeToFile:cfStrMsg:];
```
