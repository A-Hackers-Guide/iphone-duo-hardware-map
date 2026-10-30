# `CAFSessionAnalytics`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _supportsBluetoothLE;
@"NSString" _name;
@"NSString" _ppid;
@"NSString" _firmwareVersion;
@"NSString" _hardwareVersion;
@"NSString" _manufacturer;
@"NSString" _model;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_ppid) ppid;
@property (T@"NSString",R,N,V_firmwareVersion) firmwareVersion;
@property (T@"NSString",R,N,V_hardwareVersion) hardwareVersion;
@property (T@"NSString",R,N,V_manufacturer) manufacturer;
@property (T@"NSString",R,N,V_model) model;
@property (TB,R,N,V_supportsBluetoothLE) supportsBluetoothLE;
```

## Class methods

```
+[CAFSessionAnalytics supportsSecureCoding];
```

## Instance methods

```
-[CAFSessionAnalytics hardwareVersion];
-[CAFSessionAnalytics model];
-[CAFSessionAnalytics firmwareVersion];
-[CAFSessionAnalytics manufacturer];
-[CAFSessionAnalytics ppid];
-[CAFSessionAnalytics encodeWithCoder:];
-[CAFSessionAnalytics initWithCoder:];
-[CAFSessionAnalytics initWithSession:];
-[CAFSessionAnalytics name];
-[CAFSessionAnalytics supportsBluetoothLE];
```
