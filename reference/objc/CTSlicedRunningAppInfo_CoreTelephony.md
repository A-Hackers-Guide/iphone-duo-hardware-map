# `CTSlicedRunningAppInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleId;
@"NSNumber" _foreground;
@"NSArray" _interfaces;
```

## Properties

```
@property (T@"NSString",&,N,V_bundleId) bundleId;
@property (T@"NSNumber",&,N,V_foreground) foreground;
@property (T@"NSArray",&,N,V_interfaces) interfaces;
```

## Class methods

```
+[CTSlicedRunningAppInfo supportsSecureCoding];
```

## Instance methods

```
-[CTSlicedRunningAppInfo setForeground:];
-[CTSlicedRunningAppInfo foreground];
-[CTSlicedRunningAppInfo setBundleId:];
-[CTSlicedRunningAppInfo interfaces];
-[CTSlicedRunningAppInfo setInterfaces:];
-[CTSlicedRunningAppInfo bundleId];
-[CTSlicedRunningAppInfo encodeWithCoder:];
-[CTSlicedRunningAppInfo description];
-[CTSlicedRunningAppInfo initWithCoder:];
-[CTSlicedRunningAppInfo copyWithZone:];
```
