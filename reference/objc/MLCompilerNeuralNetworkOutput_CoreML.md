# `MLCompilerNeuralNetworkOutput`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 2 class methods

## Instance variables

```
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _network;
{shared_ptr<MIL::IRProgram>="__ptr_"^{IRProgram}"__cntrl_"^{__shared_weak_count}} _program;
```

## Properties

```
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},R,N,V_network) network;
@property (T{shared_ptr<MIL::IRProgram>=^{IRProgram}^{__shared_weak_count}},R,N,V_program) program;
```

## Class methods

```
+[MLCompilerNeuralNetworkOutput outputWithEspressoNetwork:];
+[MLCompilerNeuralNetworkOutput outputWithMILProgram:];
```

## Instance methods

```
-[MLCompilerNeuralNetworkOutput network];
-[MLCompilerNeuralNetworkOutput program];
-[MLCompilerNeuralNetworkOutput initWithEspressoNetwork:];
-[MLCompilerNeuralNetworkOutput initWithMILProgram:];
```
