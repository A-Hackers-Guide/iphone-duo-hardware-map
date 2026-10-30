# `CTTrafficDescriptorsContainer`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _trafficDescriptors;
@"NSNumber" _sliceABTestSamplePercentage;
@"NSNumber" _slicingAllowedForRelayFaceTimeCall;
```

## Properties

```
@property (T@"NSArray",&,N,V_trafficDescriptors) trafficDescriptors;
@property (T@"NSNumber",&,N,V_sliceABTestSamplePercentage) sliceABTestSamplePercentage;
@property (T@"NSNumber",&,N,V_slicingAllowedForRelayFaceTimeCall) slicingAllowedForRelayFaceTimeCall;
```

## Class methods

```
+[CTTrafficDescriptorsContainer supportsSecureCoding];
```

## Instance methods

```
-[CTTrafficDescriptorsContainer trafficDescriptors];
-[CTTrafficDescriptorsContainer encodeWithCoder:];
-[CTTrafficDescriptorsContainer description];
-[CTTrafficDescriptorsContainer initWithCoder:];
-[CTTrafficDescriptorsContainer setTrafficDescriptors:];
-[CTTrafficDescriptorsContainer copyWithZone:];
-[CTTrafficDescriptorsContainer setSliceABTestSamplePercentage:];
-[CTTrafficDescriptorsContainer setSlicingAllowedForRelayFaceTimeCall:];
-[CTTrafficDescriptorsContainer sliceABTestSamplePercentage];
-[CTTrafficDescriptorsContainer slicingAllowedForRelayFaceTimeCall];
```
