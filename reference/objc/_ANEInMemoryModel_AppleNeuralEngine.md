# `_ANEInMemoryModel`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 42 instance methods, 3 class methods

## Instance variables

```
c _queueDepth;
B _isMILModel;
I _perfStatsMask;
@"NSDictionary" _modelAttributes;
@"NSString" _hexStringIdentifier;
Q _intermediateBufferHandle;
@"_ANEClient" _sharedConnection;
@"NSURL" _modelURL;
@"NSString" _compilerOptionsFileName;
@"_ANEModel" _model;
Q _string_id;
Q _programHandle;
@"_ANEProgramForEvaluation" _program;
Q _state;
@"_ANEInMemoryModelDescriptor" _descriptor;
@"NSDictionary" _perFileHashes;
```

## Properties

```
@property (T@"_ANEClient",R,N,V_sharedConnection) sharedConnection;
@property (T@"NSDictionary",&,N,V_modelAttributes) modelAttributes;
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (TB,R,N,V_isMILModel) isMILModel;
@property (T@"NSString",C,N,V_compilerOptionsFileName) compilerOptionsFileName;
@property (T@"_ANEModel",&,N,V_model) model;
@property (TQ,R,N,V_string_id) string_id;
@property (TQ,N,V_programHandle) programHandle;
@property (Tc,N,V_queueDepth) queueDepth;
@property (TQ,N,V_intermediateBufferHandle) intermediateBufferHandle;
@property (T@"_ANEProgramForEvaluation",&,N,V_program) program;
@property (TI,N,V_perfStatsMask) perfStatsMask;
@property (TQ,N,V_state) state;
@property (T@"_ANEInMemoryModelDescriptor",&,N,V_descriptor) descriptor;
@property (T@"NSDictionary",C,N,V_perFileHashes) perFileHashes;
@property (T@"NSString",R,C,N,V_hexStringIdentifier) hexStringIdentifier;
```

## Class methods

```
+[_ANEInMemoryModel initialize];
+[_ANEInMemoryModel new];
+[_ANEInMemoryModel inMemoryModelWithDescriptor:];
```

## Instance methods

```
-[_ANEInMemoryModel model];
-[_ANEInMemoryModel setDescriptor:];
-[_ANEInMemoryModel setModel:];
-[_ANEInMemoryModel setState:];
-[_ANEInMemoryModel setQueueDepth:];
-[_ANEInMemoryModel setPerfStatsMask:];
-[_ANEInMemoryModel descriptor];
-[_ANEInMemoryModel sharedConnection];
-[_ANEInMemoryModel init];
-[_ANEInMemoryModel intermediateBufferHandle];
-[_ANEInMemoryModel dealloc];
-[_ANEInMemoryModel perfStatsMask];
-[_ANEInMemoryModel program];
-[_ANEInMemoryModel modelAttributes];
-[_ANEInMemoryModel setModelAttributes:];
-[_ANEInMemoryModel queueDepth];
-[_ANEInMemoryModel setProgramHandle:];
-[_ANEInMemoryModel string_id];
-[_ANEInMemoryModel programHandle];
-[_ANEInMemoryModel modelURL];
-[_ANEInMemoryModel setModelURL:];
-[_ANEInMemoryModel setIntermediateBufferHandle:];
-[_ANEInMemoryModel setProgram:];
-[_ANEInMemoryModel state];
-[_ANEInMemoryModel evaluateWithQoS:options:request:error:];
-[_ANEInMemoryModel hexStringIdentifier];
-[_ANEInMemoryModel loadWithQoS:options:error:];
-[_ANEInMemoryModel purgeCompiledModel];
-[_ANEInMemoryModel unloadWithQoS:error:];
-[_ANEInMemoryModel compileWithQoS:options:error:];
-[_ANEInMemoryModel compiledModelExists];
-[_ANEInMemoryModel compilerOptionsFileName];
-[_ANEInMemoryModel compilerOptionsWithOptions:isCompiledModelCached:];
-[_ANEInMemoryModel initWithDesctiptor:];
-[_ANEInMemoryModel isMILModel];
-[_ANEInMemoryModel localModelPath];
-[_ANEInMemoryModel mapIOSurfacesWithRequest:cacheInference:error:];
-[_ANEInMemoryModel perFileHashes];
-[_ANEInMemoryModel saveModelFiles];
-[_ANEInMemoryModel setCompilerOptionsFileName:];
-[_ANEInMemoryModel setPerFileHashes:];
-[_ANEInMemoryModel unmapIOSurfacesWithRequest:];
```
