# `MLNeuralEngineComputeDeviceRegistry`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDeviceRegistryProtocol`
- 1 instance variables, 6 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"MLNeuralEngineComputeDevice" _neuralEngineDevice;
```

## Properties

```
@property (T@"MLNeuralEngineComputeDevice",R,N,V_neuralEngineDevice) neuralEngineDevice;
@property (T@"NSArray",R,C,N) registeredComputeDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLNeuralEngineComputeDeviceRegistry sharedRegistry];
```

## Instance methods

```
-[MLNeuralEngineComputeDeviceRegistry registeredComputeDevices];
-[MLNeuralEngineComputeDeviceRegistry initWithNeuralEngineDevice:];
-[MLNeuralEngineComputeDeviceRegistry neuralEngineDevice];
```
