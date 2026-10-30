# `MLInternalSettings`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 4 class methods

## Instance variables

```
B _restrictNeuralNetworksToUseCPUOnly;
B _restrictNeuralNetworksFromUsingANE;
B _isNeuralNetworkGPUPathForbidden;
```

## Properties

```
@property (TB,V_restrictNeuralNetworksToUseCPUOnly) restrictNeuralNetworksToUseCPUOnly;
@property (TB,V_restrictNeuralNetworksFromUsingANE) restrictNeuralNetworksFromUsingANE;
@property (TB,R,N,V_isNeuralNetworkGPUPathForbidden) isNeuralNetworkGPUPathForbidden;
```

## Class methods

```
+[MLInternalSettings supportsSecureCoding];
+[MLInternalSettings globalSettings];
+[MLInternalSettings deviceHasANE];
+[MLInternalSettings globalSettingsFromSettings:];
```

## Instance methods

```
-[MLInternalSettings init];
-[MLInternalSettings encodeWithCoder:];
-[MLInternalSettings initWithCoder:];
-[MLInternalSettings isNeuralNetworkGPUPathForbidden];
-[MLInternalSettings restrictNeuralNetworksFromUsingANE];
-[MLInternalSettings restrictNeuralNetworksToUseCPUOnly];
-[MLInternalSettings setRestrictNeuralNetworksFromUsingANE:];
-[MLInternalSettings setRestrictNeuralNetworksToUseCPUOnly:];
```
