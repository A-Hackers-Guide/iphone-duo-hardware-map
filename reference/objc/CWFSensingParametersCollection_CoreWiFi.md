# `CWFSensingParametersCollection`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _forceDualAntenna;
I _csiTimeoutMs;
@"NSArray" _parameters;
```

## Properties

```
@property (T@"NSArray",C,N,V_parameters) parameters;
@property (TI,N,V_csiTimeoutMs) csiTimeoutMs;
@property (TB,N,V_forceDualAntenna) forceDualAntenna;
@property (TQ,R,N) count;
```

## Class methods

```
+[CWFSensingParametersCollection supportsSecureCoding];
```

## Instance methods

```
-[CWFSensingParametersCollection parameters];
-[CWFSensingParametersCollection initWithParameters:];
-[CWFSensingParametersCollection setParameters:];
-[CWFSensingParametersCollection init];
-[CWFSensingParametersCollection count];
-[CWFSensingParametersCollection encodeWithCoder:];
-[CWFSensingParametersCollection hash];
-[CWFSensingParametersCollection description];
-[CWFSensingParametersCollection initWithCoder:];
-[CWFSensingParametersCollection copyWithZone:];
-[CWFSensingParametersCollection isEqual:];
-[CWFSensingParametersCollection convertToDriverStructure:error:];
-[CWFSensingParametersCollection csiTimeoutMs];
-[CWFSensingParametersCollection forceDualAntenna];
-[CWFSensingParametersCollection setCsiTimeoutMs:];
-[CWFSensingParametersCollection setForceDualAntenna:];
```
