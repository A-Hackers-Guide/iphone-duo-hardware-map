# `W5DiagnosticsTestRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _uuid;
q _testID;
@"NSDictionary" _configuration;
```

## Properties

```
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_testID) testID;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
```

## Class methods

```
+[W5DiagnosticsTestRequest supportsSecureCoding];
+[W5DiagnosticsTestRequest requestWithTestID:configuration:];
```

## Instance methods

```
-[W5DiagnosticsTestRequest uuid];
-[W5DiagnosticsTestRequest init];
-[W5DiagnosticsTestRequest dealloc];
-[W5DiagnosticsTestRequest setUuid:];
-[W5DiagnosticsTestRequest setConfiguration:];
-[W5DiagnosticsTestRequest configuration];
-[W5DiagnosticsTestRequest encodeWithCoder:];
-[W5DiagnosticsTestRequest conformsToProtocol:];
-[W5DiagnosticsTestRequest hash];
-[W5DiagnosticsTestRequest description];
-[W5DiagnosticsTestRequest initWithCoder:];
-[W5DiagnosticsTestRequest copyWithZone:];
-[W5DiagnosticsTestRequest isEqual:];
-[W5DiagnosticsTestRequest setTestID:];
-[W5DiagnosticsTestRequest testID];
-[W5DiagnosticsTestRequest isEqualToDiagnosticsTestRequest:];
```
