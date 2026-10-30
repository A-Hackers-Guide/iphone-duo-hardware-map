# `PLThreadInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isNamed;
d _systemTime;
d _userTime;
Q _threadID;
@"NSString" _threadName;
```

## Properties

```
@property (Td,V_systemTime) systemTime;
@property (Td,V_userTime) userTime;
@property (TQ,V_threadID) threadID;
@property (T@"NSString",&,V_threadName) threadName;
@property (TB,V_isNamed) isNamed;
```

## Instance methods

```
-[PLThreadInfo threadID];
-[PLThreadInfo setThreadID:];
-[PLThreadInfo description];
-[PLThreadInfo isNamed];
-[PLThreadInfo threadName];
-[PLThreadInfo diffSinceBaseline:];
-[PLThreadInfo initWithThread:inProcess:];
-[PLThreadInfo isEqualToThreadInfo:];
-[PLThreadInfo setIsNamed:];
-[PLThreadInfo setSystemTime:];
-[PLThreadInfo setThreadName:];
-[PLThreadInfo setUserTime:];
-[PLThreadInfo systemTime];
-[PLThreadInfo userTime];
```
