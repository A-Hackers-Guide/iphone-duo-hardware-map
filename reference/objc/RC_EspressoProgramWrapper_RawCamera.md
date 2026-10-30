# `RC_EspressoProgramWrapper`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 22 instance methods, 5 class methods

## Instance variables

```
B _useE5;
B isLoaded;
i _planIdx;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _path;
@"NSString" _preferredDevice;
^{e5rt_e5_compiler=} _compiler;
^v _ctx;
^{e5rt_program_library=} _programLibrary;
^{e5rt_program_function=} _programFunction;
^v _plan;
^{e5rt_ane_memory_provider=} _aneMemoryProvider;
```

## Properties

```
@property (T@"NSString",R,V_path) path;
@property (T@"NSString",R,V_preferredDevice) preferredDevice;
@property (TB,V_useE5) useE5;
@property (TB,VisLoaded) isLoaded;
@property (T@"NSObject<OS_dispatch_queue>",R,V_queue) queue;
@property (T^{e5rt_program_function=},R,V_programFunction) programFunction;
@property (T^{e5rt_program_library=},R,V_programLibrary) programLibrary;
@property (T^v,R,V_plan) plan;
@property (Ti,R,V_planIdx) planIdx;
@property (T^{e5rt_ane_memory_provider=},V_aneMemoryProvider) aneMemoryProvider;
@property (T^{e5rt_e5_compiler=},V_compiler) compiler;
@property (T^v,V_ctx) ctx;
```

## Class methods

```
+[RC_EspressoProgramWrapper clearCache];
+[RC_EspressoProgramWrapper cache];
+[RC_EspressoProgramWrapper cachedProgramWithPath:];
+[RC_EspressoProgramWrapper cachedProgramWithPath:preferredDevice:];
+[RC_EspressoProgramWrapper isE5ModelPath:];
```

## Instance methods

```
-[RC_EspressoProgramWrapper compiler];
-[RC_EspressoProgramWrapper initWithPath:];
-[RC_EspressoProgramWrapper dealloc];
-[RC_EspressoProgramWrapper programLibrary];
-[RC_EspressoProgramWrapper queue];
-[RC_EspressoProgramWrapper setIsLoaded:];
-[RC_EspressoProgramWrapper isLoaded];
-[RC_EspressoProgramWrapper path];
-[RC_EspressoProgramWrapper preferredDevice];
-[RC_EspressoProgramWrapper ctx];
-[RC_EspressoProgramWrapper plan];
-[RC_EspressoProgramWrapper planIdx];
-[RC_EspressoProgramWrapper programFunction];
-[RC_EspressoProgramWrapper setCtx:];
-[RC_EspressoProgramWrapper aneMemoryProvider];
-[RC_EspressoProgramWrapper initWithPath:preferredDevice:];
-[RC_EspressoProgramWrapper loadAsync];
-[RC_EspressoProgramWrapper loadWait];
-[RC_EspressoProgramWrapper setAneMemoryProvider:];
-[RC_EspressoProgramWrapper setCompiler:];
-[RC_EspressoProgramWrapper setUseE5:];
-[RC_EspressoProgramWrapper useE5];
```
