# `SRTextInputSession`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`
- 3 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
d _duration;
q _sessionType;
@"NSString" _sessionIdentifier;
```

## Properties

```
@property (Td,V_duration) duration;
@property (Tq,V_sessionType) sessionType;
@property (T@"NSString",C,N,V_sessionIdentifier) sessionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRTextInputSession supportsSecureCoding];
+[SRTextInputSession textInputSessionWithDuration:sessionType:sessionIdentifier:];
```

## Instance methods

```
-[SRTextInputSession sessionIdentifier];
-[SRTextInputSession dealloc];
-[SRTextInputSession setSessionIdentifier:];
-[SRTextInputSession duration];
-[SRTextInputSession sessionType];
-[SRTextInputSession encodeWithCoder:];
-[SRTextInputSession description];
-[SRTextInputSession initWithCoder:];
-[SRTextInputSession setDuration:];
-[SRTextInputSession isEqual:];
-[SRTextInputSession setSessionType:];
-[SRTextInputSession sr_dictionaryRepresentation];
```
