# `AHTInterface`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`](../userland/System__Library__PrivateFrameworks__AppleHIDTransportSupport.framework__AppleHIDTransportSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AHTCommon`
- 1 instance variables, 1 properties, 10 instance methods, 3 class methods

## Instance variables

```
C _interfaceID;
```

## Properties

```
@property (TC,R,N,V_interfaceID) interfaceID;
```

## Class methods

```
+[AHTInterface allInterfaces];
+[AHTInterface withService:];
+[AHTInterface withName:];
```

## Instance methods

```
-[AHTInterface reset];
-[AHTInterface description];
-[AHTInterface initWithService:];
-[AHTInterface setEnable:];
-[AHTInterface setPower:];
-[AHTInterface interfaceID];
-[AHTInterface captureMemoryDump];
-[AHTInterface getPower:];
-[AHTInterface getReport:withData:];
-[AHTInterface setReport:withData:];
```
