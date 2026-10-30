# `_MTL4CompilerTask`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CompilerTaskGGDSPI`
- 12 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _statusMutex;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _statusCondition;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _tokenCondition;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _completionHandlerCondition;
B _hasNoPendingCompletionHandlers;
q _status;
{weak_ptr<MTLCompilerTaskInternal>="__ptr_"^{MTLCompilerTaskInternal}"__cntrl_"^{__shared_weak_count}} _weakCompilerTaskInternal;
B _statusMutexInitialized;
B _statusConditionInitialized;
B _tokenConditionInitialized;
B _completionHandlerConditionInitialized;
@"<MTL4Compiler>" _compiler;
```

## Properties

```
@property (T@"<MTL4Compiler>",R,V_compiler) compiler;
@property (Tq,R,V_status) status;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4CompilerTask compiler];
-[_MTL4CompilerTask waitUntilCompleted];
-[_MTL4CompilerTask tryCancel];
-[_MTL4CompilerTask dealloc];
-[_MTL4CompilerTask status];
-[_MTL4CompilerTask setStatus:];
-[_MTL4CompilerTask clearCompilerTaskInternalIfMatches:];
-[_MTL4CompilerTask initWithCompiler:];
-[_MTL4CompilerTask setCompilerTaskInternal:];
-[_MTL4CompilerTask setHasNoPendingCompletionHandlers];
```
