# `WFLoggerCircularBuffer`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFLoggerBase`
- 6 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
* _wiFiLoggingLogBufferRef;
q _wiFiLoggingLogBufferIndex;
q _wiFiLoggingLogBufferMaxSize;
I _dumpId;
@"NSDateFormatter" _tsFormatter;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Instance methods

```
-[WFLoggerCircularBuffer dump];
-[WFLoggerCircularBuffer init];
-[WFLoggerCircularBuffer dealloc];
-[WFLoggerCircularBuffer WFLog:privacy:cfStrMsg:];
-[WFLoggerCircularBuffer WFLog:privacy:message:valist:];
```
