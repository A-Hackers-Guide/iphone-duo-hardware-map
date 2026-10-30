# `IOGPUMetalResourcePool`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
{_IOGPUMetalResourcePoolPrivate="volatileQueue"{_IOGPUMetalResourceQueue="tqh_first"@"IOGPUMetalPooledResource""tqh_last"^@}"nonvolatileQueue"{_IOGPUMetalResourceQueue="tqh_first"@"IOGPUMetalPooledResource""tqh_last"^@}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"count"i} _priv;
# _resourceClass;
@"IOGPUMetalDevice<MTLDevice>" _device;
^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}} _resourceArgs;
I _resourceArgsSize;
Q age_to_purge;
I generation;
Q _allocatedSize;
```

## Properties

```
@property (T^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}},R,V_resourceArgs) resourceArgs;
@property (TI,R,V_resourceArgsSize) resourceArgsSize;
```

## Instance methods

```
-[IOGPUMetalResourcePool availableCount];
-[IOGPUMetalResourcePool initWithDevice:resourceClass:resourceArgs:resourceArgsSize:options:];
-[IOGPUMetalResourcePool allocatedSize];
-[IOGPUMetalResourcePool dealloc];
-[IOGPUMetalResourcePool setResourceArgs:resourceArgsSize:];
-[IOGPUMetalResourcePool purgeWithLock];
-[IOGPUMetalResourcePool purge];
-[IOGPUMetalResourcePool resourceArgsSize];
-[IOGPUMetalResourcePool resourceArgs];
-[IOGPUMetalResourcePool updateResourcePurgeability];
```
