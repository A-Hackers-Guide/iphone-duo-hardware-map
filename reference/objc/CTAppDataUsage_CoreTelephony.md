# `CTAppDataUsage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleId;
@"NSString" _displayName;
@"CTDataUsed" _used;
```

## Properties

```
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (T@"CTDataUsed",R,N,V_used) used;
```

## Class methods

```
+[CTAppDataUsage supportsSecureCoding];
```

## Instance methods

```
-[CTAppDataUsage usage];
-[CTAppDataUsage displayName];
-[CTAppDataUsage bundleId];
-[CTAppDataUsage used];
-[CTAppDataUsage encodeWithCoder:];
-[CTAppDataUsage initWithCoder:];
-[CTAppDataUsage copyWithZone:];
-[CTAppDataUsage init:withDisplayName:andUsage:];
```
