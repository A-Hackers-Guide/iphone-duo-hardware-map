# `MLE5ProgramLibraryOnDeviceAOTCompilationImpl`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5ProgramLibraryImpl`
- 6 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _milTextURL;
{shared_ptr<MIL::IRProgram>="__ptr_"^{IRProgram}"__cntrl_"^{__shared_weak_count}} _irProgram;
@? _deallocator;
@"MLModelConfiguration" _configuration;
@"MLProgramE5Container" _container;
@"NSString" _serializedMILText;
```

## Properties

```
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
@property (T@"MLProgramE5Container",R,N,V_container) container;
@property (T@"NSString",C,N,V_serializedMILText) serializedMILText;
@property (T@"NSString",R,C,N) modelDisplayName;
```

## Instance methods

```
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl initWithIRProgram:container:configuration:deallocator:];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl dealloc];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl initWithMILTextAtURL:container:configuration:];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl setSerializedMILText:];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl createProgramLibraryHandleWithRespecialization:error:];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl configuration];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl initWithMILTextAtURL:irProgram:deallocator:container:configuration:];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl modelDisplayName];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl serializedMILText];
-[MLE5ProgramLibraryOnDeviceAOTCompilationImpl container];
```
