# `WFLoggerFile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFLoggerBase`
- 20 instance variables, 3 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _loggingTimer;
C _loggingTimerStarted;
^{__CFRunLoop=} _runLoopRef;
^{__CFString=} _runLoopMode;
C _classC;
@"NSNumber" _logLifespanInDays;
Q _privacy;
Q _level;
^{__CFString=} _logFilePath;
@"NSObject<OS_dispatch_source>" _eventSource;
C _isFileLoggingEnabled;
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq} _filePtr;
^{__CFDate=} _fileCreationDate;
^{__CFDateFormatter=} _dateFormatter;
^{__CFString=} _presetFilePath;
^{__CFString=} _directoryPath;
^{__CFString=} _fileNamePrefix;
Q _maxFileSizeInBytes;
Q _timerInterval;
Q _fileAgeOutInterval;
```

## Properties

```
@property (T^{__CFString=},R,GgetLogFilePath) logFilePath;
@property (T^{__CFString=},R,GgetLogDirPath) logDirPath;
@property (T^{__CFString=},R,GgetLogFileNamePrefix) logFileNamePrefix;
```

## Instance methods

```
-[WFLoggerFile dealloc];
-[WFLoggerFile schedule:];
-[WFLoggerFile WFLog:privacy:cfStrMsg:];
-[WFLoggerFile WFLog:privacy:message:valist:];
-[WFLoggerFile changeLogFile:];
-[WFLoggerFile checkLogFileUpdate:];
-[WFLoggerFile cleanStaleLogs];
-[WFLoggerFile createDateString];
-[WFLoggerFile createLogFile:fileClassC:];
-[WFLoggerFile doesLogFileExist:];
-[WFLoggerFile generateLogFileName];
-[WFLoggerFile getLogDirPath];
-[WFLoggerFile getLogFileNamePrefix];
-[WFLoggerFile getLogFilePath];
-[WFLoggerFile getLogLevelEnable];
-[WFLoggerFile getLogLevelPersist];
-[WFLoggerFile getLogLifespanInDays];
-[WFLoggerFile getLogPrivacy];
-[WFLoggerFile getMaxFileSizeInMB];
-[WFLoggerFile init:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:];
-[WFLoggerFile initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:dispatchQueue:];
-[WFLoggerFile initWithFilePath:filePath:runLoopRef:runLoopMode:classC:dateFormatter:maxFileSizeInMB:logLifespanInDays:dispatchQueue:];
-[WFLoggerFile mapLogLevelEnum:];
-[WFLoggerFile removeLogFile:maxAge:];
-[WFLoggerFile removeLogFilesFromDir:];
-[WFLoggerFile rotateLogFile:];
-[WFLoggerFile setLogLevelEnable:];
-[WFLoggerFile setLogLevelPersist:];
-[WFLoggerFile setLogLifespanInDays:];
-[WFLoggerFile setLogPrivacy:];
-[WFLoggerFile setMaxFileSizeInMB:];
-[WFLoggerFile startWatchingLogFile];
-[WFLoggerFile stopWatchingLogFile];
-[WFLoggerFile writeToFile:cfStrMsg:];
```
