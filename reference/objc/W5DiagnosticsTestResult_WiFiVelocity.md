# `W5DiagnosticsTestResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _result;
B _didPass;
@"NSUUID" _uuid;
q _testID;
@"NSDictionary" _configuration;
@"NSDictionary" _info;
@"NSError" _error;
d _testStarted;
d _testCompleted;
```

## Properties

```
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_testID) testID;
@property (TB,N,V_result) result;
@property (TB,N,V_didPass) didPass;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
@property (T@"NSDictionary",C,N,V_info) info;
@property (T@"NSError",C,N,V_error) error;
@property (Td,N,V_testStarted) testStarted;
@property (Td,N,V_testCompleted) testCompleted;
```

## Class methods

```
+[W5DiagnosticsTestResult supportsSecureCoding];
```

## Instance methods

```
-[W5DiagnosticsTestResult setError:];
-[W5DiagnosticsTestResult setResult:];
-[W5DiagnosticsTestResult info];
-[W5DiagnosticsTestResult uuid];
-[W5DiagnosticsTestResult setInfo:];
-[W5DiagnosticsTestResult dealloc];
-[W5DiagnosticsTestResult setUuid:];
-[W5DiagnosticsTestResult setConfiguration:];
-[W5DiagnosticsTestResult error];
-[W5DiagnosticsTestResult configuration];
-[W5DiagnosticsTestResult result];
-[W5DiagnosticsTestResult encodeWithCoder:];
-[W5DiagnosticsTestResult conformsToProtocol:];
-[W5DiagnosticsTestResult hash];
-[W5DiagnosticsTestResult description];
-[W5DiagnosticsTestResult initWithCoder:];
-[W5DiagnosticsTestResult copyWithZone:];
-[W5DiagnosticsTestResult isEqual:];
-[W5DiagnosticsTestResult setTestID:];
-[W5DiagnosticsTestResult testID];
-[W5DiagnosticsTestResult didPass];
-[W5DiagnosticsTestResult isEqualToDiagnosticsTestResult:];
-[W5DiagnosticsTestResult setTestStarted:];
-[W5DiagnosticsTestResult setDidPass:];
-[W5DiagnosticsTestResult setTestCompleted:];
-[W5DiagnosticsTestResult testCompleted];
-[W5DiagnosticsTestResult testStarted];
```
