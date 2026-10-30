# `_MTLPipelineCache`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLPipelineCache`
- 3 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _writable;
^{MTLCompilerCache=^^?{os_unfair_lock_s=I}ii} _compilerCache;
B _disableRunTimeCompilation;
```

## Properties

```
@property (TB,R,V_writable) writable;
@property (T^{MTLCompilerCache=^^?{os_unfair_lock_s=I}ii},R,V_compilerCache) cache;
@property (TB,V_disableRunTimeCompilation) disableRunTimeCompilation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLPipelineCache cache];
-[_MTLPipelineCache write];
-[_MTLPipelineCache dealloc];
-[_MTLPipelineCache setDisableRunTimeCompilation:];
-[_MTLPipelineCache disableRunTimeCompilation];
-[_MTLPipelineCache writable];
-[_MTLPipelineCache initWithFilePath:readOnly:deviceInfo:];
```
