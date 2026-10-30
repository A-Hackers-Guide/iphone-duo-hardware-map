# `CTSweetgumCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _supportsServices;
B _supportsUsage;
B _supportsPlans;
B _supportsApplications;
```

## Properties

```
@property (TB,N,V_supportsServices) supportsServices;
@property (TB,N,V_supportsUsage) supportsUsage;
@property (TB,N,V_supportsPlans) supportsPlans;
@property (TB,N,V_supportsApplications) supportsApplications;
```

## Class methods

```
+[CTSweetgumCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumCapabilities encodeWithCoder:];
-[CTSweetgumCapabilities description];
-[CTSweetgumCapabilities initWithCoder:];
-[CTSweetgumCapabilities copyWithZone:];
-[CTSweetgumCapabilities isEqual:];
-[CTSweetgumCapabilities setSupportsApplications:];
-[CTSweetgumCapabilities setSupportsPlans:];
-[CTSweetgumCapabilities setSupportsServices:];
-[CTSweetgumCapabilities setSupportsUsage:];
-[CTSweetgumCapabilities supportsApplications];
-[CTSweetgumCapabilities supportsPlans];
-[CTSweetgumCapabilities supportsServices];
-[CTSweetgumCapabilities supportsUsage];
```
