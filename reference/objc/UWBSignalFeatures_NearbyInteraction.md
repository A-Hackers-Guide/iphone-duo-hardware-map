# `UWBSignalFeatures`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BiasEstimatorFeatures" _inputFeatures;
@"BiasEstimatorOutputs" _outputs;
```

## Properties

```
@property (T@"BiasEstimatorFeatures",C,N,V_inputFeatures) inputFeatures;
@property (T@"BiasEstimatorOutputs",C,N,V_outputs) outputs;
```

## Class methods

```
+[UWBSignalFeatures supportsSecureCoding];
```

## Instance methods

```
-[UWBSignalFeatures outputs];
-[UWBSignalFeatures encodeWithCoder:];
-[UWBSignalFeatures hash];
-[UWBSignalFeatures description];
-[UWBSignalFeatures initWithCoder:];
-[UWBSignalFeatures copyWithZone:];
-[UWBSignalFeatures isEqual:];
-[UWBSignalFeatures inputFeatures];
-[UWBSignalFeatures setOutputs:];
-[UWBSignalFeatures initWithUWBSignalFeatures:];
-[UWBSignalFeatures orderedBiasEstimatorFeatutes];
-[UWBSignalFeatures setInputFeatures:];
```
