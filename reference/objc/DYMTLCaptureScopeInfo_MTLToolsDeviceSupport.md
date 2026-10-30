# `DYMTLCaptureScopeInfo`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DYCapturableObject`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 12 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _isDefaultCapturable;
@"NSString" _displayName;
Q _deviceAddress;
Q _scopeAddress;
Q _scopeStreamRef;
@"NSString" _label;
```

## Properties

```
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_scopeAddress) scopeAddress;
@property (TQ,R,N,V_scopeStreamRef) scopeStreamRef;
@property (T@"NSString",R,C,N,V_label) label;
@property (TB,R,N,V_isDefaultCapturable) isDefaultCapturable;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R,N) streamRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DYMTLCaptureScopeInfo supportsSecureCoding];
+[DYMTLCaptureScopeInfo capturableObjectType];
```

## Instance methods

```
-[DYMTLCaptureScopeInfo label];
-[DYMTLCaptureScopeInfo displayName];
-[DYMTLCaptureScopeInfo encodeWithCoder:];
-[DYMTLCaptureScopeInfo description];
-[DYMTLCaptureScopeInfo initWithCoder:];
-[DYMTLCaptureScopeInfo copyWithZone:];
-[DYMTLCaptureScopeInfo isEqual:];
-[DYMTLCaptureScopeInfo deviceAddress];
-[DYMTLCaptureScopeInfo streamRef];
-[DYMTLCaptureScopeInfo isDefaultCapturable];
-[DYMTLCaptureScopeInfo scopeAddress];
-[DYMTLCaptureScopeInfo scopeStreamRef];
-[DYMTLCaptureScopeInfo capturableObjectType];
-[DYMTLCaptureScopeInfo initWithCaptureScope:];
```
