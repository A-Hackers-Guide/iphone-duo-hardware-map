# `CLFindMyAccessoryFindingCapabilities`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _supportsFC1ND;
B _supportsNBAMMS;
B _supportsUnii5;
B _supportsSimultaneousRanging;
B _supports32plusFragmentMixedMMS;
C _supportedNBConfigVersion;
I _capabilities;
```

## Properties

```
@property (TI,V_capabilities) capabilities;
@property (TB,N,V_supportsFC1ND) supportsFC1ND;
@property (TB,N,V_supportsNBAMMS) supportsNBAMMS;
@property (TB,N,V_supportsSimultaneousRanging) supportsSimultaneousRanging;
@property (TB,R,V_supportsUnii5) supportsUnii5;
@property (TB,R,V_supports32plusFragmentMixedMMS) supports32plusFragmentMixedMMS;
@property (TC,R,V_supportedNBConfigVersion) supportedNBConfigVersion;
```

## Class methods

```
+[CLFindMyAccessoryFindingCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CLFindMyAccessoryFindingCapabilities init];
-[CLFindMyAccessoryFindingCapabilities dealloc];
-[CLFindMyAccessoryFindingCapabilities encodeWithCoder:];
-[CLFindMyAccessoryFindingCapabilities capabilities];
-[CLFindMyAccessoryFindingCapabilities initWithCoder:];
-[CLFindMyAccessoryFindingCapabilities supportsNBAMMS];
-[CLFindMyAccessoryFindingCapabilities initWithData:];
-[CLFindMyAccessoryFindingCapabilities copyWithZone:];
-[CLFindMyAccessoryFindingCapabilities setCapabilities:];
-[CLFindMyAccessoryFindingCapabilities setSupportsSimultaneousRanging:];
-[CLFindMyAccessoryFindingCapabilities capabilitiesString];
-[CLFindMyAccessoryFindingCapabilities initWithSupportsFC1ND:supportsNBAMMS:supportsUnii5:capabilities:supportsSimultaneousRanging:supports32plusFragmentMixedMMS:supportedNBConfigVersion:];
-[CLFindMyAccessoryFindingCapabilities setSupportsFC1ND:];
-[CLFindMyAccessoryFindingCapabilities setSupportsNBAMMS:];
-[CLFindMyAccessoryFindingCapabilities supportedNBConfigVersion];
-[CLFindMyAccessoryFindingCapabilities supports32plusFragmentMixedMMS];
-[CLFindMyAccessoryFindingCapabilities supportsFC1ND];
-[CLFindMyAccessoryFindingCapabilities supportsSimultaneousRanging];
-[CLFindMyAccessoryFindingCapabilities supportsUnii5];
```
