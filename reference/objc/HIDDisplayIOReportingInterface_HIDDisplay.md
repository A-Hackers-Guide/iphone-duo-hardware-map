# `HIDDisplayIOReportingInterface`

- Image: [`/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`](../userland/System__Library__PrivateFrameworks__HIDDisplay.framework__HIDDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `HIDDisplayInterface`
- 3 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _usageElementMap;
@? _dataHandler;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[HIDDisplayIOReportingInterface initWithContainerID:];
-[HIDDisplayIOReportingInterface setDispatchQueue:];
-[HIDDisplayIOReportingInterface setCancelHandler:];
-[HIDDisplayIOReportingInterface activate];
-[HIDDisplayIOReportingInterface cancel];
-[HIDDisplayIOReportingInterface initWithService:];
-[HIDDisplayIOReportingInterface getHIDDevices];
-[HIDDisplayIOReportingInterface setInputDataHandler:];
-[HIDDisplayIOReportingInterface setOutputData:error:];
-[HIDDisplayIOReportingInterface setupIOReporting];
```
