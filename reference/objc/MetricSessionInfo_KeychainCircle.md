# `MetricSessionInfo`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
```

## Properties

```
@property (T@"NSString",R,V_altDSID) altDSID;
@property (T@"NSString",R,V_flowID) flowID;
@property (T@"NSString",R,V_deviceSessionID) deviceSessionID;
```

## Class methods

```
+[MetricSessionInfo sessionInfoWithAltDSID:flowID:deviceSessionID:];
+[MetricSessionInfo sessionInfoWithAltDSID:];
```

## Instance methods

```
-[MetricSessionInfo initWithAltDSID:];
-[MetricSessionInfo altDSID];
-[MetricSessionInfo flowID];
-[MetricSessionInfo initWithAltDSID:flowID:deviceSessionID:];
-[MetricSessionInfo deviceSessionID];
```
