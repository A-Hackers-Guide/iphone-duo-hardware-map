# `_ANEModel`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 21 instance variables, 21 properties, 63 instance methods, 15 class methods

## Instance variables

```
c _queueDepth;
I _numInputs;
I _numOutputs;
I _perfStatsMask;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _l;
@"NSString" _cacheURLIdentifier;
@"NSURL" _sourceURL;
@"NSURL" _modelURL;
@"NSString" _key;
@"NSUUID" _UUID;
q _identifierSource;
Q _string_id;
Q _programHandle;
Q _intermediateBufferHandle;
@"NSDictionary" _modelAttributes;
@"NSDictionary" _mpsConstants;
@"NSDictionary" _externConstants;
@"_ANEProgramForEvaluation" _program;
Q _state;
@"_ANEProgramIOSurfacesMapper" _mapper;
@"NSMutableArray" _procedures;
```

## Properties

```
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (T@"NSDictionary",&,N,V_modelAttributes) modelAttributes;
@property (TQ,N,V_programHandle) programHandle;
@property (Tc,N,V_queueDepth) queueDepth;
@property (TI,N,V_numInputs) numInputs;
@property (TI,N,V_numOutputs) numOutputs;
@property (TQ,N,V_intermediateBufferHandle) intermediateBufferHandle;
@property (T@"NSString",C,N,V_cacheURLIdentifier) cacheURLIdentifier;
@property (T@"NSDictionary",&,N,V_mpsConstants) mpsConstants;
@property (T{os_unfair_lock_s=I},N,V_l) l;
@property (T@"_ANEProgramForEvaluation",&,N,V_program) program;
@property (TI,N,V_perfStatsMask) perfStatsMask;
@property (TQ,N,V_state) state;
@property (T@"_ANEProgramIOSurfacesMapper",&,N,V_mapper) mapper;
@property (TQ,N,V_string_id) string_id;
@property (T@"NSDictionary",&,N,V_externConstants) externConstants;
@property (T@"NSMutableArray",&,N,V_procedures) procedures;
@property (T@"NSURL",R,N,V_sourceURL) sourceURL;
@property (T@"NSString",R,C,N,V_key) key;
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (Tq,R,N,V_identifierSource) identifierSource;
```

## Class methods

```
+[_ANEModel supportsSecureCoding];
+[_ANEModel modelAtURL:key:];
+[_ANEModel modelWithCacheURLIdentifier:UUID:];
+[_ANEModel uuidV5FromURL:];
+[_ANEModel modelAtURLWithCacheURLIdentifier:key:cacheURLIdentifier:];
+[_ANEModel correctFileURLFormat:];
+[_ANEModel new];
+[_ANEModel uuidV5FromString:];
+[_ANEModel modelAtURL:key:mpsConstants:];
+[_ANEModel modelAtURLWithSourceURL:sourceURL:key:cacheURLIdentifier:];
+[_ANEModel modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:];
+[_ANEModel modelWithCacheURLIdentifier:];
+[_ANEModel modelAtURL:key:externConstants:];
+[_ANEModel modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:];
+[_ANEModel modelAtURL:key:modelAttributes:];
```

## Instance methods

```
-[_ANEModel sourceURL];
-[_ANEModel l];
-[_ANEModel numOutputs];
-[_ANEModel identifierSource];
-[_ANEModel proceduresCount];
-[_ANEModel setProcedures:];
-[_ANEModel setState:];
-[_ANEModel setQueueDepth:];
-[_ANEModel setPerfStatsMask:];
-[_ANEModel setNumInputs:];
-[_ANEModel updateFromModel:shouldUpdateModelURL:shouldUpdateUUID:];
-[_ANEModel procedures];
-[_ANEModel init];
-[_ANEModel updateModelAttributes:state:programHandle:intermediateBufferHandle:queueDepth:numInputs:numOutputs:];
-[_ANEModel numInputs];
-[_ANEModel intermediateBufferHandle];
-[_ANEModel UUID];
-[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:];
-[_ANEModel dealloc];
-[_ANEModel cacheURLIdentifier];
-[_ANEModel getCacheURLIdentifier];
-[_ANEModel updateModelAttributes:state:];
-[_ANEModel setMpsConstants:];
-[_ANEModel setCacheURLIdentifier:];
-[_ANEModel perfStatsMask];
-[_ANEModel setL:];
-[_ANEModel mapper];
-[_ANEModel program];
-[_ANEModel procedureInfoForProcedureIndex:];
-[_ANEModel setMapper:];
-[_ANEModel modelAttributes];
-[_ANEModel initWithModelAtURL:sourceURL:UUID:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:string_id:generateNewStringId:mpsConstants:externConstants:programHandle:intermediateBufferHandle:queueDepth:perfStatsMask:state:];
-[_ANEModel encodeWithCoder:];
-[_ANEModel setModelAttributes:];
-[_ANEModel externConstants];
-[_ANEModel outputSymbolIndicesForProcedureIndex:];
-[_ANEModel inputSymbolIndicesForProcedureIndex:];
-[_ANEModel setNumOutputs:];
-[_ANEModel getUUID];
-[_ANEModel hash];
-[_ANEModel resetOnUnload];
-[_ANEModel description];
-[_ANEModel queueDepth];
-[_ANEModel mpsConstants];
-[_ANEModel initWithCoder:];
-[_ANEModel isEqualToModel:];
-[_ANEModel shallowCopy];
-[_ANEModel initWithModelAtURL:key:identifierSource:cacheURLIdentifier:modelAttributes:standardizeURL:];
-[_ANEModel symbolIndicesForProcedureIndex:indexArrayKey:];
-[_ANEModel setProgramHandle:];
-[_ANEModel initWithModelIdentifier:];
-[_ANEModel string_id];
-[_ANEModel copyWithZone:];
-[_ANEModel programHandle];
-[_ANEModel modelURL];
-[_ANEModel setString_id:];
-[_ANEModel setExternConstants:];
-[_ANEModel isEqual:];
-[_ANEModel setModelURL:];
-[_ANEModel setIntermediateBufferHandle:];
-[_ANEModel setProgram:];
-[_ANEModel key];
-[_ANEModel state];
```
