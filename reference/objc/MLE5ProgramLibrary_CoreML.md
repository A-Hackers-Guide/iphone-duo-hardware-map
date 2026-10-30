# `MLE5ProgramLibrary`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
^{e5rt_program_library=} _programLibraryHandle;
@"<MLE5ProgramLibraryImpl>" _impl;
@"NSObject<OS_dispatch_queue>" _lazyInitQueue;
@"MLModelConfiguration" _modelConfiguration;
@"MLProgramE5Container" _container;
```

## Properties

```
@property (T@"<MLE5ProgramLibraryImpl>",R,N,V_impl) impl;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_lazyInitQueue) lazyInitQueue;
@property (T@"MLModelConfiguration",R,N,V_modelConfiguration) modelConfiguration;
@property (T@"MLProgramE5Container",R,N,V_container) container;
@property (T@"NSString",R,C,N) modelDisplayName;
@property (T@"NSArray",R,C,N) functionNames;
@property (T@"NSString",R) serializedMILText;
```

## Instance methods

```
-[MLE5ProgramLibrary impl];
-[MLE5ProgramLibrary newStateForFunctionNamed:stateNames:clientBuffers:error:];
-[MLE5ProgramLibrary prepareAndReturnError:];
-[MLE5ProgramLibrary dealloc];
-[MLE5ProgramLibrary _programLibraryHandleWithForceRespecialization:error:];
-[MLE5ProgramLibrary _allocateStateBufferForFeatureNamed:entryFunctionName:programFunctionNames:error:];
-[MLE5ProgramLibrary modelConfiguration];
-[MLE5ProgramLibrary initWithImpl:container:configuration:];
-[MLE5ProgramLibrary lazyInitQueue];
-[MLE5ProgramLibrary functionNames];
-[MLE5ProgramLibrary createOperationForFunctionName:forceRespecialization:hasRangeShapeInputs:error:];
-[MLE5ProgramLibrary segmentationAnalyticsAndReturnError:];
-[MLE5ProgramLibrary modelDisplayName];
-[MLE5ProgramLibrary initWithContainer:configuration:error:];
-[MLE5ProgramLibrary serializedMILText];
-[MLE5ProgramLibrary container];
```
