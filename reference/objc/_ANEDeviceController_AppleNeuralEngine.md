# `_ANEDeviceController`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 5 class methods

## Instance variables

```
B _isPrivileged;
q _usecount;
^{ANEDeviceStruct=^v^v^vCiQB} _device;
Q _programHandle;
```

## Properties

```
@property (Tq,N,V_usecount) usecount;
@property (TB,R,N,V_isPrivileged) isPrivileged;
@property (T^{ANEDeviceStruct=^v^v^vCiQB},N,V_device) device;
@property (TQ,R,N,V_programHandle) programHandle;
```

## Class methods

```
+[_ANEDeviceController initialize];
+[_ANEDeviceController new];
+[_ANEDeviceController controllerWithPrivilegedVM:];
+[_ANEDeviceController controllerWithProgramHandle:];
+[_ANEDeviceController sharedPrivilegedConnection];
```

## Instance methods

```
-[_ANEDeviceController setDevice:];
-[_ANEDeviceController usecount];
-[_ANEDeviceController initWithProgramHandle:priviledged:];
-[_ANEDeviceController device];
-[_ANEDeviceController init];
-[_ANEDeviceController stop];
-[_ANEDeviceController start];
-[_ANEDeviceController isPrivileged];
-[_ANEDeviceController initWithANEPrivilegedVM:];
-[_ANEDeviceController programHandle];
-[_ANEDeviceController setUsecount:];
```
