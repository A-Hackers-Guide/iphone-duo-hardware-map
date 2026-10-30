# `CTNetworkList`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _moreComing;
@"NSMutableArray" _networks;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_networks) networks;
@property (TB,N,V_moreComing) moreComing;
```

## Class methods

```
+[CTNetworkList supportsSecureCoding];
```

## Instance methods

```
-[CTNetworkList setNetworks:];
-[CTNetworkList networks];
-[CTNetworkList encodeWithCoder:];
-[CTNetworkList description];
-[CTNetworkList initWithCoder:];
-[CTNetworkList copyWithZone:];
-[CTNetworkList moreComing];
-[CTNetworkList setMoreComing:];
```
