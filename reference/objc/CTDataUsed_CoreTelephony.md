# `CTDataUsed`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"CTDataUsage" _native;
@"CTDataUsage" _proxied;
```

## Properties

```
@property (T@"CTDataUsage",R,N,V_native) native;
@property (T@"CTDataUsage",R,N,V_proxied) proxied;
```

## Class methods

```
+[CTDataUsed supportsSecureCoding];
```

## Instance methods

```
-[CTDataUsed addNativeUsage:];
-[CTDataUsed native];
-[CTDataUsed encodeWithCoder:];
-[CTDataUsed description];
-[CTDataUsed initWithCoder:];
-[CTDataUsed addUsage:];
-[CTDataUsed copyWithZone:];
-[CTDataUsed isEqual:];
-[CTDataUsed proxied];
-[CTDataUsed initWithUsage:proxied:];
-[CTDataUsed addProxiedUsage:];
```
