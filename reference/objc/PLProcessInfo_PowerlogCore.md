# `PLProcessInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
i _pid;
d _totalSystemTime;
d _totalUserTime;
@"NSString" _processName;
@"NSDictionary" _threadNameToInfo;
```

## Properties

```
@property (Td,V_totalSystemTime) totalSystemTime;
@property (Td,V_totalUserTime) totalUserTime;
@property (Ti,V_pid) pid;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSDictionary",&,V_threadNameToInfo) threadNameToInfo;
```

## Instance methods

```
-[PLProcessInfo setProcessName:];
-[PLProcessInfo setPid:];
-[PLProcessInfo pid];
-[PLProcessInfo initWithProcessInfo:];
-[PLProcessInfo processName];
-[PLProcessInfo description];
-[PLProcessInfo totalSystemTime];
-[PLProcessInfo populateCPUTime];
-[PLProcessInfo diffSinceBaseline:];
-[PLProcessInfo initWithName:andID:];
-[PLProcessInfo isEqualToProcessInfo:];
-[PLProcessInfo setThreadNameToInfo:];
-[PLProcessInfo setTotalSystemTime:];
-[PLProcessInfo setTotalUserTime:];
-[PLProcessInfo threadNameToInfo];
-[PLProcessInfo totalUserTime];
```
