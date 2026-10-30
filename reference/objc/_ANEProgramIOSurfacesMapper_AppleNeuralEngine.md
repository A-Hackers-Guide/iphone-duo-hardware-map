# `_ANEProgramIOSurfacesMapper`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"_ANEDeviceController" _deviceController;
@"_ANEDeviceController" _controller;
Q _programHandle;
```

## Properties

```
@property (T@"_ANEDeviceController",R,N,V_controller) controller;
@property (TQ,R,N,V_programHandle) programHandle;
@property (T@"_ANEDeviceController",R,N,V_deviceController) deviceController;
```

## Class methods

```
+[_ANEProgramIOSurfacesMapper initialize];
+[_ANEProgramIOSurfacesMapper new];
+[_ANEProgramIOSurfacesMapper mapperWithController:];
+[_ANEProgramIOSurfacesMapper mapperWithProgramHandle:];
```

## Instance methods

```
-[_ANEProgramIOSurfacesMapper validateRequest:model:];
-[_ANEProgramIOSurfacesMapper unmapIOSurfacesWithModel:request:error:];
-[_ANEProgramIOSurfacesMapper controller];
-[_ANEProgramIOSurfacesMapper deviceController];
-[_ANEProgramIOSurfacesMapper init];
-[_ANEProgramIOSurfacesMapper dealloc];
-[_ANEProgramIOSurfacesMapper mapIOSurfacesWithModel:request:cacheInference:error:];
-[_ANEProgramIOSurfacesMapper prepareANEMemoryMappingParams:request:];
-[_ANEProgramIOSurfacesMapper programHandle];
-[_ANEProgramIOSurfacesMapper initWithController:];
```
