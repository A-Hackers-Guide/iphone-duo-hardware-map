# `IOThreadXPCWorkgroupTransporter`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _workgroup;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,V_workgroup) workgroup;
```

## Class methods

```
+[IOThreadXPCWorkgroupTransporter supportsSecureCoding];
+[IOThreadXPCWorkgroupTransporter transporter:];
```

## Instance methods

```
-[IOThreadXPCWorkgroupTransporter dealloc];
-[IOThreadXPCWorkgroupTransporter encodeWithCoder:];
-[IOThreadXPCWorkgroupTransporter initWithCoder:];
-[IOThreadXPCWorkgroupTransporter isEqual:];
-[IOThreadXPCWorkgroupTransporter workgroup];
-[IOThreadXPCWorkgroupTransporter getWorkgroup];
-[IOThreadXPCWorkgroupTransporter initWithWorkgroup:];
-[IOThreadXPCWorkgroupTransporter setWorkgroup:];
```
